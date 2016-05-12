from rest_framework import viewsets, mixins
from core.models import User, Repository, PullRequest, Session, EventType, ElementType, SemanticEvent, EventPosition, KeystrokeEvent, MousePositionEvent, MouseClickEvent, MouseScrollEvent, WindowResolutionEvent
from core.serializers import UserSerializer, RepositorySerializer, PullRequestSerializer, SessionSerializer, EventTypeSerializer, ElementTypeSerializer, SemanticEventSerializer, EventPositionSerializer, KeystrokeEventSerializer, MousePositionEventSerializer, MouseClickEventSerializer, MouseScrollEventSerializer, WindowResolutionEventSerializer

class CreateListRetrieveViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    pass

class UserViewSet(CreateListRetrieveViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RepositoryViewSet(CreateListRetrieveViewSet):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer

class PullRequestViewSet(CreateListRetrieveViewSet):
    queryset = PullRequest.objects.all()
    serializer_class = PullRequestSerializer

class SessionViewSet(CreateListRetrieveViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class EventTypeViewSet(CreateListRetrieveViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer

class ElementTypeViewSet(CreateListRetrieveViewSet):
    queryset = ElementType.objects.all()
    serializer_class = ElementTypeSerializer

class SemanticEventViewSet(CreateListRetrieveViewSet):
    queryset = SemanticEvent.objects.all()
    serializer_class = SemanticEventSerializer

class EventPositionViewSet(CreateListRetrieveViewSet):
    queryset = EventPosition.objects.all()
    serializer_class = EventPositionSerializer

class KeystrokeEventViewSet(CreateListRetrieveViewSet):
    queryset = KeystrokeEvent.objects.all()
    serializer_class = KeystrokeEventSerializer

class MousePositionEventViewSet(CreateListRetrieveViewSet):
    queryset = MousePositionEvent.objects.all()
    serializer_class = MousePositionEventSerializer

class MouseClickEventViewSet(CreateListRetrieveViewSet):
    queryset = MouseClickEvent.objects.all()
    serializer_class = MouseClickEventSerializer

class MouseScrollEventViewSet(CreateListRetrieveViewSet):
    queryset = MouseScrollEvent.objects.all()
    serializer_class = MouseScrollEventSerializer

class WindowResolutionEventViewSet(CreateListRetrieveViewSet):
    queryset = WindowResolutionEvent.objects.all()
    serializer_class = WindowResolutionEventSerializer
