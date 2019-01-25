def get_material_row(table, cypher):
    for row in table.rows:
        if row[0] == cypher:
            data = {'cypher': row[0], 'name': row[1], 'price': row[2]}
            return data


