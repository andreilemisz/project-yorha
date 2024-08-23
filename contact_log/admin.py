from django.contrib import admin
from contact_log import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = "name", "position",
    ordering = "id",
    search_fields = "name", "position",
    list_per_page = 20
    list_max_show_all = 50


# Register your models here.
