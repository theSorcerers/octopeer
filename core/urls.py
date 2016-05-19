from django.conf.urls import url, include
from core import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^repositories/$', views.RepositoryList.as_view(), name='repository-list'),
    url(r'^repositories/(?P<owner>.+)/(?P<name>.+)/$', views.RepositoryDetail.as_view(), name='repository-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<username>.+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^pull-requests/$', views.PullRequestList.as_view(), name='pull-request-list'),
    url(r'^pull-requests/(?P<owner>.+)/(?P<name>.+)/(?P<pull_request_number>[0-9]+)/$', views.PullRequestDetail.as_view(), name='pull-request-detail'),
    url(r'^sessions/$', views.SessionList.as_view(), name='session-list'),
    url(r'^sessions/(?P<username>.+)/(?P<owner>.+)/(?P<name>.+)/(?P<pull_request_number>[0-9]+)/$', views.SessionDetail.as_view(), name='session-detail'),
    url(r'^event-types/$', views.EventTypeList.as_view(), name='event-type-list'),
    url(r'^event-types/(?P<pk>[0-9]+)/$', views.EventTypeDetail.as_view(), name='event-type-detail'),
    url(r'^element-types/$', views.ElementTypeList.as_view(), name='element-type-list'),
    url(r'^element-types/(?P<pk>[0-9]+)/$', views.ElementTypeDetail.as_view(), name='element-type-detail'),
]
