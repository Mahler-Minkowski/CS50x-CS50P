import sys
import csv


def main():
    linejdge()
    empty=[]
    try:
        with open(sys.argv[1],'r') as i , open(sys.argv[2],'a') as o:
            ipt=csv.reader(i)
            i_=next(ipt)
            writer = csv.DictWriter(o, fieldnames=["first","last","house"])
            writer.writeheader()
            for j in ipt:
                first, last=j[0].split(',')
                writer.writerow({'first':first,'last':last,'house':j[1]})

    except FileNotFoundError:
            sys.exit('Could not read files')



def linejdge():
    if len(sys.argv)==3:
        return True
    elif len(sys.argv)<3:
        sys.exit('Too few command-line arguments')
    else:
        sys.exit('Too many command-line arguments')


if __name__=='__main__':
    main()
