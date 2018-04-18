from django.db import models


class Disease(models.Model):
    name = models.CharField(max_length=100)
    doid = models.CharField(max_length=20)
    match_status = models.BooleanField(default=False)

    class Meta:
        ordering = ["-doid"]

    def __str__(self):
        return self.name
