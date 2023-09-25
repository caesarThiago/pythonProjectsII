def regraTresDP (var_a, var_b, var_c):
    var_x = (var_b * var_c) / var_a
    return var_x

def regraTresIP (var_a, var_b, var_c):
    var_x = (var_a * var_c) / var_b
    return var_x

var_choice = input('Deseja descobrir o valor de x através da regra de três? Sim? ou Não? ')

if var_choice == 'Sim':
    var_choice = input('Regra três simples DP(Diretamente Proporcional) ou IP(Inversamente Proporcional): ')

    if var_choice == 'DP': 
        var_a = float(input('Digite o primeiro numero: '))
        var_b = float(input('Digite o segundo numero: '))
        var_c = float(input('Digite o terceiro numero: '))

        var_x = regraTresDP(var_a, var_b, var_c)

        print(f'O valor de x é {var_x:.2f}')
    elif var_choice == 'IP': 
        var_a = float(input('Digite o primeiro numero: '))
        var_b = float(input('Digite o segundo numero: '))
        var_c = float(input('Digite o terceiro numero: '))

        var_x = regraTresIP(var_a, var_b, var_c)

        print(f'O valor de x é {var_x:.2f}')
    else:
        print('Error002: unexpected_value!')
elif var_choice == 'Não':
    print('Ok, saindo!')
else:
    print('Error001: null_value or invalid_value!')