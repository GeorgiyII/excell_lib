from excell_lib.filters import (
    unmerge_filter,
)
from excell_lib.constants import UNITS


def add_units(values: list):
    for value in values:
        UNITS.append(value)
    print(UNITS)


def merge(sheet):
    for i in range(5, sheet.max_column + 1):
        for j in range(1, 3):
            value = sheet.cell(j, i).value
            if not value:
                sheet.merge_cells(f'{sheet.cell(j, i-1).coordinate}:{sheet.cell(j, i).coordinate}')


def unmerge(sheet):
    sheet_ranges = sheet.merged_cells.ranges
    for i in sheet_ranges[1:]:
        if unmerge_filter(str(i)):
            sheet.unmerge_cells(str(i))
