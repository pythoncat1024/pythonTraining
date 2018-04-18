# -*- coding: utf-8 -*-


def min1(*args):
    first, *others = args
    # print(args)
    # print("first==" + str(first))
    # print("others==" + str(others))
    for item in others:
        if first > item:
            first = item
    return first


m = min1(*[3, 2, 14, 5])
print("min ", m)


def minmax(*args):
    func, first, *others = args

    for item in others:
        if func(first, item):
            first = item
    return first


def lt(x, y):
    return x > y


def gt(x, y):
    return x < y


print(minmax(*[gt, 4, 2, 5, 9]))
