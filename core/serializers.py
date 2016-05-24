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
        kwargs = {
            'owner': getattr(repository, 'owner'),
            'name': getattr(repository, 'name'),
            'pull_request_number': getattr(obj, 'pull_request_number')
        }
        return self.reverse(view_name, kwargs=kwargs, request=request, format=format)

class SessionHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        if obj.pk is None:
            return None
        print(obj)
        pull_request = getattr(obj, 'pull_request')
        repository = getattr(pull_request, 'repository')
        user = getattr(obj, 'user')
        kwargs = {
            'username': getattr(user, 'username'),
            'owner': getattr(repository, 'owner'),
            'name': getattr(repository, 'name'),
            'pull_request_number': getattr(pull_request, 'pull_request_number')
        }
        return self.reverse(view_name, kwargs=kwargs, request=request, format=format)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    sessions = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='session-pk-detail'
    )

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'sessions')
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
    url = PullRequestHyperlinkedIdentityField(view_name='pull-request-detail')
    repository = RepositorySerializer()

    class Meta:
        model = PullRequest
        fields = ('url', 'repository', 'pull_request_number')

    def create(self, validated_data):
        repository = validated_data.pop('repository')
        (repository, _) = Repository.objects.get_or_create(**repository)
        (pullrequest, _) = PullRequest.objects.get_or_create(repository=repository, **validated_data)
        return pullrequest

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    url = SessionHyperlinkedIdentityField(view_name='session-detail')
    pull_request = PullRequestSerializer()
    user = UserSerializer()

    class Meta:
        model = Session
        fields = ('url', 'id', 'pull_request', 'user')

    def create(self, validated_data):
        pull_request = validated_data.pop('pull_request')
        repository = pull_request.pop('repository')
        (repository, _) = Repository.objects.get_or_create(**repository)
        (pull_request, _) = PullRequest.objects.get_or_create(repository=repository, **pull_request)
        user = validated_data.pop('user')
        (user, _) = User.objects.get_or_create(**user)
        (session, _) = Session.objects.get_or_create(pull_request=pull_request, user=user, **validated_data)
        return session

class EventTypeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='event-type-detail')

    class Meta:
        model = EventType
        fields = ('url', 'id', 'name')

class ElementTypeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='element-type-detail')

    class Meta:
        model = ElementType
        fields = ('url', 'id', 'name')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    @property
    def event_model(self):
        raise NotImplementedError

    class Meta:
        abstract = True

    def create(self, validated_data):
        session = validated_data.pop('session')
        pull_request = session.pop('pull_request')
        repository = pull_request.pop('repository')
        user = session.pop('user')
        (repository, _) = Repository.objects.get_or_create(**repository)
        (pull_request, _) = PullRequest.objects.get_or_create(repository=repository, **pull_request)
        (user, _) = User.objects.get_or_create(**user)
        (session, _) = Session.objects.get_or_create(pull_request=pull_request, user=user)
        (event, _) = self.event_model.objects.get_or_create(session=session, **validated_data)
        return event

class SemanticEventSerializer(EventSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='semantic-event-detail')
    session = SessionSerializer()
    event_type = serializers.HyperlinkedRelatedField(view_name='event-type-detail', queryset=EventType.objects.all())
    element_type = serializers.HyperlinkedRelatedField(view_name='element-type-detail', queryset=ElementType.objects.all())
    event_model = SemanticEvent

    class Meta:
        model = SemanticEvent
        fields = ('url', 'id', 'session', 'event_type', 'element_type', 'started_at', 'duration')

class KeystrokeEventSerializer(EventSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='keystroke-event-detail')
    session = SessionSerializer()
    event_model = KeystrokeEvent

    class Meta:
        model = KeystrokeEvent
        fields = ('url', 'id', 'session', 'keystroke', 'created_at')

class MousePositionEventSerializer(EventSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='mouse-position-event-detail')
    session = SessionSerializer()
    event_model = MousePositionEvent

    class Meta:
        model = MousePositionEvent
        fields = ('url', 'id', 'session', 'position_x', 'position_y', 'viewport_x', 'viewport_y', 'created_at')

class MouseClickEventSerializer(EventSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='mouse-click-event-detail')
    session = SessionSerializer()
    event_model = MouseClickEvent

    class Meta:
        model = MouseClickEvent
        fields = ('url', 'id', 'session', 'created_at')

class MouseScrollEventSerializer(EventSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='mouse-scroll-event-detail')
    session = SessionSerializer()
    event_model = MouseScrollEvent

    class Meta:
        model = MouseScrollEvent
        fields = ('url', 'id', 'session', 'viewport_x', 'viewport_y', 'created_at')

class WindowResolutionEventSerializer(EventSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='window-resolution-event-detail')
    session = SessionSerializer()
    event_model = WindowResolutionEvent

    class Meta:
        model = WindowResolutionEvent
        fields = ('url', 'id', 'session', 'width', 'height', 'created_at')
