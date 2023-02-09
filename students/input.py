import openpyxl

from students.services import create_student, search_student, update_student


def import_students(filepath):
    workbook = openpyxl.load_workbook(filename=filepath)
    
    sheet = workbook.worksheets[0]

    for row in sheet.iter_rows():
        full_name = str(row[0].value)
        school_parallel = str(row[1].value)
        school_сlass = str(row[2].value)

        if search_student(full_name=full_name):
            update_student(
                full_name=full_name,
                school_parallel=school_parallel,
                school_сlass=school_сlass,
            )
        else:
            create_student(
                full_name=full_name,
                school_parallel=school_parallel,
                school_сlass=school_сlass,
            )