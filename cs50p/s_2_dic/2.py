import sys
import csv


def main():
    linejdge()
    try:
        with open(sys.argv[1],'r') as i , open(sys.argv[2],'a') as o:
            reader=csv.DictReader(i)
            writer = csv.DictWriter(o, fieldnames=["first","last","house"])
            for j in reader:
                first, last=j['name'].split(',')
                writer.writerow({'first':first,'last':last,'house':j['house']})

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
