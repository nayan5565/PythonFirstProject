# w=write,r=read, a=append, rb=read binary
fileWrite = open('abc', 'a')
# fileWrite.write('Nurul',)

fileRead = open('abc', 'r')
# print(fileRead.read())

# for i in fileRead:
#     print(i, end='')
# fileNewWrite = open('xyz', 'w')

# for data in fileRead:
#     fileNewWrite.write(data)

imgFile = open('images/laptop.jpg', 'rb')
# for i in imgFile:
#     print(i)

createImg = open('images/laptopNew.jpg', 'wb')
for i in imgFile:
    createImg.write(i)
