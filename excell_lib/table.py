from excell_lib.actions import add_units
from excell_lib.cell import Cell
from excell_lib.constants import iter_letters
from beautifultable import BeautifulTable


class Table:

    def __init__(self, sheet, unit_rows: list = None, row_number_with_params: int = None):
        self._cells = {}
        self._sheet = sheet
        self.row_with_params = row_number_with_params
        self.unit_rows = unit_rows
        self.setup_table(sheet)

    def __str__(self):
        table = BeautifulTable()
        for row in self.rows:
            table.append_row(row)
        return str(table)

    @property
    def rows_number(self):
        prev_key = None
        count = 0
        for key in sorted(self._cells.keys()):
            if key[0] != prev_key:
                prev_key = key[0]
                count += 1
        return count

    @property
    def columns_number(self):
        prev_key = None
        count = 0
        for key in sorted(self._cells.keys(), key=lambda key: key[1]):
            if key[1] != prev_key:
                prev_key = key[1]
                count += 1
        return count

    def get_row_values(self, row_number):
        row = []
        for cell in self._cells:
            if cell[0] == row_number:
                row.append(self._cells[cell].value)
        return row

    def get_row_with_parameters(self):
        return self.get_row_values(self.row_with_params)

    def get_column(self, column_number):
        column = []
        for cell in self._cells:
            if cell[1] == column_number:
                column.append(self._cells[cell].value)
        return column

    @property
    def rows(self):
        for row in range(1, self.rows_number + 1):
            yield self.get_row_values(row)

    def setup_table(self, sheet):
        for column in range(1, sheet.max_column + 1):
            for row in range(1, sheet.max_row + 1):
                cell = sheet.cell(row, column)
                obj = Cell(row, column, cell.value, cell._style)
                self._cells.update({(row, column): obj})

        if self.unit_rows:
            self._setup_units_constants()

    def add_multiple_columns(self, column, columns_value):
        columns_number = len(columns_value)
        for number in range(columns_number):
            column_coordinate = column + number
            data = columns_value[number]
            self.add_column(column_coordinate, data)

    def add_column(self, column, column_values=()):
        new_table = {}
        if column > self.columns_number:
            new_table.update(self._add_column_in_the_end(column, column_values))
        else:
            for key in self._cells:
                if key[1] < column:
                    new_table.update({key: self._cells[key]})
                elif key[1] == column:
                    cell = self._copy_cell_to_next_column(key)
                    value = ""
                    if column_values:
                        value = column_values[key[0] - 1]
                    new_cell = Cell(key[0], key[1], value=value, style=cell._style)
                    new_table.update({key: new_cell})
                    new_table.update({(cell.row_number, cell.column_number): cell})
                else:
                    cell = self._copy_cell_to_next_column(key)
                    new_table.update({(cell.row_number, cell.column_number): cell})

        self._cells.update(new_table)

    def _add_column_in_the_end(self, column, column_values=()):
        new_column = {}
        for row in range(1, self.rows_number + 1):
            cell = self._cells[(row, column - 1)]
            value = ""
            if column_values:
                value = column_values[row - 1]
            new_cell = Cell(row, column, value=value, style=cell._style)
            new_column.update({(row, column): new_cell})
        return new_column

    def _copy_cell_to_next_column(self, coordinate):
        cell = self._cells[coordinate]
        cell.change_formulas_cells()
        cell.change_coordinate()
        return cell

    def _setup_units_constants(self):
        for row in self.unit_rows:
            add_units(self.get_row_values(row))

    def write_table(self, sheet):
        for cell in self._cells:
            cell = self._cells[cell]
            sheet.cell(cell.row_number, cell.column_number).value = cell.value
            sheet.cell(cell.row_number, cell.column_number)._style = cell.style

    @staticmethod
    def _count_letter_number(letter: str):
        count = 0
        for item in iter_letters():
            count += 1
            if item == letter:
                return count