n1 = float(input('Escreva a primeira nota: '))
n2 = float(input('Escreva a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'Média {media : .1f} - reprovado')
else:
    print(f'Média {media : .1f} - aprovado')