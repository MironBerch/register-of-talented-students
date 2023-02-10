from django.urls import path

from students.views import ImportStudentsView, StudentDetailView


urlpatterns = [
    path('students/import_students/', ImportStudentsView.as_view(), name='import_students'),
    path('students/<id>/', StudentDetailView.as_view(), name='student_view'),
]