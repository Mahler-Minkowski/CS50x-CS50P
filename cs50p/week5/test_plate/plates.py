import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    j="A"
    if not 2<=len(s)<=6:
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    for char in s:
            if not (char.isalpha() or char.isdigit()):
                return False
    for char in s:
         if not char.isalpha():
              j=s.index(char)
         #break位置不对 应该缩进
              break
              #return s.index(char) 这步会将整个函数结束
    #j=s.index(char)
    try:
        j=int(j)
        if s[j]=='0':
            return False
    except ValueError:
        return False
    j=str(j) #j不是字符串 没有isdigit和isalpha函数
    if j.isdigit():
         for _ in range(int(j)+1,len(s)):
             if s[_].isalpha():
                 return False
         return True

    elif j.isalpha():
         return True

if __name__ == "__main__":
    main()
