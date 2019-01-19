from excell_lib.constants import ALWAYS_MERGED_LIST, FORMULA_CHARS, NUMBERS


def change_formula_cells(data: str):
    # value = list(data)
    # print(value)
    # for i, char in enumerate(value[1:]):
    #     if char in FORMULA_CHARS:
    #         print(char)
    #         char = chr(ord(char)+1)
    #         value[i+1] = char
    # print(''.join(value))
    return data


def get_number(data):
    args = data.split(';')
    return len(args)

# if not re.findall(PASSWORD_REGULAR, data['password']):
#     pass
