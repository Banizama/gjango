from django.contrib import admin
from .models import Admin, Project, Task
# Register your models here.

admin.site.register(Admin)
admin.site.register(Project)
admin.site.register(Task)

