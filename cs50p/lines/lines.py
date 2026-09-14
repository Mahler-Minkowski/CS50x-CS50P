import sys
def main():
    if len(sys.argv)==2:
        if filename(sys.argv[1]):
            try:
                with open(sys.argv[1],'r') as f:
                    lines=f.readlines()
                    new=del_list(lines)
                    print(new)
            except FileNotFoundError:
                sys.exit('Files do not exsit')
        else:
            sys.exit('Not a Python file')

    elif len(sys.argv)>2:
        sys.exit('Too many command-line arguments')
    else:
        sys.exit('Too few command-line arguments')

def del_list(n):
    number=0
    for lines in n:
        if lines.strip().startswith('#') or lines.strip()=='':
            pass
        else:
            number=number+1
    return number

def filename(i):
    if i.endswith('.py'):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
