from django.db import models
from django.shortcuts import reverse

class Card(models.Model):
    title = models.CharField(max_length=50, unique=True)
    body = models.CharField(max_length=250)
    slug = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=50)
    picture = models.CharField(max_length=150)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug': self.slug})
