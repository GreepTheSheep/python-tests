a=float(input('Nombre 1:'))
op=str(input('Signe:'))
b=float(input('Nombre 2:'))

if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '*':
    print(a*b)
elif op == '/':
    if b == 0:
        print('Division par zéro impossible')
    else:
        print(a/b)
else:
    print('erreur')
