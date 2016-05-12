from django.conf.urls import url, include
from core import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'repositories', views.RepositoryViewSet)
router.register(r'pull-requests', views.PullRequestViewSet)
router.register(r'sessions', views.SessionViewSet)
router.register(r'event-types', views.EventTypeViewSet)
router.register(r'element-types', views.ElementTypeViewSet)
router.register(r'semantic-events', views.SemanticEventViewSet)
router.register(r'event-positions', views.EventPositionViewSet)
router.register(r'keystroke-events', views.KeystrokeEventViewSet)
router.register(r'mouse-position-events', views.MousePositionEventViewSet)
router.register(r'mouse-click-events', views.MouseClickEventViewSet)
router.register(r'mouse-scroll-events', views.MouseScrollEventViewSet)
router.register(r'window-resolution-events', views.WindowResolutionEventViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
