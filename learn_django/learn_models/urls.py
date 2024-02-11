from django.urls import path
from .views import learn_model

urlpatterns = [
    path("", learn_model)
]
