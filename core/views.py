from core.models import (
    ChangeTabEvent,
    ElementType,
    EventType,
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
from core.serializers import (
    UserSerializer,
    ChangeTabEventSerializer,
    ElementTypeSerializer,
    EventTypeSerializer,
    KeystrokeEventSerializer,
    MouseClickEventSerializer,
    MousePositionEventSerializer,
    MouseScrollEventSerializer,
    PullRequestSerializer,
    RepositorySerializer,
    SemanticEventSerializer,
    SessionSerializer,
    WindowResolutionEventSerializer,
)
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'change-tab-events': reverse('change-tab-event-list', request=request, format=format),
        'element-types': reverse('element-type-list', request=request, format=format),
        'event-types': reverse('event-type-list', request=request, format=format),
        'keystroke-events': reverse('keystroke-event-list', request=request, format=format),
        'mouse-click-events': reverse('mouse-click-event-list', request=request, format=format),
        'mouse-position-events': reverse('mouse-position-event-list', request=request, format=format),
        'mouse-scroll-events': reverse('mouse-scroll-event-list', request=request, format=format),
        'pull-requests': reverse('pull-request-list', request=request, format=format),
        'repositories': reverse('repository-list', request=request, format=format),
        'semantic-events': reverse('semantic-event-list', request=request, format=format),
        'sessions': reverse('session-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'window-resolution-events': reverse('window-resolution-event-list', request=request, format=format),
    })

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

class RepositoryList(generics.ListCreateAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer

class RepositoryDetail(generics.RetrieveAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer

    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {
            'owner': self.kwargs['owner'],
            'name': self.kwargs['name']
        }
        return get_object_or_404(queryset, **filter)  # Lookup the object

class PullRequestList(generics.ListCreateAPIView):
    queryset = PullRequest.objects.all()
    serializer_class = PullRequestSerializer

class PullRequestDetail(generics.RetrieveAPIView):
    queryset = PullRequest.objects.all()
    serializer_class = PullRequestSerializer

    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        repository = Repository.objects.get(
            owner=self.kwargs['owner'],
            name=self.kwargs['name']
        )
        filter = {
            'repository': repository,
            'pull_request_number': self.kwargs['pull_request_number']
        }
        return get_object_or_404(queryset, **filter)  # Lookup the object

class SessionList(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class SessionDetail(generics.RetrieveAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        if 'pk' in self.kwargs:
            filter = { 'id': self.kwargs['pk'] }
            return get_object_or_404(queryset, **filter)
        user = User.objects.get(username=self.kwargs['username'])
        repository = Repository.objects.get(
            owner=self.kwargs['owner'],
            name=self.kwargs['name']
        )
        pull_request = PullRequest.objects.get(
            repository=repository,
            pull_request_number=self.kwargs['pull_request_number']
        )
        filter = {
            'pull_request': pull_request,
            'user': user
        }
        return get_object_or_404(queryset, **filter)  # Lookup the object

class EventTypeList(generics.ListAPIView):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer

class EventTypeDetail(generics.RetrieveAPIView):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer

class ElementTypeList(generics.ListAPIView):
    queryset = ElementType.objects.all()
    serializer_class = ElementTypeSerializer

class ElementTypeDetail(generics.RetrieveAPIView):
    queryset = ElementType.objects.all()
    serializer_class = ElementTypeSerializer

class SemanticEventList(generics.ListCreateAPIView):
    queryset = SemanticEvent.objects.all()
    serializer_class = SemanticEventSerializer

class SemanticEventDetail(generics.RetrieveAPIView):
    queryset = SemanticEvent.objects.all()
    serializer_class = SemanticEventSerializer

class KeystrokeEventList(generics.ListCreateAPIView):
    queryset = KeystrokeEvent.objects.all()
    serializer_class = KeystrokeEventSerializer

class KeystrokeEventDetail(generics.RetrieveAPIView):
    queryset = KeystrokeEvent.objects.all()
    serializer_class = KeystrokeEventSerializer

class MousePositionEventList(generics.ListCreateAPIView):
    queryset = MousePositionEvent.objects.all()
    serializer_class = MousePositionEventSerializer

class MousePositionEventDetail(generics.RetrieveAPIView):
    queryset = MousePositionEvent.objects.all()
    serializer_class = MousePositionEventSerializer

class MouseClickEventList(generics.ListCreateAPIView):
    queryset = MouseClickEvent.objects.all()
    serializer_class = MouseClickEventSerializer

class MouseClickEventDetail(generics.RetrieveAPIView):
    queryset = MouseClickEvent.objects.all()
    serializer_class = MouseClickEventSerializer

class MouseScrollEventList(generics.ListCreateAPIView):
    queryset = MouseScrollEvent.objects.all()
    serializer_class = MouseScrollEventSerializer

class MouseScrollEventDetail(generics.RetrieveAPIView):
    queryset = MouseScrollEvent.objects.all()
    serializer_class = MouseScrollEventSerializer

class WindowResolutionEventList(generics.ListCreateAPIView):
    queryset = WindowResolutionEvent.objects.all()
    serializer_class = WindowResolutionEventSerializer

class WindowResolutionEventDetail(generics.RetrieveAPIView):
    queryset = WindowResolutionEvent.objects.all()
    serializer_class = WindowResolutionEventSerializer

class ChangeTabEventList(generics.ListCreateAPIView):
    queryset = ChangeTabEvent.objects.all()
    serializer_class = ChangeTabEventSerializer

class ChangeTabEventDetail(generics.RetrieveAPIView):
    queryset = ChangeTabEvent.objects.all()
    serializer_class = ChangeTabEventSerializer
