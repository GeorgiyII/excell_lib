from excell_lib.constants import (
    iter_letters,
    get_letter,
)


class Column:

    _letter: str = None
    _cells = {}
    _number: int = None

    def __init__(self, letter: str, number: int, cells: dict):
        self._letter = letter
        self._cells = cells
        self._number =number

    def __str__(self):
        result = [self._letter]
        for cell in self.cells:
            data = cell.value
            result.append(data)
        return str(result)

    @property
    def letter(self):
        return self._letter

    @property
    def cells(self):
        for key in self._cells:
            yield self._cells[key]

    @property
    def number(self):
        return self._number

    def set_letter(self, letter):
        self._letter = letter

    def change_coordinate_right(self, number: int):
        interval_number = number - self._number
        self.set_letter(get_letter(number))
        for cell in self.cells:
            cell.change_formulas_cells(interval_number)
            cell.change_coordinate(self.letter)

    def change_letter_right(self, letter: str):
        number = self._count_letter_number(letter) - self._number
        self.set_letter(letter)
        for cell in self.cells:
            cell.change_formulas_cells(number)

    def clear_cells(self):
        for cell in self.cells:
            cell.clear()

    @staticmethod
    def _count_letter_number(letter: str):
        count = 0
        for item in iter_letters():
            count += 1
            if item == letter:
                return count
