import os 
os.system('cls')

salario = float(input('Digite seu salário: '))

if salario <= 2259.20:
    print ('IR R$ 0.00')
elif 2259.21 <= salario <= 2826.65:
    ir = salario * 0.075 - 169.44
    print (f'IR R$ {ir:.2f}')
elif 2826.66 <= salario <= 3751.05:
    ir = salario * 0.15 - 381.44
    print (f'IR R$ {ir:.2f}')    
elif 3751.06 <= salario <= 4664.68:
    ir = salario * 0.225 - 662.77
    print (f'IR R$ {ir:.2f}')  
else:
    ir = salario * 0.275 - 896.00
    print (f'IR R$ {ir:.2f}')  

