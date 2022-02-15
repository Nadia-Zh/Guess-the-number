import argparse
from random import randint

a1, a2=0, 100

def ParsingCheck (a1, a2):
    ap = argparse.ArgumentParser()
    
    ap.add_argument("-a1", "--LBorder",default=a1, help="Left Border")
    ap.add_argument("-a2", "--RBorder",default=a2, help="Right Border")
    args = vars(ap.parse_args())
    try:
        a1=int(args['LBorder'])
    except ValueError as error:
        print(f'You should type a number: {error} \n')
    try:
        a2=int(args['RBorder'])
    except ValueError as error:
        print(f'You should type a number: {error} \n')    

    if a2<a1:
        a1+=a2
        a2=a1-a2
        a1-=a2
    return a1, a2

def numbcheck (numb):
    if numb=='stop':
        print("\nBye!")
        exit()
    try:
        numb=int(numb)
    except ValueError as error:
        print(f'You should type a number: {error} \n')
        return None
    if numb<a1 or numb>a2:
        print(f'You should choose any number in {[a1, a2]}\n')
        return None
    return numb 

def compare(a, numb):
    if numb>a:
        print(f'Your number {numb} is bigger than a\n')
    elif(numb<a):
        print(f'Your number {numb} is less than a\n')
    else:
        print("You won!")
        exit()

a1, a2=ParsingCheck(a1, a2)
a=randint(a1, a2)

while True:
    numb=input(f'Hello! Enter any number from {a1} to {a2} or type "stop" to quit the game: ')
    numb = numbcheck(numb)
    if numb is not None:
        compare(a, numb)
    
