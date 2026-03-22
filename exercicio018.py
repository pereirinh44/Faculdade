import os 
os.system('cls')

lado1 = int(input('Lado A: '))
lado2 = int(input('Lado B: '))
lado3 = int(input('Lado C: '))

equilatero = lado1 == lado2 == lado3


if lado1 + lado2 >= lado3:
    if lado1 + lado3 >= lado2:
        if lado2 + lado3 >= lado1:
            if equilatero:
                print(f'Os lados {lado1}, {lado2} e {lado3} formam um triângulo equilátero.')
            elif lado1 == lado3:
                 print(f'Os lados {lado1}, {lado2} e {lado3} formam um triângulo isosceles.')
            elif lado1 == lado2:
                 print(f'Os lados {lado1}, {lado2} e {lado3} formam um triângulo isosceles.')
            elif lado2 == lado3:
                 print(f'Os lados {lado1}, {lado2} e {lado3} formam um triângulo isosceles.')
            else:
                print(f'Os lados {lado1}, {lado2} e {lado3} formam um triângulo escaleno.')
        else:
            print(f'Os lados {lado1}, {lado2} e {lado3} não formam um triângulo')
    else:
        print(f'Os lados {lado1}, {lado2} e {lado3} não formam um triângulo')
else:
    print(f'Os lados {lado1}, {lado2} e {lado3} não formam um triângulo')


