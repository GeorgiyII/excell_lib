import re
import string
import itertools

ALWAYS_MERGED_LIST = ['A', 'B', 'C', 'D']
NOT_CHANGED_COLUMNS = ['A', 'B', 'C', 'D']

REGULAR_LETTERS = re.compile('[^a-zA-Z ]')
REGULAR_FORMULAS_CELLS = re.compile(r'[a-zA-Z]+[0-9]+')
ALPHABET = string.ascii_uppercase
SUPPORT_LETTERS_NUMBER = 1000000


def iter_letters():
    for size in itertools.count(start=0, step=1):
        for s in itertools.product(ALPHABET, repeat=size):
            yield "".join(s)
