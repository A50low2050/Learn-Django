from django.contrib import admin
from .models import Advert, Chat


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ["id", "chat"]


@admin.register(Chat)
class AdvertChat(admin.ModelAdmin):
    list_display = ["id", "name"]
