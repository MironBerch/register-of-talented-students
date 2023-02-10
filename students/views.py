from django.shortcuts import redirect
from django.views import View
from django.views.generic.base import TemplateResponseMixin
from users.mixins import SuperUserRequiredMixin
from students.forms import StudentsImportForm
from students.input import import_students
import os
from django.contrib.auth.mixins import LoginRequiredMixin
from students.services import get_student_contest_by_id, get_student_by_id

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
        
        return self.render_to_response(
            context = {
                'form': self.form_class(),
            },
        )
    

class StudentDetailView(
    LoginRequiredMixin,
    TemplateResponseMixin,
    View,
):
    
    template_name = 'students/detail_student.html'

    def get(self, request, id):
        return self.render_to_response(
            context = {
                'contests': get_student_contest_by_id(id=id),
                'student': get_student_by_id(id=id)
            },
        )