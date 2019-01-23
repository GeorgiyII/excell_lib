import openpyxl

from excell_lib.table import Table
from excell_lib.actions import (
    merge,
    unmerge,
)


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
    table = Table([1, 2, 3])
    unmerge(sheet)
    table.setup_table(sheet)
    print(table)
    table.add_many_pass_column_right(7, 2)
    print(table.get_row_values(2))
    print(table)
    table.write_table(sheet)
    merge(sheet)

    book.save('example.xlsx')


main('example.xlsx')
