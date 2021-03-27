from Calc import *

money = 100


def first_call():
    print('he')


def su(x, y=6):
    t = x + y
    s = x - y
    return t, s


def su_new(x, *y):
    t = x
    for tt in y:
        t = t + tt
    return t


# a = int(input('first value'))
# b = int(input('second value'))
# first_call()
# result, minus = su(a, b)
# result2, minus2 = su(x=a)
# result3 = su_new(a, b, 3, 3)
# print('sum: ', result2)
# print('minus: ', result3)


def person(name, **data):
    globals()['money'] = 200
    print(name)
    for i, j in data.items():
        print(i, j)


# person('nayan', age=32, city='dhaka', cell='01629683563')
# print(money)


def count(lst):
    even = 0
    odd = 0
    nothing = 'something'
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd, nothing


lst = [12, 32, 53, 63, 23, 86, 47, 90, 57]

even, odd, nothing = count(lst)


# print('even: {} and odd: {} and nothing: {}'.format(even, odd, nothing))

def div(a, b):
    return print(a / b)


def smart_div(func):
    def inner(a, b):
        if a < b:
            # sawp value if a is lesser then b
            a, b = b, a
        return func(a, b)

    return inner


div = smart_div(div)

print('func says',__name__)


def rev(x):
    return x[::-1]


my_txt = rev('nayan')
if __name__ == '__main__':
    print(add(3, 4))
    div(2, 4)
