#Exception Handling ; TRY and CATCH
try:
    a = int(input('Enter a number :'))
    print('The value of',a,'is',a)
except ValueError as ex:
    print('The error is',ex)
print('I am outside the Try and Catch')    