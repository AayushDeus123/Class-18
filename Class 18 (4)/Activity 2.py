#ZeroDivisionError and NameError using except and finally 
try:
    num = int(input('Enter a number : '))
    num1 = int(input('Enter another number to be divided with :'))
    result = num/num1
    print('The result is',result)
    print('The result is',result1)
except ZeroDivisionError:
    print('Number devided by zero is undefined')
except ValueError:
    print('The input is not a number')
except NameError as ex:
    print('Your error is' ,ex)
finally:
    print('\nI will get executed no matter what')