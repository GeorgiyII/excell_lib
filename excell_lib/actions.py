import copy

from excell_lib.filters import (
    unmerge_filter,
    not_formula,
)
from excell_lib.parsers import (
    change_formula_cells,
    get_number,
)


def move_right(column_coordinate, number):
    """
    Moves all data starting from the specified column by the number of columns entered
    :param column_coordinate: starting column
    :param number: the number of columns you need to move
    """
    max_column = sheet.max_column
    max_row = sheet.max_row
    _copy_range_column(column_coordinate, max_column, max_row)
    _clear_range_column(column_coordinate, number)

    for i in range(len(COPY_DATA)):
        coordinate = column_coordinate + number + i
        _paste_range_column(coordinate, i)


def _copy_range_column(start_column, max_column, max_row):
    for column in range(start_column, max_column + 1):
        COPY_DATA.append(column_parser(column, max_row))


def _paste_range_column(column_number, data_numb):
    _paste_column(column_number, COPY_DATA[data_numb])
    book.save('example.xlsx')


def _paste_column(column_coordinate: int, data: list):
    for cell in data:
        sheet.cell(cell.row, column_coordinate).value = cell.value
        sheet.cell(cell.row, column_coordinate)._style = cell._style


def column_parser(column_coordinate, max_row):
    column_data = []
    for row in range(1, max_row + 1):
        copy_sheet = sheet.cell(row, column_coordinate)
        if not not_formula(copy_sheet.value):
            copy_sheet.value = change_formula_cells(copy_sheet.value)
        column_data.append(copy.deepcopy(copy_sheet))
    return column_data


def _clear_range_column(column_coordinate, number):
    for column in range(column_coordinate, column_coordinate + number + 1):
        for row in range(1, sheet.max_row + 1):
            sheet.cell(row, column).value = None


def merge_cells(start, finish):
    sheet.merge_cells(f'{start}:{finish}')


def merge():
    for i in range(5, sheet.max_column + 1):
        for j in range(1, 3):
            value = sheet.cell(j, i).value
            if not value:
                merge_cells(sheet.cell(j, i-1).coordinate, sheet.cell(j, i).coordinate)


def unmerge():
    sheet_ranges = sheet.merged_cells.ranges
    for i in sheet_ranges[1:]:
        if unmerge_filter(str(i)):
            sheet.unmerge_cells(str(i))


def find_args():
    for i in range(5, sheet.max_column + 1):
        if sheet.cell(2, i).value:
            number = get_number(sheet.cell(2, i).value)
            move_right(i + 2, number)