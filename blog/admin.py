from django.contrib import admin

from .models import Announcement, Blog, Tag

# Register your models here.
admin.site.register(Announcement)
admin.site.register(Blog)
admin.site.register(Tag)