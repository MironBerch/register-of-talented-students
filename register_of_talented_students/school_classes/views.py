from django.views import View
from django.http import FileResponse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateResponseMixin

from school_classes.services import get_all_classes, get_number_of_school_classes_students
from students.models import Student


class SchoolClassesListView(
    LoginRequiredMixin,
    TemplateResponseMixin,
    View,
):

    template_name = 'school_classes/classes_list.html'

    def get(self, request):
        return self.render_to_response(
            context = {
                'school_classes': get_all_classes(),
                'numbers_of_school_classes': get_number_of_school_classes_students(),
            },
        )