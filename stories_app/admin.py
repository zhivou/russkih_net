from django.contrib import admin
from .models import Story, News, NewsImgs
# Register your models here.
admin.site.register(Story)
admin.site.register(News)
admin.site.register(NewsImgs)
