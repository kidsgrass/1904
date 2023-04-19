# Programa para somar ou multiplicar dois números

op=input('deseja somar (s) ou multiplicar (M)? ')
if (op == 'S' or op == 'M'):
    x= float(input('Digite o primeiro numero: '))
    y= float(input('Digite o segundo numero: '))
    if (op == 'S'):
         r = x + y
    else:
         r= x * y
    print('O resultado é', r)
else:
     print('Opção inválida"')