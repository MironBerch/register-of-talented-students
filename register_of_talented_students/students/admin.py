from django.contrib import admin

from students.models import Student, StudentsBase, Class


@admin.register(Student)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'school_сlass',
        'is_learns',
    )
    list_filter = (
        'school_сlass',
        'is_learns',
    )
    search_fields = (
        'full_name',
        'school_сlass',
    )


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = (
        'school_class',
    )


admin.site.register(StudentsBase)