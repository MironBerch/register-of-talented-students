from django.test import SimpleTestCase
from django.urls import resolve, reverse

from accounts.views import SigninView, SignoutView, SignupView


class TestUserUrls(SimpleTestCase):

    def test_signup_view_is_resolved(self):
        url = reverse('signup')
        self.assertEquals(
            resolve(url).func.view_class, SignupView,
        )

    def test_signin_view_is_resolved(self):
        url = reverse('signin')
        self.assertEquals(
            resolve(url).func.view_class, SigninView,
        )

    def test_signout_view_is_resolved(self):
        url = reverse('signout')
        self.assertEquals(
            resolve(url).func.view_class, SignoutView,
        )
