Whole=[]
while True:
    try:
         Veg=input()
         #Whole=Whole.append(Veg)
         if not Veg in Whole:
             Whole.append(Veg)
         elif 
    except EOFError:
         sorted_Whole=sorted(Whole,key=str.lower)
         for i in range(len(sorted_Whole)):
              print(str(i+1)+"."+sorted_Whole[i].upper())
         break





