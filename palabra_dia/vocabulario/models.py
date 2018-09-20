from django.db import models


class Vocabulario(models.Model):
    palabra = models.CharField(max_length=100, blank=True, default='')
    definicion = models.TextField()
    class Meta:
        ordering = ('palabra',)

