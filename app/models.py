from email.policy import default
from operator import mod
from turtle import title
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL #auth.User


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.title
