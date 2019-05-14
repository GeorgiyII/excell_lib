from excell_lib.constants import get_letter
from constants import EURO, FORMULA_PREFIX


def get_materials_abbreviation(materials_row, symbol: str):
    materials_cyphers = {}
    for index, cell in enumerate(materials_row):
        if cell:
            materials = cell.split(f'{symbol}')
            column = index + 1
            materials_cyphers.update({column: materials})
    return materials_cyphers


def get_materials_data(materials: dict, material_prices, rows_number):
    materials_full = materials
    for key in materials.keys():
        materials_data = {}
        for index, cypher in enumerate(materials[key]):
            for row in material_prices.rows:
                if cypher.strip() in row:
                    column_data = _get_column_data(column=key, name=row[1], price=row[2], rows_number=rows_number)
                    materials_data.update({index + 2: column_data})
        materials_full[key] = materials_data
    return materials_full


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
