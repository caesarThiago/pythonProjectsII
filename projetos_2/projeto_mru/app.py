def MRU(posicao_inicial, velocidade, intervalo_tempo):
    var_s = posicao_inicial + velocidade + intervalo_tempo
    return var_s

var_choice = input('Quer descobrir a posição final? Sim? ou Não? ')

if var_choice == 'Sim':
    var_si = float(input('Digite sua posição inicial (em metros): '))
    var_vel = float(input('Digite sua velocidade (em metros por segundos): '))
    var_int_tempo = float(input('Digite o intervalo de tempo (em segundos): '))

    var_s = MRU(var_si, var_vel, var_int_tempo)

    print(f'A posição final é de {var_s} metros.')
elif var_choice == 'Não':
    print('Ok, saindo!')
else:
    print('Error001: null_value or invalid_value!')

