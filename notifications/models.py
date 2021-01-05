from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModel
from friends.models import Invite


class Notification(BaseModel):
    text = models.TextField(verbose_name="Текст уведомления")
    is_readed = models.BooleanField(default=False, verbose_name="Прочитано ли?")
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="notification",
        verbose_name="Пользователь",
        null=True
    )

    def __str__(self):
        return self.text[:10]


class InviteNotification(Notification):
    invite = models.OneToOneField(
        to=Invite,
        related_name="notification",
        on_delete=models.CASCADE,
        verbose_name="Инвайт"
    )

    
    

