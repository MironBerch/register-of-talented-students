from students.models import Student


def get_all_students():
    """return all students"""
    students = Student.objects.all()
    return students