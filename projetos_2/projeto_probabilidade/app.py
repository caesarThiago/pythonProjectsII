
def probabilidadeFunc(casosFav, casosPos): 
    var_result = casosFav/casosPos
    return var_result * 100

var_choice = input('Deseja descobrir a probabilidade do evento? Sim? ou Não? ')

if var_choice == 'Sim': 
    var_casos_Fav = int(input('Digite o número de casos favoráveis: '))
    var_casos_Pos = int(input('Digite o número de casos possíveis: '))

    print(f'A probabilidade é de {probabilidadeFunc(var_casos_Fav, var_casos_Pos):.2f}%')
elif var_choice == 'Não':
    print('Ok, Saindo!')
else:
    print('Error001: null_value or invalid_value!')