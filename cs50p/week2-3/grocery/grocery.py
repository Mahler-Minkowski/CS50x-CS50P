from collections import Counter
num=Counter()
while True:
    try:
        X=input().upper().strip()
        if X!="":
            num[X] += 1
    except EOFError:
        for k,v in sorted(num.items()):
            print(f"{v} {k}")
        break
