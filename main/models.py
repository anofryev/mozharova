from django.db import models

# Create your models here.
class Tag(models.Model):
    """Тэги"""
    name = models.CharField("Тэг", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

class Palette(models.Model):
    """Палитра"""
    name = models.CharField("Цвет", max_length=50)
    image = models.ImageField("Картинка", upload_to="colors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"

class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Имя", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Painting(models.Model):
    """Картина"""
    title_rus = models.CharField("Название", max_length=100)
    title_eng = models.CharField("Title", max_length=100, null=True)
    description_rus = models.CharField("Описание", max_length=2000, null=True)
    description_eng = models.CharField("Description", max_length=2000, null=True)
    year = models.PositiveIntegerField("Год", default=2021)
    tags = models.ManyToManyField(Tag, verbose_name="Тэги", null=True)
    palette = models.ManyToManyField(Palette, verbose_name="Палитра", null=True)
    genre = models.ManyToManyField(Genre, verbose_name="Жанр", null=True)
    height = models.PositiveIntegerField("Высота")
    width = models.PositiveIntegerField("Ширина")
    area = models.PositiveIntegerField("Площадь")

    def __str__(self):
        return self.title_rus

    class Meta:
        verbose_name = "Картина"
        verbose_name_plural = "Картины"
