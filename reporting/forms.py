from django import forms

from reporting.models import Contest
from students.models import Student
from students.services import get_learning_students


class ContestForm(forms.ModelForm):
    PARALLEL_CHOICES = (
        ('---------', '---------'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
    )
    CLASS_CHOICES = (
        ('---------', '---------'),
        ('а', 'а'),
        ('б', 'б'),
        ('в', 'в'),
    )
    school_parallel = forms.ChoiceField(
        widget=forms.Select,
        choices=PARALLEL_CHOICES,
    )
    school_сlass = forms.ChoiceField(
        widget=forms.Select,
        choices=CLASS_CHOICES,
    )
    event_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
            }
        ),
    )
    student = forms.ModelChoiceField(
            queryset=get_learning_students(),
        )
    class Meta:
        model = Contest
        fields = ('event_date', 'title', 'student', 'other', 'teachers_name', 'stage', 'direction', 'subject', 'result', 'scan_diploma',)
        widgets = {
            'scan_diploma': forms.FileInput(
                attrs={
                    'id': 'formFile',
                    'type': 'file',
                }
            ),
        }     