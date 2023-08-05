from django.urls import path

from accounts.views import SigninView, SignoutView, SignupView

urlpatterns = [
    path(
        route='signup/',
        view=SignupView.as_view(),
        name='signup',
    ),
    path(
        route='signin/',
        view=SigninView.as_view(),
        name='signin',
    ),
    path(
        route='signout/',
        view=SignoutView.as_view(),
        name='signout',
    ),
]
