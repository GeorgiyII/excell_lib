import openpyxl

from excell_lib.table import Table
from excell_lib.actions import (
    merge,
    unmerge,
)
from table_logic import add_column_with_prices


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
    unmerge(sheet)
    sheet_prices = book.get_sheet_by_name('model')
    table = Table(sheet, [1, 2, 3], 2)
    table_prices = Table(sheet=sheet_prices)
    symbol = ';'
    new_table = add_column_with_prices(table, table_prices, symbol)
    new_table.write_table(sheet)
    # table.write_table(sheet)
    # merge(sheet)

    book.save('example.xlsx')


main('example.xlsx')
