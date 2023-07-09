from django.db import models
from core.abstract.models import AbstractManager, AbstractModel


class PostManager(AbstractManager):
    pass


class Post(AbstractModel):
    author = models.ForeignKey(to="core_user.User", on_delete=models.CASCADE)
    text = models.TextField()
    edited = models.BooleanField(default=False)

    object = PostManager()

    def __str__(self):
        return self.author.name
