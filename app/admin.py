from django.contrib import admin
from .models import Schedule, Admin, Faculty, Student, Subject

admin.site.register(Schedule)
admin.site.register(Admin)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Subject)

