import sys
import csv
from tabulate import tabulate
def main():
    linejdge()
    namejdge(sys.argv[1])
    asciiprint()


def linejdge():
    if len(sys.argv)==2:
        ori=True
        return True
    elif len(sys.argv)<2:
        sys.exit('Too few command-line arguments')
    else:
        sys.exit('Too many command-line arguments')


def namejdge(i):
    if i.endswith('.csv'):
        return True
    else:
        sys.exit('Not a csv file')


def asciiprint():
    with open(sys.argv[1],'r') as f:
        file=csv.DictReader(f)
        print(tabulate(file,headers='keys',tablefmt='grid'))

if __name__=='__main__':
    main()

