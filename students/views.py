from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from reporting.export import export_contest_to_excel
import os
from reporting.services import get_all_contests, get_users_creation_contests, get_contest
from django.http import FileResponse
from django.views import View
from django.views.generic.base import TemplateResponseMixin
from students.models import Student
from users.mixins import SuperUserRequiredMixin
from students.forms import StudentsImportForm


class ImportStudentsView(
    SuperUserRequiredMixin,
    View,
):

    template_name = 'students/import_student.html'
    form_class = StudentsImportForm

    def get(self, request):
        return self.render_to_response(
            context = {
                'form': self.form_class(),
            },
        )