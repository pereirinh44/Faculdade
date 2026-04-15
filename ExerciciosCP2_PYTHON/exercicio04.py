num = int(input('Entrada: '))
final = num * 10
inicial = num
tabuada = 0

print('Saida: ', end = ' ')

for num in range(0,final+1,num):
    print(f'{inicial} * {tabuada} = {num}')
    tabuada = tabuada + 1