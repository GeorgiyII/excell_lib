from excell_lib.constants import get_letter
from constants import EURO, FORMULA_PREFIX


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
        for row in material_prices.rows:
            if cypher.strip() in row:
                column_data = _get_column_data(column=column_number, name=row[1], price=row[2], rows_number=rows_number)
                materials_data.append(column_data)
    return materials_data


def _get_column_data(column, name, price, rows_number):
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
            data = _formula_material_pricing(row, column, price)
            column_data.append(data)
    return column_data


def _formula_material_pricing(row, column, price):
    cell_with_volume = _cell_cypher_manager(row, column)
    formula = f"{FORMULA_PREFIX}{cell_with_volume}*{price}"
    return formula


def _cell_cypher_manager(row: int, column: int):
    letter = get_letter(column)
    return f"{letter}{row}"
