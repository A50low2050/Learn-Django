
from django.shortcuts import render

from .models import Advert, Chat, User


def adverts_list(request):
    adverts = Advert.objects.all()
    context = {
        "adverts": adverts,
    }
    return render(request, "adverts.html", context=context)


def adverts_create(request):
    Advert.objects.get_or_create(title='test advert')
    context = {

    }
    return render(request, "advert_create.html", context=context)


def chat(request, advert_id):
    user = User.objects.get(pk=1)
    advert = Advert.objects.get(pk=advert_id)

    chat, created = Chat.objects.get_or_create(
        name=advert.title,
    )

    chat.members.add(user)
    chat.advert_set.add(advert)

    context = {

    }
    return render(request, "chat.html", context=context)
