import random
level=input('Level: ')
while True:
    try:
        ipt=int(level)
        if ipt>0:
            break
        else:
            raise ValueError
    except ValueError:
        print('your input is not an positive integer')
        level=input("Level:")

n=random.randint(1,ipt)
while True:
    try:
        gs=int(input('Guess: '))
        if gs==n:
            print('Just right!')
            break
        elif gs < n:
            print('Too small!')
        elif gs > n:
            print('Too large!')
    except ValueError:
        print('your input is not an integer')
