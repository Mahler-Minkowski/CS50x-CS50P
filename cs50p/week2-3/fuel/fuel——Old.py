'''
from fractions import Fraction
while True:
    frac=float((input("plz give a fraction")))
    remains=int(round(100*frac))
    break

if remains > 99:
    print("F")
elif remains < 1:
    print("E")
else:
    print(f"{remains}"+"%")
'''
def main():
    insert=input("plz give a fraction like 3/4").split("/")
    if len(insert)==2:
        if judge(insert):
            convert(insert)
def judge(i):
     if (0<= int(i[0]) <= int(i[1]) and int(i[1]!=0)):
        return True
     else:
       print("plz give a fraction like 3/4")
def convert(i):
    try:
        frac=int(i[0])/int(i[1])
        total=round(frac*100)
    except ZeroDivisionError:
    else:
        if total>=99:
        print("F")
        elif total<=1:
        print("E")
        else:
        print(f"{total}%")
main()





