import os 
os.system('cls')

salario = float(input('Digite seu salário: '))
if salario <= 1518:
    inss = salario * 0.075  
elif 1518.01 <= salario <= 2793.88:
    inss = salario * 0.09 - 22.77  
elif 2793.89 <= salario <= 4190.83:
    inss = salario * 0.12 - 106.59  
elif 4190.84 <= salario <= 8157.41:
    inss = salario * 0.14 - 190.40 
else:
    inssFixo = 8157.41 * 0.14 - 190.40
    inss = inssFixo
   
if salario <= 2259.20:
    ir = 0
elif 2259.21 <= salario <= 2826.65:
    ir = salario * 0.075 - 169.44
elif 2826.66 <= salario <= 3751.05:
    ir = salario * 0.15 - 381.44 
elif 3751.06 <= salario <= 4664.68:
    ir = salario * 0.225 - 662.77
else:
    ir = salario * 0.275 - 896.00
    

liquido = salario - inss - ir

print(f'''Salário..........: R$ {salario:.2f}
INSS.............: R$ {inss:.2f}
IR...............: R$ {ir:.2f}
Salário líquido..: R$ {liquido:.2f}''')

    