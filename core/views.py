from rest_framework import viewsets, mixins, generics
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from core.models import User, Repository, PullRequest, Session, EventType, ElementType, SemanticEvent, EventPosition, KeystrokeEvent, MousePositionEvent, MouseClickEvent, MouseScrollEvent, WindowResolutionEvent
from core.serializers import UserSerializer, RepositorySerializer, PullRequestSerializer, SessionSerializer, EventTypeSerializer, ElementTypeSerializer, SemanticEventSerializer, KeystrokeEventSerializer
# , , MousePositionEventSerializer, MouseClickEventSerializer, MouseScrollEventSerializer, WindowResolutionEventSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'repositories': reverse('repository-list', request=request, format=format),
        'pull-requests': reverse('pull-request-list', request=request, format=format),
        'sessions': reverse('session-list', request=request, format=format),
        'event-types': reverse('event-type-list', request=request, format=format),
        'element-types': reverse('element-type-list', request=request, format=format),
        'semantic-events': reverse('semantic-event-list', request=request, format=format),
        'keystroke-events': reverse('keystroke-event-list', request=request, format=format),
    })

class MultipleFieldLookupMixin(object):
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            filter[field] = self.kwargs[field]
        return get_object_or_404(queryset, **filter)  # Lookup the object

class CreateListRetrieveViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    pass

class MultipleFieldRetrieveAPIView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    pass

class PullRequestRetrieveAPIView(generics.RetrieveAPIView):
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        owner = self.kwargs['owner']
        name = self.kwargs['name']
        repository = Repository.objects.get(owner=owner, name=name)
        filter = {
            'repository': repository,
            'pull_request_number': self.kwargs['pull_request_number']
        }
        return get_object_or_404(queryset, **filter)  # Lookup the object

class SessionRetrieveAPIView(generics.RetrieveAPIView):
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        username = self.kwargs['username']
        owner = self.kwargs['owner']
        name = self.kwargs['name']
        pull_request_number = self.kwargs['pull_request_number']
        user = User.objects.get(username=username)
        repository = Repository.objects.get(owner=owner, name=name)
        pull_request = PullRequest.objects.get(repository=repository, pull_request_number=pull_request_number)
        filter = {
            'pull_request': pull_request,
            'user': user
        }
        return get_object_or_404(queryset, **filter)  # Lookup the object

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

class RepositoryDetail(MultipleFieldRetrieveAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
    lookup_fields = ('owner', 'name')

class PullRequestList(generics.ListCreateAPIView):
    queryset = PullRequest.objects.all()
    serializer_class = PullRequestSerializer

class PullRequestDetail(PullRequestRetrieveAPIView):
    queryset = PullRequest.objects.all()
    serializer_class = PullRequestSerializer

class SessionList(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class SessionDetail(SessionRetrieveAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class EventTypeList(generics.ListCreateAPIView):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer

class EventTypeDetail(generics.RetrieveAPIView):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer

class ElementTypeList(generics.ListCreateAPIView):
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
