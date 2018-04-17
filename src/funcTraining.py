
def tester(start):
    state = start

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1

    return nested


f = tester(0)
f("php")
f("php")
tester(4)("c++")
f("php")

"""
php 0
php 1
c++ 4
php 2
"""

# SyntaxError: no binding for nonlocal 'state' found


"""
def tester(start):
    global state
    state = start

    def nested(label):
        global state
        print(label, state)
        state += 1

    return nested


f = tester(0)
f("php")
f("php")
tester(4)("c++")
f("php")
"""
# 对应的输出：
"""
php 0
php 1
c++ 4
php 5
"""