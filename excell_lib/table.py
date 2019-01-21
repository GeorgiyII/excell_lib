from excell_lib.constants import (
    REGULAR_LETTERS as letters
)
from excell_lib.column import Column
from excell_lib.cell import Cell
from typing import Dict, Type
import copy


class Table:

    _columns: Dict[int, Type[Column]] = {}
    _cells: Dict[int, Type[Cell]] = {}

    def __str__(self):
        for column in self._columns:
            print(self._columns[column])
        return ''

    def _move_right_range_right(self, number: int):
        pass

    def setup_table(self, sheet):
        for column in range(1, sheet.max_column + 1):
            cells = {}
            letter = None
            for row in range(1, sheet.max_row + 1):
                cell = sheet.cell(row, column)
                obj = Cell(cell, row, column)
                cells.update({row: obj})
                letter = letters.sub('', sheet.cell(row, column).coordinate)

            self._cells.update(cells)
            obj = Column(letter, column, cells)
            self._columns.update({column: obj})

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

    def add_many_pass_column_right(self, coordinate, number):
        for column in range(coordinate, coordinate + number + 1):
            self._add_pass_column(column)

