import pyfiglet
import sys
import random
I=input("Input: ")
F=['-f','--font']
Script=pyfiglet.FigletFont.getFonts()

if (len(sys.argv)==3 and sys.argv[1] in F):
    if sys.argv[2] in Script:
         print(pyfiglet.figlet_format(I, font=(sys.argv[2])))
    else:
        sys.exit('Invalid Usage')
elif len(sys.argv)==1:
    random_1=random.choice(Script)
    print(pyfiglet.figlet_format(I,font=(random_1)))
else:
    sys.exit('Invalid Usage')
