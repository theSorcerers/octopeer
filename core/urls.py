from django.conf.urls import url, include
from core import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'pull-requests', views.PullRequestViewSet)
router.register(r'sessions', views.SessionViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'event-positions', views.EventPositionViewSet)
router.register(r'event-types', views.EventTypeViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
