from django.test import SimpleTestCase
from reporting.forms import ContestForm


class TestForms(SimpleTestCase):

    def test_contest_form_valid_data(self):
        form = ContestForm(
            data={
                'title': 'ВСОШ',
                'students_name': 'Ф И О',
                'other': '',
                'teachers_name': 'Ф И О',
                'stage': 'Школьный',
                'direction': 'Образование',
                'subject': 'Русский язык',
                'school_сlass': 'а',
                'result': '1 место',
                'school_parallel': '1' ,
                'event_date': '13.12.2023',
            }
        )

        self.assertTrue(form.is_valid())


    def test_contest_form_valid_no_data(self):
        form = ContestForm(data={})

        self.assertFalse(form.is_valid())