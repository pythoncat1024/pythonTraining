# -*- coding: utf-8 -*-
"""
函数即是一个普通的对象，可以如同对象一样使用

`lambda`表达式，就像`def`一样，创建了一个之后能够调用的函数，但是它返回了一个函数，而不是将这个函数值赋给一个变量名。
"""


def gensquare(N):
    for i in range(N):
        yield i ** 2


if __name__ == "__main__":
    pass
    # print([x for x in map(inc, numbers)])
    # print([x for x in map(lambda item: item + 100, numbers)])
    #
    # print(list(map(pow, [1, 2, 3], [4, 5, 6])))
    #
    # print([ord(z) for z in "hello world"])
    #
    # print([(x, y) for x in range(0, 5) if x % 2 == 0 for y in range(5) if y % 2 == 1])
    #
    # x='hello world! hello rxjava'
    #
    # for index,item in enumerate(x):
    #     print(index,item)

    print("====================================================")
    print(iter([1, 2, 3]))
    # for item in zip('abc','def','hij'):
    #     print(item)

    for x in gensquare(5):
        print(x, end=" ")
