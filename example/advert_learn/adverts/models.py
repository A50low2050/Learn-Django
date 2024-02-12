from django.db import models


class User(models.Model):
    username = models.CharField("Логин", max_length=40)

    class Meta:
        db_table = "user"


class Advert(models.Model):
    title = models.CharField("Название", max_length=40)
    chat = models.ForeignKey("Chat", models.CASCADE, null=True)

    class Meta:
        db_table = "advert"

    def __str__(self):
        return self.title


class Chat(models.Model):
    name = models.CharField("Название чата", max_length=40)
    members = models.ManyToManyField(User, through="MembershipChat")

    def __str__(self):
        return self.name


class MembershipChat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
