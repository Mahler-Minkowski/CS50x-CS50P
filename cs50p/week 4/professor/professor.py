import random


def main():
    score=0
    level=get_level()
    for i in range(1,11):
        x=generate_integer(level)
        y=generate_integer(level)
        z=x+y
        time=0
        for j in range(1,4):
            print(f'{x} + {y}= ',end='')
            asr=input()
            try:
                asr=int(asr)
                if int(asr)==z:
                    score=score+1
                    break
                else:
                     time=time+1
                     print('EEE')
                     if time==3:
                        print(f'{x} + {y} = {z}')
            except ValueError:
                time=time+1
                print('EEE')
                if time==3:
                    print(f'{x}+{y}={z}')
    print(score)


def get_level():
    while True:
        level=input("Level: ")
        try:
            level=int(level)
            if 1<=level<=3:
               return level
        except ValueError:
            print('The wrong input')

def generate_integer(level):
    if level==1:
        X=random.randint(0,9)

    elif level==2:
        X=random.randint(10,99)
    elif level==3:
        X=random.randint(100,999)
    return X


if __name__ == "__main__":
    main()
