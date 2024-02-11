from django.urls import path
from .views import adverts_list, adverts_create, chat

urlpatterns = [
    path("", adverts_list, name="show_adverts"),
    path("create/", adverts_create, name="create_advert"),
    path("chat/<int:advert_id>/", chat, name="chat"),
]
