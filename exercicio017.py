lado1 = int(input('Lado A: '))
lado2 = int(input('Lado B: '))
lado3 = int(input('Lado C: '))

if lado1 + lado2 >= lado3:
    if lado1 + lado3 >= lado2:
        if lado2 + lado3 >= lado1:
            print(f'Os lados {lado1}, {lado2} e {lado3} formam um triângulo')
        else:
            print(f'Os lados {lado1}, {lado2} e {lado3} não formam um triângulo')
    else:
        print(f'Os lados {lado1}, {lado2} e {lado3} não formam um triângulo')
else:
    print(f'Os lados {lado1}, {lado2} e {lado3} não formam um triângulo')