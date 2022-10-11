from django.contrib import admin
from .models import MainInfo, Project, Resume

# Register your models here.
admin.site.register(MainInfo)
admin.site.register(Project)
admin.site.register(Resume)