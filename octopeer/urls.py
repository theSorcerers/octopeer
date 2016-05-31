from django.conf.urls import url, include
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^api/', include('core.urls')),
    url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^$', RedirectView.as_view(url='/api/')),
]
