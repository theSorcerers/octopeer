from rest_framework import serializers
from core.models import User, Repository, PullRequest, Session, EventType, ElementType, SemanticEvent, EventPosition, KeystrokeEvent, MousePositionEvent, MouseClickEvent, MouseScrollEvent, WindowResolutionEvent

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RepositorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Repository
        fields = '__all__'

class PullRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PullRequest
        fields = '__all__'

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class EventTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventType
        fields = ('url', 'id', 'name')

class ElementTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ElementType
        fields = ('url', 'id', 'name')

class SemanticEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SemanticEvent
        fields = '__all__'

class EventPositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventPosition
        fields = '__all__'

class KeystrokeEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KeystrokeEvent
        fields = '__all__'

class MousePositionEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MousePositionEvent
        fields = '__all__'

class MouseClickEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MouseClickEvent
        fields = '__all__'

class MouseScrollEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MouseScrollEvent
        fields = '__all__'

class WindowResolutionEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WindowResolutionEvent
        fields = '__all__'
