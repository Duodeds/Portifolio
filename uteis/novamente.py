def novamente():
    calc_novamente = input('''
Deseja calcular novamente?
Digite S para SIM ou N para NÃO.
''')

    if calc_novamente.upper() == 'S':
        from uteis import calcular  # Importação dentro da função para evitar ciclo
        calcular.calcular()
    elif calc_novamente.upper() == 'N':
        print('Até mais!')
    else:
        novamente()
