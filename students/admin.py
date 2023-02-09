from django.contrib import admin

from students.models import Student, StudentsBase


admin.site.register(StudentsBase)
admin.site.register(Student)