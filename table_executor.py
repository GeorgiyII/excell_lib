import openpyxl

from excell_lib.table import Table
from excell_lib.actions import (
    merge,
    unmerge,
)

from data_master import get_materials_abbreviation, get_materials_data


def add_column_with_prices(table, table_prices, symbol):
    rows_number = table.rows_number
    materials_row = table.get_row_with_parameters()
    materials = get_materials_abbreviation(materials_row, symbol)
    materials_data = get_materials_data(materials, table_prices, rows_number)
    new_table = add_column_for_new_material(table, materials_data)
    return new_table


def add_column_for_new_material(table, materials: dict):
    offset = 0
    for column in materials.keys():
        for add in materials[column]:
            coordinate = column + add + offset
            table.add_column(coordinate, materials[column][add])

        offset += len(materials[column])
    return table


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
