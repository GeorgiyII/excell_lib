from excell_lib.constants import (
    REGULAR_FORMULAS_CELLS,
    REGULAR_LETTERS,
    iter_letters,
    NOT_CHANGED_COLUMNS,
    SUPPORT_LETTERS_NUMBER
)


class Cell:

    _cypher: str = None
    _coordinate: list = []
    _data: str = None
    _style = None

    def __init__(self, cell, column_number: int, row_number: int):
        self._cypher = cell.coordinate
        self._coordinate = [row_number, column_number]
        self._data = cell.value
        self._style = cell._style

    def get_data(self):
        return str(self._data)

    def get_coordinate(self):
        return self._coordinate

    def get_cypher(self):
        return self._cypher

    def get_style(self):
        return self._style

    def change_coordinate(self, cypher, coordinate):
        self._cypher = cypher
        self._coordinate = coordinate

    def change_formulas_cells(self, number):
        cells = REGULAR_FORMULAS_CELLS.findall(self._data)
        for cell in cells:
            letters = REGULAR_LETTERS.sub('', cell)
            if letters not in NOT_CHANGED_COLUMNS:
                new_cell = cell.replace(letters, self._take_next_letter(str(letters), number))
                self._data = self._data.replace(cell, new_cell)

    def _take_next_letter(self, letter, number):
        count = SUPPORT_LETTERS_NUMBER
        for item in iter_letters():
            if item == letter:
                count = number
            if not count:
                return item
            count -= 1


# cell = Cell()
# cell._data = '=SUMM(D154:E105)'
# cell.change_formulas_cells(3)


# for s in iter_letters():
#     print(s)
#     if s == 'BB':
#         break

