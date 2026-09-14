xyz=input("Please insert X Y Z").split()
Error= False
if xyz[1]=="+":
    output=float(xyz[0])+ float(xyz[2])
elif xyz[1]=="-":
    output=float(xyz[0])- float(xyz[2])
elif xyz[1]=="*":
    output=float(xyz[0])* float(xyz[2])
elif xyz[1]=="/" and float(xyz[-1])==0:
    print("WRONG")
    Error=True
elif xyz[1]=="/":
    output=float(xyz[0])/ float(xyz[2])
if not Error==True:
    print(round(output,1))
