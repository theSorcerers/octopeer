from core.models import (
    ChangeTabEvent,
    ElementType,
    EventType,
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
from core.serializers import (
    UserSerializer,
    ChangeTabEventSerializer,
    ElementTypeSerializer,
    EventTypeSerializer,
    HTMLPageSerializer,
    KeystrokeEventSerializer,
    KeystrokeTypeSerializer,
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
        'html-pages': reverse('html-page-list', request=request, format=format),
        'keystroke-events': reverse('keystroke-event-list', request=request, format=format),
        'keystroke-types': reverse('keystroke-type-list', request=request, format=format),
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

class EventUserFilter(generics.ListAPIView):
    @property
    def queryset(self):
        raise NotImplementedError

    class Meta:
        abstract = True

    def get_queryset(self):
        username = self.kwargs['username']
        user = User.objects.get(username=username)
        sessions = Session.objects.filter(user=user)
        return self.queryset.filter(session__in=sessions)

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

class SessionUserList(generics.ListAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        date_from = self.request.query_params.get('date_from', None)
        date_to = self.request.query_params.get('date_to', None)
        user = User.objects.get(username=username)
        sessions = self.queryset.filter(user=user)
        if date_from is not None:
            sessions = sessions.filter(created_at__gte=date_from)
        if date_to is not None:
            sessions = sessions.filter(created_at__gte=date_to)
        return sessions

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

class SemanticEventUserList(EventUserFilter):
    queryset = SemanticEvent.objects.all()
    serializer_class = SemanticEventSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        event_type = self.request.query_params.get('event_type', None)
        element_type = self.request.query_params.get('element_type', None)
        date_from = self.request.query_params.get('date_from', None)
        date_to = self.request.query_params.get('date_to', None)
        user = User.objects.get(username=username)
        sessions = Session.objects.filter(user=user)
        semantic_events = self.queryset.filter(session__in=sessions)
        if event_type is not None:
            semantic_events = semantic_events.filter(event_type=event_type)
        if element_type is not None:
            semantic_events = semantic_events.filter(element_type=element_type)
        if date_from is not None:
            semantic_events = semantic_events.filter(created_at__gte=date_from)
        if date_to is not None:
            semantic_events = semantic_events.filter(created_at__gte=date_to)
        return semantic_events

class SemanticEventSessionList(EventUserFilter):
    queryset = SemanticEvent.objects.all()
    serializer_class = SemanticEventSerializer

    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['username'])
        repository = Repository.objects.get(
            owner=self.kwargs['owner'],
            name=self.kwargs['name']
        )
        pull_request = PullRequest.objects.get(
            repository=repository,
            pull_request_number=self.kwargs['pull_request_number']
        )
        session = Session.objects.get(
            pull_request=pull_request,
            user=user
        )
        semantic_events = self.queryset.filter(session=session)
        return semantic_events

class SemanticEventDetail(generics.RetrieveAPIView):
    queryset = SemanticEvent.objects.all()
    serializer_class = SemanticEventSerializer

class KeystrokeEventList(generics.ListCreateAPIView):
    queryset = KeystrokeEvent.objects.all()
    serializer_class = KeystrokeEventSerializer

class KeystrokeEventUserList(EventUserFilter):
    queryset = KeystrokeEvent.objects.all()
    serializer_class = KeystrokeEventSerializer

class KeystrokeEventDetail(generics.RetrieveAPIView):
    queryset = KeystrokeEvent.objects.all()
    serializer_class = KeystrokeEventSerializer

class KeystrokeTypeList(generics.ListAPIView):
    queryset = KeystrokeType.objects.all()
    serializer_class = KeystrokeTypeSerializer

class KeystrokeTypeDetail(generics.RetrieveAPIView):
    queryset = KeystrokeType.objects.all()
    serializer_class = KeystrokeTypeSerializer

class MousePositionEventList(generics.ListCreateAPIView):
    queryset = MousePositionEvent.objects.all()
    serializer_class = MousePositionEventSerializer

class MousePositionEventUserList(EventUserFilter):
    queryset = MousePositionEvent.objects.all()
    serializer_class = MousePositionEventSerializer

class MousePositionEventDetail(generics.RetrieveAPIView):
    queryset = MousePositionEvent.objects.all()
    serializer_class = MousePositionEventSerializer

class MouseClickEventList(generics.ListCreateAPIView):
    queryset = MouseClickEvent.objects.all()
    serializer_class = MouseClickEventSerializer

class MouseClickEventUserList(EventUserFilter):
    queryset = MouseClickEvent.objects.all()
    serializer_class = MouseClickEventSerializer

class MouseClickEventDetail(generics.RetrieveAPIView):
    queryset = MouseClickEvent.objects.all()
    serializer_class = MouseClickEventSerializer

class MouseScrollEventList(generics.ListCreateAPIView):
    queryset = MouseScrollEvent.objects.all()
    serializer_class = MouseScrollEventSerializer

class MouseScrollEventUserList(EventUserFilter):
    queryset = MouseScrollEvent.objects.all()
    serializer_class = MouseScrollEventSerializer

class MouseScrollEventDetail(generics.RetrieveAPIView):
    queryset = MouseScrollEvent.objects.all()
    serializer_class = MouseScrollEventSerializer

class WindowResolutionEventList(generics.ListCreateAPIView):
    queryset = WindowResolutionEvent.objects.all()
    serializer_class = WindowResolutionEventSerializer

class WindowResolutionEventUserList(EventUserFilter):
    queryset = WindowResolutionEvent.objects.all()
    serializer_class = WindowResolutionEventSerializer

class WindowResolutionEventDetail(generics.RetrieveAPIView):
    queryset = WindowResolutionEvent.objects.all()
    serializer_class = WindowResolutionEventSerializer

class ChangeTabEventList(generics.ListCreateAPIView):
    queryset = ChangeTabEvent.objects.all()
    serializer_class = ChangeTabEventSerializer

class ChangeTabEventUserList(EventUserFilter):
    queryset = ChangeTabEvent.objects.all()
    serializer_class = ChangeTabEventSerializer

class ChangeTabEventDetail(generics.RetrieveAPIView):
    queryset = ChangeTabEvent.objects.all()
    serializer_class = ChangeTabEventSerializer

class HTMLPageList(generics.ListCreateAPIView):
    queryset = HTMLPage.objects.all()
    serializer_class = HTMLPageSerializer

class HTMLPageUserList(EventUserFilter):
    queryset = HTMLPage.objects.all()
    serializer_class = HTMLPageSerializer

class HTMLPageDetail(generics.RetrieveAPIView):
    queryset = HTMLPage.objects.all()
    serializer_class = HTMLPageSerializer
