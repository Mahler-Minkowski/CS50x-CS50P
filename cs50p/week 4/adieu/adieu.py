import sys
list=[]
while True:
    try:
        Names=input('Name: ')
        if Names != "":
            list.append(Names)
    except EOFError:
        print()
        if len(list)==1:
            print('Adieu, adieu, to '+list[0])
            break
        elif len(list)==2:
            print(f'Adieu, adieu, to {list[0]} and {list[1]}')
        elif len(list)>=2:
            print('Adieu, adieu, to ', end='')
            for i in list[0:-1]:
                print(f'{i}' ,sep=", ", end=", ")

            print('and '+list[-1])
            break


