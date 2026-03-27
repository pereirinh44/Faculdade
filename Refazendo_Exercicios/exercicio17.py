ladoa = int(input('Lado A: '))
ladob = int(input('Lado B: '))
ladoc = int(input('Lado C: '))

if ladoa + ladob > ladoc and ladoa + ladoc > ladob  and ladob + ladoc > ladoa:
    print(f'Os lados {ladoa}, {ladob} e {ladoc} Formam um triangulo')
else:
    print(f'Os lados {ladoa}, {ladob} e {ladoc} não formam um triangulo')
