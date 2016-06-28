from core.models import (
    ChangeTabEvent,
    ElementType,
    EventType,
    FilePosition,
    HTMLPage,
    KeystrokeEvent,
    KeystrokeType,
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
    url = fields.UserHyperLinkedIdentityField(view_name='user-detail')

    class Meta:
        model = User
        fields = ('url', 'id', 'username')
        validators = []

    def create(self, validated_data):
        user, created = User.objects.get_or_create(**validated_data)
        return user

class RepositorySerializer(serializers.HyperlinkedModelSerializer):
    url = fields.RepositoryHyperlinkedIdentityField(view_name='repository-detail')

    class Meta:
        model = Repository
        fields = ('url', 'owner', 'name', 'platform')
        validators = []

    def create(self, validated_data):
        repository, created = Repository.objects.get_or_create(**validated_data)
        return repository

class PullRequestSerializer(serializers.HyperlinkedModelSerializer):
    url = fields.PullRequestHyperlinkedIdentityField(view_name='pull-request-detail')
    repository = RepositorySerializer()

    class Meta:
        model = PullRequest
        fields = ('url', 'repository', 'pull_request_number')
        validators = []

    def create(self, validated_data):
        repository = validated_data.pop('repository')
        repository, created = Repository.objects.get_or_create(**repository)
        pull_request, created = PullRequest.objects.get_or_create(repository=repository, **validated_data)
        return pull_request

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    url = fields.SessionHyperlinkedIdentityField(view_name='session-detail')
    pull_request = PullRequestSerializer()
    user = UserSerializer()

    class Meta:
        model = Session
        fields = ('url', 'id', 'pull_request', 'user')
        validators = []

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

class FilePositionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='file-position-detail')
    semantic_event = serializers.PrimaryKeyRelatedField(queryset=SemanticEvent.objects.all())

    class Meta:
        model = FilePosition
        fields = ('url', 'id', 'semantic_event', 'commit_hash', 'filename', 'line_number')

class KeystrokeTypeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='keystroke-type-detail')

    class Meta:
        model = KeystrokeType
        fields = ('url', 'id', 'name')

class KeystrokeEventSerializer(EventSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='keystroke-event-detail')
    keystroke_type = serializers.PrimaryKeyRelatedField(queryset=KeystrokeType.objects.all())

    class Meta:
        model = KeystrokeEvent
        fields = ('url', 'id', 'session', 'keystroke', 'keystroke_type', 'created_at')

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
