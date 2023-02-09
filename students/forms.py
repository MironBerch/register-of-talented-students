from django import forms

from students.models import Student


class StudentsImportForm(forms.Form):
    file = forms.FileField()