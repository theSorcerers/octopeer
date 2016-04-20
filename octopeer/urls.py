from django.conf.urls import url, include
from core import views
from django.contrib import admin

urlpatterns = [
    url(r'^api/', include('core.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include('rest_framework_docs.urls')),
]
