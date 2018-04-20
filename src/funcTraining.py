# -*- coding: utf-8 -*-
"""
函数即是一个普通的对象，可以如同对象一样使用
"""


def echo(text):
    print(text)


def marker(label):
    def echo(message):
        print(label + " : " + message)

    return echo


if __name__ == "__main__":
    schedule = [(echo, "Hello"), (echo, "World")]

    for func, arg in schedule:
        func(arg)
    pass

    marker("learning")('python')
