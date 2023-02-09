from students.models import Student, StudentsBase


def get_all_students():
    """return all students"""
    students = Student.objects.all()
    return students


def get_last_file():
    file = StudentsBase.objects.all().order_by('id')
    return file


def search_student(full_name) -> bool:
    student = Student.objects.filter(full_name=full_name).exists()
    return student


def create_student(full_name, school_parallel, school_сlass) -> None:
    Student.objects.create(
        full_name=full_name,
        school_parallel=school_parallel,
        school_сlass=school_сlass,
    )


def update_student(full_name, school_parallel, school_сlass) -> None:
    student = Student.objects.get(full_name=full_name)
    student.school_parallel = school_parallel
    student.school_сlass = school_сlass
    student.save()