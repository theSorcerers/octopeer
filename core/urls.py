from django.conf.urls import url, include
from core import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'sessions', views.SessionViewSet)
router.register(r'keystroke-events', views.KeystrokeEventViewSet)
router.register(r'text-selection-events', views.TextSelectionEventViewSet)
router.register(r'mouse-hover-events', views.MouseHoverEventViewSet)
router.register(r'mouse-movement-events', views.MouseMovementEventViewSet)
router.register(r'mouse-click-events', views.MouseClickEventViewSet)
router.register(r'mouse-scroll-events', views.MouseScrollEventViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
