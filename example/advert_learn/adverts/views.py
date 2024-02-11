
from django.shortcuts import render

from .models import Advert, Chat


def adverts_list(request):
    adverts = Advert.objects.all()
    context = {
        "adverts": adverts,
    }
    return render(request, "adverts.html", context=context)


def adverts_create(request):
    advert = Advert.objects.create(title='Testing Advert')

    context = {

    }
    return render(request, "advert_create.html", context=context)


def chat(request, advert_id):
    advert = Advert.objects.get(pk=advert_id)

    chat = Chat.objects.create(
        name=advert.title,
    )
    chat.save()

    context = {

    }
    return render(request, "chat.html", context=context)
