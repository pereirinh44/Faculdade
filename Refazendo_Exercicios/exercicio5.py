numero = int(input('Número: '))

multiplo = ((numero //5)+1) * 5

if numero % 5 == 0:
    print(numero)
else: 
    print(multiplo)