I=input("Input:").lower()
Vowels=['a','e','i','o','u']
print("output:",end="")
for char in I:
    if char not in Vowels:
        print(char,end="")
print()
