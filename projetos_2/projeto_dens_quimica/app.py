def densidadeQuimica(massa_solucao, vol_solucao): 
    var_dens = massa_solucao / vol_solucao
    return var_dens

var_choice = input('Deseja calcular a densidade de soluções químicas com densidades diferentes? Sim? ou Não? ')

if var_choice == 'Sim': 
    var_massa_solucao = float(input('Digite a massa de solução: '))
    var_vol_solucao = float(input('Digite o volume de solução: '))

    var_dens = densidadeQuimica(var_massa_solucao, var_vol_solucao)

    print(f'A densidade da solução é de {var_dens:.2f}')
elif var_choice == 'Não': 
    print('Ok, saindo!')
else: 
    print('Error001: null_value or invalid_value!')