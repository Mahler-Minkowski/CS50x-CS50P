import sys
Em=[]
with open(sys.argv[1],'r') as f:
    lines=f.readlines()
    for i in lines:
        i=i.lstrip()
        Em.append(i)
    print(Em)
