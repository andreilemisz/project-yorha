from django.urls import path
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.conf import settings

from . import views as contact_log_views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", contact_log_views.contact_log_startingpage, name="contact_log_startingpage")
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

