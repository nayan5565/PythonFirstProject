# x = 8
# r=x % 2
# if r==0:
#     print('even')
# else:
#     print('odd')

# while x >= 1:
#     print('Nayan ', end='')
#     j = 1
#     while j <= 5:
#         print('islam ', end='')
#         j = j + 1
#     x = x - 1
#     print()
#
# n = 'nayan'
# for i in range(1, 10):
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)
#
# for i in range(1, 10):
#     if i % 2 == 0:
#         pass
#     else:
#         print(i)

# for k in range(4):
#     for j in range(4-k):
#         print("#", end="")
#
#     print()

# num=9
# for i in range(2, num):
#     if num % i == 0:
#         print('not prime')
#         break
# else:
#     print('Prime')

# num = 100
# for i in range(2, num):
#     if num % i == 0:
#         print('not prime')
#         continue
#     else:
#         print('Prime', n)

# from array import *

# vals = array('i', [11, 5, 8, 7])
# newVals = array(vals.typecode, (a*2 for a in vals))
# print(newVals.typecode)
# for v in newVals:
#     print(v)

# vals = array('i', [])
#
# n = int(input('Enter the length of the array'))
#
# for v in range(n):
#     nv = int(input('Enter the length of the array'))
#     vals.append(nv)
# print(vals)
#
# # search index from array by value
# i=0
# sv = int(input('Enter the value for search'))
# for e in vals:
#     if e==sv:
#         print(i)
#         break
#     i+=1

from numpy import *

vals = array([12, 43, 13])
vals2 = array([3, 7, 17])
vals3 = vals + vals2
ls = linspace(1, 10, 2)
lgs = logspace(1, 10, 2)
ar = arange(1, 10, 2)
one = ones(4)
zr = zeros(3)
mv = min(vals)
mxv = max(vals)
s = sum(vals)
cc=concatenate([vals,vals2])
m=matrix('1 2 3; 4 5 6; 7 8 9')
print(ls)
print(mv)
print(diagonal(m))
print(m.min())
