#Calcular média apenas se as duas notas forem validas 
#Caso qualquer nota seja invalida finaizar programa com a mensagem "nota x invalida"
import os 
os.system('cls')

n1 = float(input('Escreva a primeira nota: '))
if n1 < 0:
    print(f'Nota {n1:.1f} inválida!')
elif n1 > 10:
    print(f'Nota {n1:.1f} inválida!')
else:
    n2 = float(input('Escreva a segunda nota: '))
    if n2 < 0:
        print(f'Nota {n2:.1f} inválida!')
    elif n2 > 10:
        print(f'Nota {n2:.1f} inválida!')
    else:
        media = (n1 + n2) / 2
        if media < 5 :
            print(f'Média {media:.1f} - Reprovado')
        else: 
            print(f'Média {media:.1f} - Aprovado')