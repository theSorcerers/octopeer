from core.models import (
    ChangeTabEvent,
    ElementType,
    EventType,
    HTMLPage,
    KeystrokeEvent,
    MouseClickEvent,
    MousePositionEvent,
    MouseScrollEvent,
    PullRequest,
    Repository,
    SemanticEvent,
    Session,
    User,
    WindowResolutionEvent,
)
import core.serializer_fields as fields
from rest_framework import serializers


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

    def create(self, validated_data):
        user, created = User.objects.get_or_create(**validated_data)
        return user

class RepositorySerializer(serializers.HyperlinkedModelSerializer):
    url = fields.RepositoryHyperlinkedIdentityField(view_name='repository-detail')

    class Meta:
        model = Repository
        fields = ('url', 'owner', 'name', 'platform')

    def create(self, validated_data):
        repository, created = Repository.objects.get_or_create(**validated_data)
        return repository

class PullRequestSerializer(serializers.HyperlinkedModelSerializer):
    url = fields.PullRequestHyperlinkedIdentityField(view_name='pull-request-detail')
    repository = RepositorySerializer()

    class Meta:
        model = PullRequest
        fields = ('url', 'repository', 'pull_request_number')

    def create(self, validated_data):
        repository = validated_data.pop('repository')
        repository, created = Repository.objects.get_or_create(**repository)
        pull_request, created = PullRequest.objects.get_or_create(repository=repository, **validated_data)
        return pull_request

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    url = fields.SessionHyperlinkedIdentityField(view_name='session-detail')
    pull_request = PullRequestSerializer()
    user = UserSerializer()
    semantic_events = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='semantic-event-detail'
    )

    class Meta:
        model = Session
        fields = ('url', 'id', 'pull_request', 'user', 'semantic_events')

    def create(self, validated_data):
        user = validated_data.pop('user')
        pull_request = validated_data.pop('pull_request')
        repository = pull_request.pop('repository')
        user, created = User.objects.get_or_create(**user)
        repository, created = Repository.objects.get_or_create(**repository)
        pull_request, created = PullRequest.objects.get_or_create(repository=repository, **pull_request)
        session, created = Session.objects.get_or_create(pull_request=pull_request, user=user)
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
    session = SessionSerializer()

    class Meta:
        abstract = True

    def create(self, validated_data):
        session = validated_data.pop('session')
        user = session.pop('user')
        pull_request = session.pop('pull_request')
        repository = pull_request.pop('repository')
        user, created = User.objects.get_or_create(**user)
        repository, created = Repository.objects.get_or_create(**repository)
        pull_request, created = PullRequest.objects.get_or_create(repository=repository, **pull_request)
        session, created = Session.objects.get_or_create(pull_request=pull_request, user=user)
        event, created = self.Meta.model.objects.get_or_create(session=session, **validated_data)
        return event

class SemanticEventSerializer(EventSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='semantic-event-detail')
    event_type = serializers.PrimaryKeyRelatedField(queryset=EventType.objects.all())
    element_type = serializers.PrimaryKeyRelatedField(queryset=ElementType.objects.all())

    class Meta:
        model = SemanticEvent
        fields = ('url', 'id', 'session', 'event_type', 'element_type', 'created_at')

class KeystrokeEventSerializer(EventSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='keystroke-event-detail')

    class Meta:
        model = KeystrokeEvent
        fields = ('url', 'id', 'session', 'keystroke', 'key_down_at', 'key_up_at')

class MousePositionEventSerializer(EventSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='mouse-position-event-detail')

    class Meta:
        model = MousePositionEvent
        fields = ('url', 'id', 'session', 'position_x', 'position_y', 'viewport_x', 'viewport_y', 'created_at')

class MouseClickEventSerializer(EventSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='mouse-click-event-detail')

    class Meta:
        model = MouseClickEvent
        fields = ('url', 'id', 'session', 'created_at')

class MouseScrollEventSerializer(EventSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='mouse-scroll-event-detail')

    class Meta:
        model = MouseScrollEvent
        fields = ('url', 'id', 'session', 'viewport_x', 'viewport_y', 'created_at')

class WindowResolutionEventSerializer(EventSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='window-resolution-event-detail')

    class Meta:
        model = WindowResolutionEvent
        fields = ('url', 'id', 'session', 'width', 'height', 'created_at')

class ChangeTabEventSerializer(EventSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='change-tab-event-detail')

    class Meta:
        model = ChangeTabEvent
        fields = ('url', 'id', 'session', 'url', 'created_at')

class HTMLPageSerializer(EventSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='html-page-detail')

    class Meta:
        model = HTMLPage
        fields = ('url', 'id', 'session', 'dom', 'created_at')
