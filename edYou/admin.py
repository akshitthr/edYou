from django.contrib import admin

from .models import User, Course, Chapter, Video, Enrolled, Notes

# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Chapter)
admin.site.register(Video)
admin.site.register(Enrolled)
admin.site.register(Notes)
