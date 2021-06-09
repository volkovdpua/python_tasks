import os


def filter_list(list, n):
    result = []
    for x in list:
        if x < n:
            result.append(x)
    return result


def find_matches(f_list, t_list):
    result = []
    for x in f_list:
        if x in t_list:
            result.append(x)
    return result


def comb(*args):
    result = list(zip(*args))
    return result


def comb_without_zip(*args):
    min_length = len(args[0])
    result = []
    for list in args:
        if len(list) < min_length:
            min_length = len(list)
    for i in range(min_length):
        it = []
        for x in args:
            it.append(x[i])
        result.append(it)
    return result


def merge_dict(d1, d2):
    result = d1.copy()
    result.update(d2)
    return result


def get_extension(fname):
    result = os.path.splitext(fname)
    return result[-1]

