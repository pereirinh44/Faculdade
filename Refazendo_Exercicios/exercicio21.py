sal = float(input('Sálario: '))

if sal <= 1518:
    inss = sal * 0.075

elif sal >1518 and sal <= 2793.88:
    inss = sal * 0.09 -22.77
   
elif sal > 2793.88 and sal <= 4190.83:
    inss = sal * 0.12 - 106.59
    
elif sal > 4190.83 and sal <= 8157.41:
    inss = sal * 0.14 - 190.40
    
else:
    teto = 8157.41
    inss = teto * 0.14 - 190.40

if sal <= 2259.20:
    ir = 0
 
elif sal > 2259.20 and sal <= 2826.65:
    ir = sal * 0.075 - 169.44
    
elif sal > 2826.65 and sal <= 3751.05:
    ir = sal * 0.15 - 381.44
   
elif sal > 3751.05 and sal <= 4664.68:
    ir = sal * 0.225 - 662.77
  
else:
    ir = sal * 0.275 - 896.00

salario_liquido = sal - inss - ir 
print(f'''Salário: {sal}
INSS: {inss}
IR: {ir}
Salário Liquido: {salario_liquido}''')