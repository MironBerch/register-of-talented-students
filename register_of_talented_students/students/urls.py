from django.urls import path

from students.views import ImportStudentsView, StudentDetailView, download_students_import_example


urlpatterns = [
    path('students/import_students/', ImportStudentsView.as_view(), name='import_students'),
    path('students/<id>/', StudentDetailView.as_view(), name='student_view'),
    path('students/import_students/download_file_example/', download_students_import_example, name='download_students_import_example'),
]