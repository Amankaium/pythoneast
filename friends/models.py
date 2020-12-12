from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModel


class Invite(BaseModel):
    user_1 = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="friend_1"
    )

    user_2 = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="friend_2"
    )

    is_accepted = models.BooleanField(default=False)