# Generated by Django 3.2 on 2021-04-23 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Palette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Цвет')),
                ('image', models.ImageField(upload_to='colors/', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Тэг')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_rus', models.CharField(max_length=100, verbose_name='Название')),
                ('title_eng', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('description_rus', models.CharField(max_length=2000, null=True, verbose_name='Описание')),
                ('description_eng', models.CharField(max_length=2000, null=True, verbose_name='Description')),
                ('year', models.PositiveIntegerField(default=2021, verbose_name='Год')),
                ('height', models.PositiveIntegerField(verbose_name='Высота')),
                ('width', models.PositiveIntegerField(verbose_name='Ширина')),
                ('area', models.PositiveIntegerField(verbose_name='Площадь')),
                ('genre', models.ManyToManyField(null=True, to='main.Genre', verbose_name='Жанр')),
                ('palette', models.ManyToManyField(null=True, to='main.Palette', verbose_name='Палитра')),
                ('tags', models.ManyToManyField(null=True, to='main.Tag', verbose_name='Тэги')),
            ],
            options={
                'verbose_name': 'Картина',
                'verbose_name_plural': 'Картины',
            },
        ),
    ]
