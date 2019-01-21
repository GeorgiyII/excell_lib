import copy

from excell_lib.filters import (
    unmerge_filter,
    not_formula,
)
from excell_lib.parsers import (
    change_formula_cells,
    get_number,
)


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