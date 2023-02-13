from django.db import models
from datetime import datetime


class AboutMe(models.Model):
    description = models.TextField()

    class Meta:
        verbose_name = 'o mnie'
        verbose_name_plural = 'o mnie'

    def __str__(self):
        return 'O mnie'


class ServiceDescription(models.Model):
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'opis usług'

    def __str__(self):
        return self.description


class Service(models.Model):
    service_type = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'usługa'
        verbose_name_plural = 'usługi'

    def __str__(self):
        return self.service_type


class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'kategoria'
        verbose_name_plural = 'kategorie'

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True)

    class Meta:
        verbose_name = 'zdjęcia'
        verbose_name_plural = 'galeria zdjęć'

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    facebook = models.URLField()
    fixly = models.URLField()

    class Meta:
        verbose_name = 'kontakt'
        verbose_name_plural = 'dane kontaktowe'

    def __str__(self):
        return self.name
