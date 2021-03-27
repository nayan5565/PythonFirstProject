import sys


def fact(n):
    f = 1
    for j in range(1, n + 1):
        f = f * j
    return f


result = fact(3)
print(result)

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

i = 0


# recursion
def rec():
    global i
    i += 1
    print('hi', i)
    if i < 990:
        rec()


rec()


# fab with recursion
def fac_rec(n):
    if n == 0:
        return 1
    return n * fac_rec(n - 1)


res = fac_rec(5)
print('fact with {} recursive: '.format(res), res)
