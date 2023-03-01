from django.shortcuts import get_object_or_404

from students.models import Student, StudentsBase, Class
from reporting.models import Contest


def get_all_students():
    """return all students"""
    students = Student.objects.all()
    return students


def deduct_students():
    """Deduct all students"""
    students = Student.objects.all()
    for student in students:
        student.is_learns = False
        student.save()


def get_last_file():
    """Get last students excel file"""
    file = StudentsBase.objects.all().order_by('id')
    return file


def search_student(full_name) -> bool:
    """Search student by full name"""
    student = Student.objects.filter(full_name=full_name).exists()
    return student


def create_student(full_name, school_сlass, is_learns) -> None:
    """Create new student"""
    Student.objects.create(
        full_name=full_name,
        school_сlass=school_сlass,
        is_learns=is_learns,
    )


def update_student(full_name, school_сlass, is_learns) -> None:
    """Update student"""
    student = Student.objects.get(full_name=full_name)
    student.school_сlass = school_сlass
    student.is_learns = is_learns
    student.save()


def get_learning_students():
    """Get all learning students"""
    students = Student.objects.filter(
        is_learns=True,
    )
    return students


def get_student_contest_by_id(id):
    """Get student contests"""
    student = get_object_or_404(Student, id=id)
    contests = Contest.objects.filter(student=student)
    return contests


def get_student_by_id(id):
    """Get student by id"""
    student = get_object_or_404(Student, id=id)
    return student


def get_school_class(school_class):
    """Get school class model by school class name"""
    student_class = get_object_or_404(Class, school_class=school_class)
    return student_class


def get_all_classes():
    """Get all classes"""
    school_class = Class.objects.all()
    return school_class


def get_students_by_class(school_class):
    """Get students which learns at class"""
    student_class = get_object_or_404(Class, school_class=school_class)
    students = get_learning_students()
    students = students.filter(school_сlass=student_class)
    return students


def get_student_by_full_name(full_name):
    """Get student by full name"""
    student = Student.objects.get(full_name=full_name)
    return student