from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Blog, BlogAdmin)
admin.site.register(Topic, TopicAdmin)
