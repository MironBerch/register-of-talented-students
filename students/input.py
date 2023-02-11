import openpyxl

from students.services import create_student, search_student, update_student, deduct_students, get_student_class


def import_students(filepath):
    deduct_students()
    workbook = openpyxl.load_workbook(filename=filepath)
    
    sheet = workbook.worksheets[0]

    for row in sheet.iter_rows():
        full_name = str(row[0].value)
        class_digit = str(row[1].value)
        class_letter = str(row[2].value)
        
        school_сlass = class_digit + class_letter

        if search_student(full_name=full_name):
            update_student(
                full_name=full_name,
                school_сlass=get_student_class(school_сlass),
                is_learns=True,
            )
        else:
            create_student(
                full_name=full_name,
                school_сlass=get_student_class(school_сlass),
                is_learns=True,
            )