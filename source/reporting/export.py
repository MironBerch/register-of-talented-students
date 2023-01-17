from openpyxl import Workbook


def export_contest_to_excel(contests) -> None:
    contests = contests.order_by('creation_date')
    print(contests)
    for contest in contests:
        print(contest.title)
        print(type(str(contest.creation_date)))

    wb = Workbook()

    ws = wb.active

    ws.title = "2023"

    ws['A1'] = 'Название мероприятия'
    ws['B1'] = 'ФИО ученика'
    ws['C1'] = 'ФИО преподавателя'
    ws['D1'] = 'Предмет'
    ws['E1'] = 'Класс'
    ws['F1'] = 'Направление'
    ws['G1'] = 'Этап'
    ws['H1'] = 'Результат'
    ws['I1'] = 'Комментарий'
    ws['J1'] = 'Дата мероприятия'
    ws['K1'] = 'Дата Учёта'

    for contest in contests:
        letter_string = 'ABCDEFGHIJK'
        index = 1
        letter = letter_string
        print(contest.title)
        print(type(str(contest.creation_date)))

    wb.save('учёт.xlsx')

#docs
#https://openpyxl.readthedocs.io/en/stable/usage.html
#https://openpyxl.readthedocs.io/en/stable/tutorial.html