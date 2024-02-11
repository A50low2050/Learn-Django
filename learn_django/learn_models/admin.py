from django.contrib import admin
from .models import (
    Person,
    Car,
    Manufacturer,
    Album,
    Artist,
    Song,
)


@admin.register(Person)
class AdminPerson(admin.ModelAdmin):
    list_display = ["first_name", "last_name"]


@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    pass


@admin.register(Manufacturer)
class AdminManufacturer(admin.ModelAdmin):
    pass


@admin.register(Album)
class AdminAlbum(admin.ModelAdmin):
    pass


@admin.register(Artist)
class AdminArtist(admin.ModelAdmin):
    pass


@admin.register(Song)
class AdminSong(admin.ModelAdmin):
    pass
