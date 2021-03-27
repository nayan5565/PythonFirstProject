a = 5
b = 2

try:
    print('resource open')
    print(a / b)
    k = int(input('Enter a number'))
except ZeroDivisionError as e:
    print('you can not divide number by zero', e)
except ValueError as e:
    print('Invalid input', e)
except Exception as e:
    print('Something went wrong', e)
finally:
    print('resource close')
