
def get_materials_abbreviation(materials_row, symbol: str):
    materials_cyphers = {}
    for index, cell in enumerate(materials_row):
        if cell:
            materials_cyphers.update({(index + 1, index + 2): cell.split(f'{symbol}')})
    return materials_cyphers


def get_materials_data(materials: dict, material_prices):
    materials_full = materials
    for key in materials.keys():
        materials_data = {}
        for index, cypher in enumerate(materials[key]):
            for row in material_prices:
                if cypher.strip() in row:
                    materials_data.update({index + 2: {'name': row[1], 'price': row[2]}})
        materials_full[key] = materials_data
    return materials_full


def _column_with_material():
    pass


def _material_name(table, name):
    pass


def _formula_material_pricing(table, price):
    pass
