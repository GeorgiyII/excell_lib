from excell_lib.constants import iter_letters


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
        for cell in self._cells:
            data = self._cells[cell].get_data()
            result.append(data)
        return str(result)

    def get_letter(self):
        return self._letter

    def get_cells(self):
        return self._cells

    def get_number(self):
        return self._number

    def change_coordinate_right(self, number: int):
        number = number - self._number
        self._letter = self._get_letter(number)
        for cell in self._cells:
            cell.change_formulas_cells(number)

    def change_letter_right(self, letter: str):
        number = self._count_letter_number(letter) - self._number
        self._letter = letter
        for cell in self._cells:
            cell.change_formulas_cells(number)

    @staticmethod
    def _count_letter_number(letter: str):
        count = 0
        for item in iter_letters():
            count += 1
            if item == letter:
                return count

    @staticmethod
    def _get_letter(number: int):
        count = 0
        for item in iter_letters():
            count += 1
            if count == number:
                return item
