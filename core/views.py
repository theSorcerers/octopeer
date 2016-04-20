from rest_framework import viewsets, mixins
from core.models import User, Session, KeystrokeEvent, TextSelectionEvent, MouseHoverEvent, MouseMovementEvent, MouseClickEvent, MouseScrollEvent
from core.serializers import UserSerializer, SessionSerializer, KeystrokeEventSerializer, TextSelectionEventSerializer, MouseHoverEventSerializer, MouseMovementEventSerializer, MouseClickEventSerializer, MouseScrollEventSerializer

class CreateListRetrieveViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    pass

class UserViewSet(CreateListRetrieveViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SessionViewSet(CreateListRetrieveViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class KeystrokeEventViewSet(CreateListRetrieveViewSet):
    queryset = KeystrokeEvent.objects.all()
    serializer_class = KeystrokeEventSerializer

class TextSelectionEventViewSet(CreateListRetrieveViewSet):
    queryset = TextSelectionEvent.objects.all()
    serializer_class = TextSelectionEventSerializer

class MouseHoverEventViewSet(CreateListRetrieveViewSet):
    queryset = MouseHoverEvent.objects.all()
    serializer_class = MouseHoverEventSerializer

class MouseMovementEventViewSet(CreateListRetrieveViewSet):
    queryset = MouseMovementEvent.objects.all()
    serializer_class = MouseMovementEventSerializer

class MouseClickEventViewSet(CreateListRetrieveViewSet):
    queryset = MouseClickEvent.objects.all()
    serializer_class = MouseClickEventSerializer

class MouseScrollEventViewSet(CreateListRetrieveViewSet):
    queryset = MouseScrollEvent.objects.all()
    serializer_class = MouseScrollEventSerializer
