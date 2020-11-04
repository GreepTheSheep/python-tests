import random
nbcalcs=int(input('Nombre de calculs :  '))
breps=int(0)

for x in range(nbcalcs):
    nb1 = random.randint(1, 9)
    nb2 = random.randint(1, 9)
    result=int(input(str(nb1) + '+' + str(nb2) + '= '))
    if nb1+nb2 == result:
        print('Bonne réponse :)')
        breps+=1
    else:
        print('Mauvaise réponse :(')
        print('La réponse était: ',nb1+nb2)
    print('')
print('Vous avez', breps, 'bonnes réponses et', nbcalcs-breps, 'mauvaises réponses.')
