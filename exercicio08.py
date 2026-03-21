import os 
os.system('cls')

nota = float(input('De uma nota: '))

if 0 <= nota <= 10:
    print(f'{nota:.1f} é uma nota válida.')
else:
    print(f'{nota:.1f} é uma nota inválida.')