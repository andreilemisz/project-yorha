from django.urls import path

from . import views as contact_log_views

app_name = "contact_log"

urlpatterns = [
    path('<int:contact_id>/', contact_log_views.contact, name='contact'), 
    path("", contact_log_views.contact_log_startingpage, name="contact_log_startingpage"),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

