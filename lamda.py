from functools import reduce

f = lambda a, b: a * b

result = f(6, 5)
# print(result)


# find even by filter
numbs = [2, 4, 3, 6, 8, 9, 5]
evens = list(filter(lambda
                        n: n % 2 == 0, numbs))

doubles = list(map(lambda n: n * 2, evens))

sum = reduce(lambda a, b: a + b, doubles)
print(doubles)
print(sum)
print(evens)
