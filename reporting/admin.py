from django.contrib import admin

from reporting.models import Contest


@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date', 'modified_date')
    list_display = (
        'contest_creater',
        'title',
        'student',
        'teachers_name',
        'stage',
        'direction',
        'subject',
        'result',
        'creation_date',
    )
    list_filter = (
        'stage',
        'direction',
        'subject',
        'result',
    )
    search_fields = (
        'teachers_name',
        'title',
        'student',
        'contest_creater',
    )