from excell_lib.constants import (
    REGULAR_LETTERS as letters
)
from excell_lib.column import Column
from excell_lib.cell import Cell
from excell_lib.actions import add_units
from typing import Dict, Type
import copy


class Table:

    _columns: Dict[int, Type[Column]] = {}

    def __init__(self, unit_rows: list):
        self.unit_rows = unit_rows

    def __str__(self):
        for column in self.columns:
            print(column)
        return ''

    @property
    def columns(self):
        for column in self._columns:
            yield self._columns[column]

    def get_row_values(self, row_number):
        row = []
        for column in self.columns:
            for cell in column.cells:
                if cell.row_number == row_number:
                    row.append(cell.value)
        return row

    def setup_table(self, sheet):
        for column in range(1, sheet.max_column + 1):
            cells = {}
            letter = None
            for row in range(1, sheet.max_row + 1):
                cell = sheet.cell(row, column)
                obj = Cell(cell, row, column)
                cells.update({row: obj})
                letter = letters.sub('', sheet.cell(row, column).coordinate)

            obj = Column(letter, column, cells)
            self._columns.update({column: obj})
        self._setup_units_constants()

    def _add_pass_column(self, coordinate):
        new_columns = {}
        flag = False
        for column in self._columns:
            if coordinate == column:
                flag = True
                pass_column = copy.deepcopy(self._columns[column])
                pass_column.clear_cells()
                new_columns.update({column: pass_column})
            if flag:
                key = column + 1
                moved_column = copy.deepcopy(self._columns[column])
                moved_column.change_coordinate_right(key)
                new_column = {key: moved_column}
            else:
                new_column = {column: self._columns[column]}

            new_columns.update(new_column)
        self._columns = new_columns

    def _setup_units_constants(self):
        for row in self.unit_rows:
            add_units(self.get_row_values(row))

    def add_many_pass_column_right(self, coordinate, number=1):
        for column in range(coordinate, coordinate + number):
            self._add_pass_column(column)

    def write_table(self, sheet):
        for column in self.columns:
            for cell in column.cells:
                sheet.cell(cell.row_number, cell.column_number).value = cell.value
                sheet.cell(cell.row_number, cell.column_number)._style = cell.style

