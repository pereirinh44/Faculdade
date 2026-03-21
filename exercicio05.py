num = int(input('digite um número: '))

multiplo = num + (5 - (num % 5))

if num % 5 == 0:
    print(num)

if num % 5 != 0:
    print(multiplo)
