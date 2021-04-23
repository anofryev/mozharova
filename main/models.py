from django.db import models

# Create your models here.
class Painting(models.Model):
    """Картина"""
    title_rus = models.CharField("Название", max_length=100)
    title_eng = models.Charfield("Title", max_length=100, null=True)
    description_rus = models.CharField("Описание", max_length=2000, null=True)
    description_eng = models.CharField("Description", max_length=2000, null=True)
    year = models.PositiveIntegerField("Год", default=2021)
    tags = models.ManyToManyField()##


class Tags(models.Model):
    pass


class Category(models.Model):
    pass

