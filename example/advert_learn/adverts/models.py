from django.db import models


class Advert(models.Model):
    title = models.CharField("Название", max_length=40)
    chat = models.ForeignKey("Chat", models.CASCADE, null=True)

    class Meta:
        db_table = "advert"

    def __str__(self):
        return self.title


class Chat(models.Model):
    name = models.CharField("Название чата", max_length=40)

    class Meta:
        db_table = "chat"

    def __str__(self):
        return self.name

