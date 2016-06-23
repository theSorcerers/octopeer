from django.conf.urls import url
from core import views


urlpatterns = [
    url(r'^$', views.api_root),

    url(r'^change-tab-events/$', views.ChangeTabEventList.as_view(), name='change-tab-event-list'),
    url(r'^change-tab-events/(?P<pk>[0-9]+)/$', views.ChangeTabEventDetail.as_view(), name='change-tab-event-detail'),
    url(r'^change-tab-events/(?P<username>.+)/$', views.ChangeTabEventUserList.as_view(), name='change-tab-event-user-list'),

    url(r'^element-types/$', views.ElementTypeList.as_view(), name='element-type-list'),
    url(r'^element-types/(?P<pk>[0-9]+)/$', views.ElementTypeDetail.as_view(), name='element-type-detail'),

    url(r'^event-types/$', views.EventTypeList.as_view(), name='event-type-list'),
    url(r'^event-types/(?P<pk>[0-9]+)/$', views.EventTypeDetail.as_view(), name='event-type-detail'),

    url(r'^file-positions/$', views.FilePositionList.as_view(), name='file-position-list'),
    url(r'^file-positions/(?P<pk>[0-9]+)/$', views.FilePositionDetail.as_view(), name='file-position-detail'),

    url(r'^html-pages/$', views.HTMLPageList.as_view(), name='html-page-list'),
    url(r'^html-pages/(?P<pk>[0-9]+)/$', views.HTMLPageDetail.as_view(), name='html-page-detail'),
    url(r'^html-pages/(?P<username>.+)/$', views.HTMLPageUserList.as_view(), name='html-page-user-list'),

    url(r'^keystroke-events/$', views.KeystrokeEventList.as_view(), name='keystroke-event-list'),
    url(r'^keystroke-events/(?P<pk>[0-9]+)/$', views.KeystrokeEventDetail.as_view(), name='keystroke-event-detail'),
    url(r'^keystroke-events/(?P<username>.+)/$', views.KeystrokeEventUserList.as_view(), name='keystroke-user-list'),

    url(r'^keystroke-types/$', views.KeystrokeTypeList.as_view(), name='keystroke-type-list'),
    url(r'^keystroke-types/(?P<pk>[0-9]+)/$', views.KeystrokeTypeDetail.as_view(), name='keystroke-type-detail'),

    url(r'^mouse-click-events/$', views.MouseClickEventList.as_view(), name='mouse-click-event-list'),
    url(r'^mouse-click-events/(?P<pk>[0-9]+)/$', views.MouseClickEventDetail.as_view(), name='mouse-click-event-detail'),
    url(r'^mouse-click-events/(?P<username>.+)/$', views.MouseClickEventUserList.as_view(), name='mouse-click-event-user-list'),

    url(r'^mouse-position-events/$', views.MousePositionEventList.as_view(), name='mouse-position-event-list'),
    url(r'^mouse-position-events/(?P<pk>[0-9]+)/$', views.MousePositionEventDetail.as_view(), name='mouse-position-event-detail'),
    url(r'^mouse-position-events/(?P<username>.+)/$', views.MousePositionEventUserList.as_view(), name='mouse-position-event-user-list'),

    url(r'^mouse-scroll-events/$', views.MouseScrollEventList.as_view(), name='mouse-scroll-event-list'),
    url(r'^mouse-scroll-events/(?P<pk>[0-9]+)/$', views.MouseScrollEventDetail.as_view(), name='mouse-scroll-event-detail'),
    url(r'^mouse-scroll-events/(?P<username>.+)/$', views.MouseScrollEventUserList.as_view(), name='mouse-scroll-event-user-list'),

    url(r'^pull-requests/$', views.PullRequestList.as_view(), name='pull-request-list'),
    url(r'^pull-requests/(?P<owner>.+)/(?P<name>.+)/(?P<pull_request_number>[0-9]+)/$', views.PullRequestDetail.as_view(), name='pull-request-detail'),

    url(r'^repositories/$', views.RepositoryList.as_view(), name='repository-list'),
    url(r'^repositories/(?P<owner>.+)/(?P<name>.+)/$', views.RepositoryDetail.as_view(), name='repository-detail'),

    url(r'^semantic-events/$', views.SemanticEventList.as_view(), name='semantic-event-list'),
    url(r'^semantic-events/(?P<pk>[0-9]+)/$', views.SemanticEventDetail.as_view(), name='semantic-event-detail'),
    url(r'^semantic-events/(?P<username>.+)/(?P<owner>.+)/(?P<name>.+)/(?P<pull_request_number>[0-9]+)/$', views.SemanticEventSessionList.as_view(), name='semantic-event-session-list'),
    url(r'^semantic-events/(?P<username>.+)/$', views.SemanticEventUserList.as_view(), name='semantic-event-user-list'),

    url(r'^sessions/$', views.SessionList.as_view(), name='session-list'),
    url(r'^sessions/(?P<username>.+)/(?P<owner>.+)/(?P<name>.+)/(?P<pull_request_number>[0-9]+)/$', views.SessionDetail.as_view(), name='session-detail'),
    url(r'^sessions/(?P<pk>[0-9]+)/$', views.SessionDetail.as_view(), name='session-pk-detail'),
    url(r'^sessions/(?P<username>.+)/$', views.SessionUserList.as_view(), name='session-user-list'),

    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<username>.+)/$', views.UserDetail.as_view(), name='user-detail'),

    url(r'^window-resolution-events/$', views.WindowResolutionEventList.as_view(), name='window-resolution-event-list'),
    url(r'^window-resolution-events/(?P<pk>[0-9]+)/$', views.WindowResolutionEventDetail.as_view(), name='window-resolution-event-detail'),
    url(r'^window-resolution-events/(?P<username>.+)/$', views.WindowResolutionEventUserList.as_view(), name='window-resolution-event-user-list'),
]
