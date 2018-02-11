from django.db import models

from .mixins import CreationModificationDateMixin


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Idea(CreationModificationDateMixin, models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.ManyToManyField(Category,
                                        related_name='ideas',
                                        blank=True)

    def __str__(self):
        return self.title
