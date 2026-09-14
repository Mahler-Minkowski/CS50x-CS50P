"""
alphabet=["A","B","C","D","E","F","G",'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
str.Camel=input("plz input camel genre")
for i in alphabet:
    Camel=Camel.split(i)
print("_".join(Camel))
"""
Camel=input("plz input camel genre")
EL=[]
for char in Camel:
    if "A"<=char<="Z":
    if char.isupper():
        EL.append("_")
        EL.append(char.lower())
    else:
        EL.append(char)
print("".join(EL))

