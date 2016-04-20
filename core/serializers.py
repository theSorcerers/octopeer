from rest_framework import serializers
from core.models import User, Session, Event, KeystrokeEvent, TextSelectionEvent, MouseHoverEvent, MouseMovementEvent, MouseClickEvent, MouseScrollEvent

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class KeystrokeEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KeystrokeEvent
        fields = '__all__'

class TextSelectionEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TextSelectionEvent
        fields = '__all__'

class MouseHoverEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MouseHoverEvent
        fields = '__all__'

class MouseMovementEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MouseMovementEvent
        fields = '__all__'

class MouseClickEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MouseClickEvent
        fields = '__all__'

class MouseScrollEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MouseScrollEvent
        fields = '__all__'
