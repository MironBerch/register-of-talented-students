from django.contrib import admin

from reporting.models import Contest


class ContestAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date', 'modified_date')


admin.site.register(Contest, ContestAdmin)