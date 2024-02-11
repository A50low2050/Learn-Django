from django.http import HttpResponse
from django.shortcuts import render


def learn_model(request):
    return HttpResponse(request, "test_model")
