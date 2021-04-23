from django.contrib import admin
from .models import Painting, Palette, Tag, Genre

# Register your models here.
admin.site.register(Painting)
admin.site.register(Palette)
admin.site.register(Tag)
admin.site.register(Genre)

