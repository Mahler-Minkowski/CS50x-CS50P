X=input("Say something plz")
# print(f"{Y[0],Y[1],Y[2]}",sep="…")
#我怎么获得分割后的变量？？？

#法一
Y=str.split(X)
T="…".join(Y)
print(T)

#法二
X=X.replace(" ","…")
print(X)

#法三
print(*Y,sep="()")
