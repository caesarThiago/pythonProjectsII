var_choice = input('Deseja contar um número? Sim? ou Não? ')

if var_choice == 'Sim':
    var_num = int(input('Digite um número: '))
    inicio = 0
    while inicio < var_num: 
        print(f'O número é {inicio}')
        inicio += 1
        
elif var_choice == 'Não':
    print('Ok, Saindo!')
else:
    print('Error001: null_value or invalid_value!')