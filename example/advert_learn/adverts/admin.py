from django.contrib import admin
from .models import (
    Advert,
    Chat,
    User,
    MembershipChat,
)


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "chat"]


class InlineChatAdmin(admin.TabularInline):
    model = MembershipChat
    extra = 1


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    inlines = (InlineChatAdmin,)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username"]
