def velocidadePropagacaoOnda(comprimento_onda, frequencia):
    vel_propag_onda = comprimento_onda * frequencia
    return vel_propag_onda

var_choice = input('Deseja descubrir quantos Mach uma aeronave tem? Sim? ou Não? ')

if var_choice == 'Sim':
    var_comprimento_onda = float(input('Digite o comprimento da onda (em metros): '))
    var_frequencia = float(input('Digite a frequência (em hertz): '))
    
    var_vel_propag_onda = velocidadePropagacaoOnda(var_comprimento_onda, var_frequencia)

    print(f'A velocidade de propagação da onda é de {var_vel_propag_onda:.2f}m/s (metros por segundo)')
elif var_choice == 'Não': 
    print('Ok, saindo!')
else: 
    print('Error001: null_value or invalid_value!')

