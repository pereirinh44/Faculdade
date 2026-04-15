num = int(input('Entrada: '))
mult = 0
inicial = num
final = num * 10

print('Saida: ', end = ' ')

for num in range(inicial,final+1,num):
    multiplo = num * (mult + 1)
    print(multiplo, end = ' ')