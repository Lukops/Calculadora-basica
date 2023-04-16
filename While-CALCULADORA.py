'''
Calculadora
'''

while True:
    num1 = input('Digite um número: ') 
    num2 = input('Digite outro número: ')
    operador = input('Digite um operador (+, -, /, *): ')
    
    numeros_validos = None
    # Lembrar de não definir variáveis dentro dos blocos de código, semprem fora
    num1_float = 0 
    num2_float = 0

    try:
        num1_float = float(num1) 
        num2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos == None:
        print('Um ou ambos os números são inválidos.')
        continue
    
    operadores_permitidos = "+-/*"

    if operador not in operadores_permitidos:
        print('Operador inválido.')

    if len(operador) > 1:
        print('Digite apenas um operdor.')
        
    print('Realizando os cálculos:')
    if operador == '+':
        print(f'{num1_float}+{num2_float}=',num1_float + num2_float)
    if operador == '-':
        print(f'{num1_float}-{num2_float}=',num1_float - num2_float)
    if operador == '/':
        print(f'{num1_float}/{num2_float}=',num1_float / num2_float)
    if operador == '*':
        print(f'{num1_float}*{num2_float}=',num1_float * num2_float)   
    else: 
        print('O código não deveria chegar aqui...')
    

    sair = input('Quer [s]air? ').lower().startswith("s")

    if sair is True:
        break