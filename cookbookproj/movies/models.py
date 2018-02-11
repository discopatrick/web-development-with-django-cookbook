from django.db import models

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey, TreeManyToManyField

from cookbookproj.mixins import CreationModificationDateMixin


class Category(MPTTModel, CreationModificationDateMixin):
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            blank=True,
                            null=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['tree_id', 'lft']
        verbose_name_plural = 'categories'


class Movie(CreationModificationDateMixin):
    title = models.CharField(max_length=255)
    categories = TreeManyToManyField(Category)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'movies'
