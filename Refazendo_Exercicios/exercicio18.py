ladoa = int(input('Lado A: '))
ladob = int(input('Lado B: '))
ladoc = int(input('Lado C: '))
equilatero = ladoa == ladob == ladoc

if ladoa + ladob > ladoc and ladoa + ladoc > ladob  and ladob + ladoc > ladoa:
    if equilatero:
        print(f'Os lados {ladoa}, {ladob} e {ladoc} formam um triangulo equilatero')
    elif ladoa == ladob or ladoa == ladoc or ladoc == ladob:
        print(f'Os lados {ladoa}, {ladob} e {ladoc} formam um triangulo isosceles')
    else:
        print(f'Os lados {ladoa}, {ladob} e {ladoc} formam um triangulo escaleno')
else:
        print(f'Os lados {ladoa}, {ladob} e {ladoc} não formam triangulo')