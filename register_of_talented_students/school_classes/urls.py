from django.urls import path

from school_classes.views import SchoolClassesListView


urlpatterns = [
    path(
        route='school_classes/',
        view=SchoolClassesListView.as_view(),
        name='school_classes',
    ),
]