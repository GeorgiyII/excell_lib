from excell_lib.constants import (
    REGULAR_LETTERS as letters,
    get_letter,
)
from excell_lib.column import Column
from excell_lib.cell import Cell
from excell_lib.actions import add_units
from typing import Dict, Type
import copy


class Table:

    def __init__(self, sheet, unit_rows: list = None, row_number: int = None):
        self._columns = {}
        self._sheet = sheet
        self._row_number = sheet.max_row
        self.row_with_params = row_number
        self.unit_rows = unit_rows
        self.setup_table(sheet)

    def __str__(self):
        for column in self.columns:
            print(column)
        return ''

    @property
    def rows_number(self):
        return self._row_number

    @property
    def columns_number(self):
        return len(self._columns)

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

    def get_row_with_parameters(self):
        return self.get_row_values(self.row_with_params)

    @property
    def rows(self):
        rows = self._row_number
        for row in range(1, rows + 1):
            yield self.get_row_values(row)

    def setup_table(self, sheet):
        for column in range(1, sheet.max_column + 1):
            cells = {}
            letter = None
            for row in range(1, sheet.max_row + 1):
                cell = sheet.cell(row, column)
                obj = Cell(cell.coordinate, row, column, cell.value, cell._style)
                cells.update({row: obj})
                letter = letters.sub('', sheet.cell(row, column).coordinate)

            obj = Column(letter, column, cells)
            self._columns.update({column: obj})
        if self.unit_rows:
            self._setup_units_constants()

    def add_pass_column(self, coordinate):
        new_columns = {}
        flag = False
        for key in self._columns:
            column = self._columns[key]
            if column.number == coordinate:
                flag = True
                new_columns.update({key: column})
                pass_column = self._add_pass_column(key)
                new_columns.update(pass_column)
                for copy_column in self._copy_data_right(key + 1):
                    new_columns.update(copy_column)
            if not flag:
                new_columns.update({key: column})

        self._columns = new_columns

    def _setup_units_constants(self):
        for row in self.unit_rows:
            add_units(self.get_row_values(row))

    def _add_pass_column(self, number):
        cells = {}
        for i in range(1, self.rows_number + 1):
            cell = Cell(f'{get_letter(number + 1)}{number + 1}', i, number + 1)
            cells.update({i: cell})
            column = Column(get_letter(number + 1), number + 1, cells)
        return {number + 1: column}

    def add_many_pass_column_right(self, coordinate, number=1):
        for column in range(coordinate, coordinate + number):
            self.add_pass_column(column)

    def _copy_data_right(self, start_column):
        for i in range(start_column, self.columns_number + 1):
            column = self._columns[i]
            column.change_coordinate_right(i + 1)
            yield {i + 1: column}

    def write_table(self, sheet):
        for column in self.columns:
            for cell in column.cells:
                sheet.cell(cell.row_number, cell.column_number).value = cell.value
                sheet.cell(cell.row_number, cell.column_number)._style = cell.style

