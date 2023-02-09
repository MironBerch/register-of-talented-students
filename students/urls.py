from django.urls import path

from students.views import ImportStudentsView


urlpatterns = [
    path('import_students/', ImportStudentsView.as_view(), name='import_students'),
]