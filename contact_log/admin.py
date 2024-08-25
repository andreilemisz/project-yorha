from django.contrib import admin
from contact_log import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = "name", "rank",
    ordering = "id",
    search_fields = "name", "rank",
    list_per_page = 20
    list_max_show_all = 50
    
@admin.register(models.Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = "name",
    ordering = "id",
    list_per_page = 20
    list_max_show_all = 50


# Register your models here.
