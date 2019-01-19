import openpyxl

from excell_lib.table import Table


def copy_worksheet(book):
    if book.get_sheet_by_name('innervagg Copy'):
        sheet = book.get_sheet_by_name('innervagg Copy')
        book.remove(sheet)
    sheet = book.get_sheet_by_name('innervagg')
    book.copy_worksheet(sheet)
    sheet = book.get_sheet_by_name('innervagg Copy')
    return sheet


def main(file_name):
    book = openpyxl.load_workbook(file_name)
    sheet = copy_worksheet(book)
    table = Table()
    table.setup_table(sheet)
    print(table)

    book.save('example.xlsx')


main('example.xlsx')