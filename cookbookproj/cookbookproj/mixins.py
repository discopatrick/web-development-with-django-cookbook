from django.db import models
from django.utils import timezone


class CreationModificationDateMixin(models.Model):

    class Meta:
        abstract = True

    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created = timezone.now()
        else:
            self.modified = timezone.now()

        super(CreationModificationDateMixin, self).save(*args, **kwargs)
