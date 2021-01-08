from random import *
n=int(input('Entrer maximun number: '))
while n<1:
    n=int(input('Maximum number is lower than 1, be higher: '))
Nbrand=randint(0, n)
essais=0
trouve=False
while trouve==False:
    valeur=int(input('Guess the number between 0 and '+n+': '))
    essais=essais+1
    if valeur<Nbrand:
        print('Lower')
    elif valeur>Nbrand:
        print('Higher')
    else:
        print('Congrats! you found the right number on', essais, 'tryes')
        trouve=True