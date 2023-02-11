from django.contrib import admin

from students.models import Student, StudentsBase, Class


admin.site.register(StudentsBase)
admin.site.register(Student)
admin.site.register(Class)