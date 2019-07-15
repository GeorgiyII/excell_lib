from excel_lib.constants import get_letter
from service_app.constants import EURO, FORMULA_PREFIX, MATERIAL_PRICE_NAME


def get_next_abbreviation_pack(start_index, materials_row, table_prices_abbreviation, symbol):
    for index in range(start_index, len(materials_row)):
        materials_abbreviation = materials_row[index]
        if " " in materials_abbreviation:
            materials = materials_abbreviation.split(f'{symbol} ')
        else:
            materials = materials_abbreviation.split(f'{symbol}')
        if materials and set(materials).issubset(set(table_prices_abbreviation)):
            return materials, index + 1, index + 1
    return None, None, None


def get_materials_data(materials: tuple, material_prices, rows_number, column_number):
    materials_data = []
    for index, cypher in enumerate(materials):
        for row_number, row in enumerate(material_prices.rows):
            if cypher.strip() in row:
                price_cell = f'{get_letter(3)}{row_number + 1}'
                column_data = _get_column_data(
                    column=column_number, name=row[1], price_cell=price_cell, rows_number=rows_number
                )
                materials_data.append(column_data)
    return materials_data


def _get_column_data(column, name, price_cell, rows_number):
    column_data = []
    for row in range(1, rows_number + 1):
        if row < 2:
            data = ""
            column_data.append(data)
        elif row == 2:
            data = name
            column_data.append(data)
        elif row == 3:
            data = EURO
            column_data.append(data)
        else:
            data = _formula_material_pricing(row, column, price_cell)
            column_data.append(data)
    return column_data


def _formula_material_pricing(row, column, price_cell):
    cell_with_volume = _cell_cypher_manager(row, column)
    formula = f"{FORMULA_PREFIX}{cell_with_volume}*{MATERIAL_PRICE_NAME}!{price_cell}"
    return formula


def _cell_cypher_manager(row: int, column: int):
    letter = get_letter(column)
    return f"{letter}{row}"


def get_merge_cells(row_data, row_number):
    merge_cells = []
    start_cell = None
    finish_cell = None
    for index, data in enumerate(row_data):
        if index > 3:
            if data and not start_cell:
                start_cell = (row_number, index + 1)
            elif data and start_cell and not finish_cell:
                finish_cell = (row_number, index)
            if start_cell and finish_cell:
                merge_cells.append((start_cell, finish_cell))
                start_cell = (row_number, index + 1)
                finish_cell = None
    if start_cell and not finish_cell:
        finish_cell = (row_number, len(row_data))
        merge_cells.append((start_cell, finish_cell))
    return merge_cells
