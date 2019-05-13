
def get_materials_abbreviation(materials_row, symbol: str):
    materials_cyphers = {}
    for index, cell in enumerate(materials_row):
        if cell:
            materials = cell.split(f'{symbol}')
            column = index + 1
            materials_cyphers.update({column: materials})
    return materials_cyphers


def get_materials_data(materials: dict, material_prices):
    materials_full = materials
    for key in materials.keys():
        materials_data = {}
        for index, cypher in enumerate(materials[key]):
            for row in material_prices.rows:
                if cypher.strip() in row:
                    column_data = _get_column_data(name=row[1], price=row[2])
                    materials_data.update({index + 2: column_data})
        materials_full[key] = materials_data
    return materials_full


def _get_column_data(name, price):
    column_data = []

    return column_data


def _formula_material_pricing(table, price):
    pass
