from excell_lib.constants import (
    REGULAR_FORMULAS_CELLS,
    REGULAR_LETTERS,
    iter_letters,
    NOT_CHANGED_COLUMNS,
    SUPPORT_LETTERS_NUMBER,
    UNITS
)


class Cell:

    def __init__(self, coordinate, row_number: int, column_number: int, value='', style=''):
        self._cypher = coordinate
        self._coordinate = [row_number, column_number]
        if not value:
            self._data = ''
        else:
            self._data = value
        self._style = style

    def clear(self):
        self._data = ''

    def change_style(self, style):
        self._style = style

    @property
    def value(self):
        if isinstance(self._data, float):
            return str(self._data).replace(".", ",")
        else:
            return self._data

    @property
    def coordinate(self):
        return self._coordinate

    @property
    def cypher(self):
        return self._cypher

    @property
    def row_number(self):
        return self.coordinate[0]

    @property
    def column_number(self):
        return self.coordinate[1]

    @property
    def style(self):
        return self._style

    def change_coordinate(self, letter):
        self._cypher = f'{letter}{self.coordinate[0]}'
        self._coordinate[1] += 1

    def change_formulas_cells(self, number):
        cells = REGULAR_FORMULAS_CELLS.findall(str(self._data))
        for cell in cells:
            if cell not in UNITS:
                letters = REGULAR_LETTERS.sub('', cell)
                if letters not in NOT_CHANGED_COLUMNS:
                    new_cell = cell.replace(letters, self._take_next_letter(str(letters), number))
                    self._data = self._data.replace(cell, new_cell)

    @staticmethod
    def _take_next_letter(letter, number):
        count = SUPPORT_LETTERS_NUMBER
        for item in iter_letters():
            if item == letter:
                count = number
            if not count:
                return item
            count -= 1
