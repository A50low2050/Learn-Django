from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table = "person"


class Car(models.Model):
    name = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(
        "Manufacturer",
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        db_table = "car"


class Manufacturer(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = "manufacturer"

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = "artist"

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    class Meta:
        db_table = "album"


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)

    class Meta:
        db_table = "song"


class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        db_table = "publication"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication, through="Membership")

    class Meta:
        db_table = "article"
        ordering = ["headline"]

    def __str__(self):
        return self.headline


class Membership(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date_pub = models.DateField()
