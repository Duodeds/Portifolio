from uteis import novamente  # Importação correta

def calcular():
    operacao = input('''
Por favor, digite a operação matemática que deseja realizar:
+ para adição
- para subtração
* para multiplicação
/ para divisão
** para exponenciação
% para módulo (resto da divisão)
''')

    while operacao not in ['+', '-', '*', '/', '**', '%']:
        print('Caractere inválido, digite +, -, *, /, ** ou %.')
        operacao = input('Digite novamente a operação: ')

    numero_1 = int(input('Por favor, insira o primeiro número: '))
    numero_2 = int(input('Por favor, insira o segundo número: '))

    if operacao == '+':
        print(f'{numero_1} + {numero_2} = {numero_1 + numero_2}')

    elif operacao == '-':
        print(f'{numero_1} - {numero_2} = {numero_1 - numero_2}')

    elif operacao == '*':
        print(f'{numero_1} * {numero_2} = {numero_1 * numero_2}')

    elif operacao == '/':
        if numero_2 == 0:
            print('Erro: divisão por zero não é permitida!')
        else:
            print(f'{numero_1} / {numero_2} = {numero_1 / numero_2}')

    elif operacao == '**':
        print(f'{numero_1} ** {numero_2} = {numero_1 ** numero_2}')

    elif operacao == '%':
        if numero_2 == 0:
            print('Erro: divisão por zero não é permitida!')
        else:
            print(f'{numero_1} % {numero_2} = {numero_1 % numero_2}')

    novamente.novamente()  
