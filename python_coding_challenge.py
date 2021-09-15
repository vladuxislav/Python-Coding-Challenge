# 1

from collections import defaultdict


def rename_me_with_order(string):
    dictionary = defaultdict(int)
    for char in string:
        if char.isdigit():
            dictionary[char] += 1
    return dict(dictionary)


print(rename_me_with_order('p823j98fh89ahf9sd8h0afsd'))


# 2
# this option is preferable if the order of the keys in the dictionary doesn't matter

def rename_me(string):
    dictionary = {str(k): 0 for k in range(10)}
    for char in string:
        if char.isdigit():
            dictionary[char] += 1
    dictionary = {k: v for k, v in dictionary.items() if v != 0}
    return dict(dictionary)


print(rename_me('p823j98fh89ahf9sd8h0afsd'))
