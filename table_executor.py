import openpyxl

from excell_lib.table import Table
from excell_lib.actions import (
    merge,
    unmerge,
)

from data_master import get_materials_data, get_next_abbreviation_pack


def add_column_with_prices(table, table_prices, symbol):
    rows_number = table.rows_number
    new_table = table
    index = True
    while index:
        materials_row = new_table.get_row_with_parameters()
        table_prices_abbreviation = table_prices.get_column(1)
        materials, column_number, index = get_next_abbreviation_pack(index, materials_row, table_prices_abbreviation, symbol)
        index = index
        if materials and column_number:
            materials_data = get_materials_data(materials, table_prices, rows_number, column_number)
            new_table.add_multiple_columns(column_number + 2, materials_data)

    return new_table


def copy_worksheet(book):
    if book.get_sheet_by_name('innervagg Copy'):
        sheet = book.get_sheet_by_name('innervagg Copy')
        book.remove(sheet)
    sheet = book.get_sheet_by_name('innervagg')
    book.copy_worksheet(sheet)
    sheet = book.get_sheet_by_name('innervagg Copy')
    return sheet


def start(file_name):
    book = openpyxl.load_workbook(file_name)
    sheet = copy_worksheet(book)
    unmerge(sheet)
    sheet_prices = book.get_sheet_by_name('model')
    table = Table(sheet, [1, 2, 3], 2)
    table_prices = Table(sheet=sheet_prices)
    symbol = ';'
    new_table = add_column_with_prices(table, table_prices, symbol)
    new_table.write_table(sheet)
    merge(sheet, [1, 2])

    book.save(file_name)
