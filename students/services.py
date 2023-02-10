from django.shortcuts import get_object_or_404

from students.models import Student, StudentsBase
from reporting.models import Contest


def get_all_students():
    """return all students"""
    students = Student.objects.all()
    return students


def deduct_students():
    students = Student.objects.all()
    for student in students:
        student.is_learns = False
        student.save()


def get_last_file():
    file = StudentsBase.objects.all().order_by('id')
    return file


def search_student(full_name) -> bool:
    student = Student.objects.filter(full_name=full_name).exists()
    return student


def create_student(full_name, school_parallel, school_сlass, is_learns) -> None:
    Student.objects.create(
        full_name=full_name,
        school_parallel=school_parallel,
        school_сlass=school_сlass,
        is_learns=is_learns,
    )


def update_student(full_name, school_parallel, school_сlass, is_learns) -> None:
    student = Student.objects.get(full_name=full_name)
    student.school_parallel = school_parallel
    student.school_сlass = school_сlass
    student.is_learns = is_learns
    student.save()


def get_learning_students():
    students = Student.objects.filter(
        is_learns=True,
    )
    return students


def get_student_contest_by_id(id):
    student = get_object_or_404(Student, id=id)
    contests = Contest.objects.filter(student=student)
    return contests


def get_student_by_id(id):
    student = get_object_or_404(Student, id=id)
    return student