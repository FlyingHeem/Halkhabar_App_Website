from django.contrib import admin
from .models import NewsItem, Comment

# Register your models here.

admin.site.register(NewsItem)
admin.site.register(Comment)


'''
class MyModelAdmin(admin.ModelAdmin):
	pass

'''