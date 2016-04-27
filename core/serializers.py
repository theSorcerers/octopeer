from rest_framework import serializers
from core.models import User, PullRequest, Session, Event, EventPosition, EventType

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PullRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PullRequest
        fields = '__all__'

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventPositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventPosition
        fields = '__all__'

class EventTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventType
        fields = '__all__'
