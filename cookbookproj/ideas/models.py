from django.db import models

from .mixins import CreationModificationDateMixin


class Idea(CreationModificationDateMixin, models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
