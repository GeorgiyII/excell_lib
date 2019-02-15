from excell_lib.filters import (
    unmerge_filter,
)
from excell_lib.constants import UNITS


def add_units(values: list):
    for value in values:
        UNITS.append(value)


def merge(sheet, rows):
    start_column = None
    finish_column = None
    flag = False
    for row in rows:
        for column in range(5, sheet.max_column + 1):
            value = sheet.cell(row, column).value
            if value:
                if flag:
                    flag = False
                    sheet.merge_cells(
                        f'{sheet.cell(row, start_column).coordinate}:{sheet.cell(row, finish_column).coordinate}')
                    finish_column = None
                start_column = column
            else:
                flag = True
                finish_column = column
        sheet.merge_cells(
            f'{sheet.cell(row, start_column).coordinate}:{sheet.cell(row, finish_column).coordinate}')


def unmerge(sheet):
    sheet_ranges = sheet.merged_cells.ranges
    for i in sheet_ranges[1:]:
        if unmerge_filter(str(i)):
            sheet.unmerge_cells(str(i))


