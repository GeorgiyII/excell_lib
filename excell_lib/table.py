from excell_lib.constants import REGULAR_LETTERS as letters
from excell_lib.column import Column
from excell_lib.cell import Cell
from typing import Dict, Optional, Type


# class Table:
#
#     table_data = {}
#     buffer_column = []
#     column_names = {}
#     column_numbers = {}
#
#     def __init__(self, sheet):
#         self.sheet = sheet
#         self.max_column = sheet.max_column
#         self.max_row = sheet.max_row
#         self._load_table()
#         self._get_column_names()
#         self._get_column_numbers()
#
#     def __str__(self):
#         return str(self.table_data)
#
#     def __getitem__(self, key):
#         return self.table_data[key]
#
#     def __setitem__(self, key, value):
#         self.table_data.update({key: value})
#
#     def _load_table(self):
#         for column in range(1, self.max_column + 1):
#             for row in range(1, self.max_row + 1):
#                 cell = {self.sheet.cell(row, column).coordinate: self.sheet.cell(row, column).value}
#                 self.table_data.update(cell)
#
#     def _get_column_names(self):
#         self.column_names = {}
#         name = ''
#         number = 1
#         for item in self.table_data:
#             column_letter = REGULAR_LETTERS.sub('', item)
#             if not name:
#                 name = column_letter
#                 self.column_names.update({column_letter: number})
#                 number += 1
#             if name != column_letter:
#                 name = column_letter
#                 self.column_names.update({column_letter: number})
#                 number += 1
#
#     def _get_column_numbers(self):
#         self.column_numbers = {}
#         name = ''
#         number = 1
#         for item in self.table_data:
#             column_letter = REGULAR_LETTERS.sub('', item)
#             if not name:
#                 name = column_letter
#                 self.column_numbers.update({number: column_letter})
#                 number += 1
#             if name != column_letter:
#                 name = column_letter
#                 self.column_numbers.update({number: column_letter})
#                 number += 1
#
#     def get_column_data(self, coordinate):
#         self.buffer_column = []
#         coordinate_letter = REGULAR_LETTERS.sub('', coordinate)
#         self.buffer_column.append(coordinate_letter)
#         for item in self.table_data:
#             column_letter = REGULAR_LETTERS.sub('', item)
#             if column_letter == coordinate_letter:
#                 self.buffer_column.append(self.table_data[item])
#         return self.buffer_column
#
#     def get_all_columns_data_right(self, coordinate):
#         column_letter = REGULAR_LETTERS.sub('', coordinate)
#         column_number = self.column_names[column_letter]
#         for column in range(column_number, self.max_column + 1):
#             letter = self.column_numbers[column]
#             yield self.get_column_data(letter)
#
#     def get_all_columns_data_left(self, coordinate):
#         column_letter = REGULAR_LETTERS.sub('', coordinate)
#         column_number = self.column_names[column_letter]
#         for column in range(1, column_number + 1):
#             letter = self.column_numbers[column]
#             yield self.get_column_data(letter)


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

    def add_pass_column(self, coordinate):
        pass



