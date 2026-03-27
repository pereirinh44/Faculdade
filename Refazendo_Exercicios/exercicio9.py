import os
os.system('cls')

num1 = int(input('Nota 1 : '))


if num1 < 0 or num1 > 10:
    print('nota invalida')
else:
    num2 = int(input('Nota 2 : '))
    if num2 < 0 or num2 > 10:
        print('nota invalida')
    else: 
        media = (num1 + num2) / 2
        
        if media >= 5: 
            print(f'Média {media} Aprovado')
        else:
            print(f'Média {media} Reprovado')


          


