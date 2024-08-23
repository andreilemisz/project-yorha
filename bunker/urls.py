from django.urls import include, path
from . import views as bunker_views

from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path("", bunker_views.bunker_startingpage, name="bunker_startingpage"),
    path("contact_log/", include("contact_log.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)