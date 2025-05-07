num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segunfo número: '))
sinal = input('Digite o sinal para o calculo (+ | - | * | /): ')

if sinal == '+':
    calc = lambda a, b: a + b
    print(calc(num1, num2))
elif sinal == '-':
    calc = lambda a, b: a - b
    print(calc(num1, num2))
elif sinal == '*':
    calc = lambda a, b: a * b
    print(calc(num1, num2))
elif sinal == '/':
    calc = lambda a, b: a / b
    print(calc(num1, num2))
else:
    print('Insira um operador valido')


