from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateResponseMixin
from students.models import Student, StudentsBase
from users.mixins import SuperUserRequiredMixin
from students.forms import StudentsImportForm
from students.input import import_students
from students.services import get_last_file
import openpyxl
import os


class ImportStudentsView(
    SuperUserRequiredMixin,
    TemplateResponseMixin,
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
    
    def post(self, request):
        form = StudentsImportForm(request.POST or None, files=request.FILES or None)

        if form.is_valid():
            students = form.save()
            filename = students.file.open('r')
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            filepath = BASE_DIR + '/media/' + str(filename)
            import_students(filepath)
            return redirect('list')
        return redirect('import_students')