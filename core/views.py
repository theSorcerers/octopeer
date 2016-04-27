from rest_framework import viewsets, mixins
from core.models import User, PullRequest, Session, Event, EventPosition, EventType
from core.serializers import UserSerializer, PullRequestSerializer, SessionSerializer, EventSerializer, EventPositionSerializer, EventTypeSerializer

class CreateListRetrieveViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    pass

class UserViewSet(CreateListRetrieveViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PullRequestViewSet(CreateListRetrieveViewSet):
    queryset = PullRequest.objects.all()
    serializer_class = PullRequestSerializer

class SessionViewSet(CreateListRetrieveViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class EventViewSet(CreateListRetrieveViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventPositionViewSet(CreateListRetrieveViewSet):
    queryset = EventPosition.objects.all()
    serializer_class = EventPositionSerializer

class EventTypeViewSet(CreateListRetrieveViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
