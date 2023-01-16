from openpyxl import Workbook

wb = Workbook()

ws = wb.active

def export_contest_to_excel(contests) -> None:
    print(contests)
    for contest in contests:
        print(contest.title)