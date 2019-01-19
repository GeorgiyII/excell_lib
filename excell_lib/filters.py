from excell_lib.constants import ALWAYS_MERGED_LIST


def unmerge_filter(coordinate: str):
    flag = True
    for letter in ALWAYS_MERGED_LIST:
        if letter in coordinate:
            flag = False
    return flag


def not_formula(data):
    flag = True
    if isinstance(data, str):
        if data[0] == '=':
            flag = False
    return flag
