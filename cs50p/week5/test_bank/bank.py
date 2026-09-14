def main():
    greeting=input("Greeting: ")
    value(greeting)


def value(greeting):
    greeting=greeting.strip().lower()
    if greeting.startswith("hello"): #start s with 函数 注意有个s
        return "0$"
    elif greeting.startswith("h"):
        return "20$"
    else:
        return "100$"


if __name__ == "__main__":
    main()



