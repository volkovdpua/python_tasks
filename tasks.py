import os



def filter_list(list,n):
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
    result = []
    len_args = []
    for x in args:
        len_args.append(len(x))
    for i in range(min(len_args)):
        it = []
        for x in args:
            it.append(x[i])
        result.append(it)
    return result

def merge_dict(d1,d2):
    result = d1.copy()
    return result.update(d2)

def get_extension(fname):
    result = os.path.splitext(fname)
    return result[-1]

print("Бога нет")
print("Бога нет")
print("Бога нет")
print("Бога нет")