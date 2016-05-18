from rest_framework import viewsets, mixins, generics
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from core.models import User, Repository, PullRequest, Session, EventType, ElementType, SemanticEvent, EventPosition, KeystrokeEvent, MousePositionEvent, MouseClickEvent, MouseScrollEvent, WindowResolutionEvent
from core.serializers import UserSerializer, RepositorySerializer, PullRequestSerializer
# , SessionSerializer, EventTypeSerializer, ElementTypeSerializer, SemanticEventSerializer, EventPositionSerializer, KeystrokeEventSerializer, MousePositionEventSerializer, MouseClickEventSerializer, MouseScrollEventSerializer, WindowResolutionEventSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'repositories': reverse('repository-list', request=request, format=format),
        'pullrequests': reverse('pullrequest-list', request=request, format=format),
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

# class CreateListRetrieveViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, MultipleFieldLookupMixin, viewsets.GenericViewSet):
#     pass

class MultipleFieldRetrieveAPIView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    pass

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

class PullRequestDetail(MultipleFieldRetrieveAPIView):
    queryset = PullRequest.objects.all()
    serializer_class = PullRequestSerializer
    lookup_fields = ('repository', 'pull_request_number')

# class SessionViewSet(CreateListRetrieveViewSet):
#     queryset = Session.objects.all()
#     serializer_class = SessionSerializer
#
# class EventTypeViewSet(CreateListRetrieveViewSet):
#     queryset = EventType.objects.all()
#     serializer_class = EventTypeSerializer
#
# class ElementTypeViewSet(CreateListRetrieveViewSet):
#     queryset = ElementType.objects.all()
#     serializer_class = ElementTypeSerializer
#
# class SemanticEventViewSet(CreateListRetrieveViewSet):
#     queryset = SemanticEvent.objects.all()
#     serializer_class = SemanticEventSerializer
#
# class EventPositionViewSet(CreateListRetrieveViewSet):
#     queryset = EventPosition.objects.all()
#     serializer_class = EventPositionSerializer
#
# class KeystrokeEventViewSet(CreateListRetrieveViewSet):
#     queryset = KeystrokeEvent.objects.all()
#     serializer_class = KeystrokeEventSerializer
#
# class MousePositionEventViewSet(CreateListRetrieveViewSet):
#     queryset = MousePositionEvent.objects.all()
#     serializer_class = MousePositionEventSerializer
#
# class MouseClickEventViewSet(CreateListRetrieveViewSet):
#     queryset = MouseClickEvent.objects.all()
#     serializer_class = MouseClickEventSerializer
#
# class MouseScrollEventViewSet(CreateListRetrieveViewSet):
#     queryset = MouseScrollEvent.objects.all()
#     serializer_class = MouseScrollEventSerializer
#
# class WindowResolutionEventViewSet(CreateListRetrieveViewSet):
#     queryset = WindowResolutionEvent.objects.all()
#     serializer_class = WindowResolutionEventSerializer
