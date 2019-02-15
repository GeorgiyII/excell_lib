def add_column_with_prices(table, table_prices, symbol, coeff_coordinate, coeff_number):
    # table.add_many_pass_column_right(coeff_coordinate, coeff_number)
    materials_row = table.get_row_with_parameters()
    materials = _get_next_materials(materials_row, symbol)
    materials_data = _get_materials_data(materials, table_prices)
    new_table = add_column_for_new_material(table, materials_data)
    return new_table


def add_column_for_new_material(table, materials: dict):
    offset = 0
    for column in materials.keys():
        for add in materials[column]:
            coordinate = column - 1 + add + offset
            table.add_many_pass_column_right(coordinate)

        offset += len(materials[column])
    return table


def add_column_with_material():
    pass


def add_material_name(table, name):
    pass


def add_formula_material_pricing(table, price):
    pass


def _get_next_materials(materials_row, symbol: str):
    materials_cyphers = {}
    for index, cell in enumerate(materials_row):
        if cell:
            materials_cyphers.update({index + 1: cell.split(f'{symbol}')})
    return materials_cyphers


def _get_materials_data(materials: dict, table_prices):
    materials_full = materials
    for key in materials.keys():
        materials_data = {}
        for index, cypher in enumerate(materials[key]):
            for row in table_prices.rows:
                if cypher.strip() in row:
                    materials_data.update({index + 2: {'name': row[1], 'price': row[2]}})
        materials_full[key] = materials_data
    return materials_full
