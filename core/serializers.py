from rest_framework import serializers
from core.models import User, Repository, PullRequest, Session, EventType, ElementType, SemanticEvent, EventPosition, KeystrokeEvent, MousePositionEvent, MouseClickEvent, MouseScrollEvent, WindowResolutionEvent
from rest_framework.reverse import reverse

class MultiKeyHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
    identity_args = {}
    def get_url(self, obj, view_name, request, format):
        if obj.pk is None:
            return None
        kwargs = dict((url_kw, getattr(obj, prop)) for url_kw, prop in self.identity_args.items())
        return self.reverse(view_name, kwargs=kwargs, request=request, format=format)

class PullRequestHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        if obj.pk is None:
            return None
        repository = getattr(obj, 'repository')
        # if repository.pk is None:
        #     return None
        kwargs = {
            'owner': getattr(repository, 'owner'),
            'name': getattr(repository, 'name'),
            'pull_request_number': getattr(obj, 'pull_request_number')
        }
        return self.reverse(view_name, kwargs=kwargs, request=request, format=format)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username')
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }

class RepositoryHyperlinkedIdentityField(MultiKeyHyperlinkedIdentityField):
    identity_args = {
        'owner': 'owner',
        'name': 'name'
    }

class RepositorySerializer(serializers.HyperlinkedModelSerializer):
    url = RepositoryHyperlinkedIdentityField(view_name='repository-detail')

    class Meta:
        model = Repository
        fields = ('url', 'owner', 'name', 'platform')

class PullRequestSerializer(serializers.HyperlinkedModelSerializer):
    # url = PullRequestHyperlinkedIdentityField(view_name='pullrequest-detail')
    repository = RepositorySerializer()

    class Meta:
        model = PullRequest
        fields = ('url', 'repository', 'pull_request_number')

    def create(self, validated_data):
        repository = validated_data.pop('repository')
        repository = Repository.objects.create(**repository)
        pullrequest = PullRequest.objects.create(repository=repository, **validated_data)
        return pullrequest

# class SessionSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Session
#         fields = ('pull_request', 'user')
#
# class EventTypeSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = EventType
#         fields = '__all__'
#
# class ElementTypeSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = ElementType
#         fields = '__all__'
#
# class SemanticEventSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = SemanticEvent
#         fields = '__all__'
#
# class EventPositionSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = EventPosition
#         fields = '__all__'
#
# class KeystrokeEventSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = KeystrokeEvent
#         fields = '__all__'
#
# class MousePositionEventSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = MousePositionEvent
#         fields = '__all__'
#
# class MouseClickEventSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = MouseClickEvent
#         fields = '__all__'
#
# class MouseScrollEventSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = MouseScrollEvent
#         fields = '__all__'
#
# class WindowResolutionEventSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = WindowResolutionEvent
#         fields = '__all__'
