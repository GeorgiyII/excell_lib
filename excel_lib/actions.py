from excel_lib.filters import (
    unmerge_filter,
)


def merge(sheet, coordinates):
    for cells_range in coordinates:
        sheet.merge_cells(
            f'{sheet.cell(cells_range[0][0], cells_range[0][1]).coordinate}:'
            f'{sheet.cell(cells_range[1][0], cells_range[1][1]).coordinate}'
        )


def unmerge(sheet):
    sheet_ranges = sheet.merged_cells.ranges
    for i in sheet_ranges[1:]:
        if unmerge_filter(str(i)):
            sheet.unmerge_cells(str(i))


