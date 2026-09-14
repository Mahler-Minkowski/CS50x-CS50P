import re
import sys


def main():
    L=input("IPv4 Address: ")
    print(validate(L))


def validate(ip):
    a=r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-5][0-5])'
    pattern= '^(' + a + r'\.){3}' + a + '$'
    if re.search(pattern,ip):
        return True
    else:
        sys.exit('False')


if __name__ == "__main__":
    main()
