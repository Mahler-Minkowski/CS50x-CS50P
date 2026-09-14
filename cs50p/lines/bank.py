greeting=input("Greeting: ").strip().lower()


if greeting.startswith("hello"): #start s with 函数 注意有个s
    print("0$")
elif greeting.startswith("h"):
    print("20$")
else:
    print("100$")

if greeting[:5]=="hello":
    print("0$")
# elif x[0]=="h": (可能的错误点：空字符输入报错)
elif greeting[:1]=="h":
    print("20$")
else:
    print("100$")
