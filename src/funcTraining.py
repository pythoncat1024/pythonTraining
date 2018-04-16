# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     funcTraining
   Description :
   Author :       cat
   date：          2018/4/16
-------------------------------------------------
   Change Activity:
                   2018/4/16:
-------------------------------------------------
"""


def intersect(s1, s2):
    res = []
    for x in s1:
        if x in s2:
            res.append(x)
    return res


if "__main__" == __name__:
    s1 = "scam"
    s2 = "pcsm"

    print(intersect(s1, s2))          // ['s', 'c', 'm']
    print([x for x in s1 if x in s2]) // ['s', 'c', 'm']
    pass
