#Exception Handling using WHILE LOOP
valid = False

while not valid:
    try:
        a = int(input('Enter a number : '))
        while a%2 == 0:
            print('Even')
            value = True
    except ValueError:
        print('Invalid input')
    