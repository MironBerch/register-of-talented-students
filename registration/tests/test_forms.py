from django.test import SimpleTestCase
from users.forms import SignupForm, SigninForm


class TestForms(SimpleTestCase):

    def test_signup_form_valid_data(self):
        form = SignupForm(
            data={
                'email': 'user@gmail.com',
                'name': 'name',
                'surname': 'surname',
                'patronymic': 'patronymic',
                'password': 'password',
                'confirm_password': 'confirm_password',
            }
        )

        self.assertTrue(form.is_valid())

    def test_signin_form_valid_data(self):
        form = SigninForm(
            data={
                'email': 'user@gmail.com',
                'password': 'password',
            }
        )

        self.assertTrue(form.is_valid())

    def test_contest_form_valid_no_data(self):
        form = SignupForm(data={})

        self.assertFalse(form.is_valid())

    def test_contest_form_valid_no_data(self):
        form = SigninForm(data={})

        self.assertFalse(form.is_valid())