class Test:

    _number = 2

    def number_change(self):
        new = self._number
        return new - 1

    def change_number(self):
        self._number = 4


test = Test()
test_2 = Test()

print(test._number)

test.change_number()

print(test._number)

print(test_2._number)
