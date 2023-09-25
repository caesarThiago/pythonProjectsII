def meninaAltura(alturaPai, alturaMae): 
    var_altura = (alturaPai + alturaMae - 13) / 2
    return var_altura

def meninoAltura(alturaPai, alturaMae): 
    var_altura = (alturaPai + alturaMae + 13) / 2
    return var_altura

var_choice = input('Deseja saber a altura do seu filho ou filha? Sim? ou Não? ')

if var_choice == 'Sim': 
    var_choice = input('Qual é o gênero do bebê ou criança? Masculino? ou Feminino? ')

    if var_choice == 'Masculino': 
        var_altura_pai = float(input('Digite a altura do pai: '))
        var_altura_mae = float(input('Digite a altura da mãe: '))

        var_altura = meninoAltura(var_altura_pai, var_altura_mae)
        print(f'A altura do seu filho (menino) será de: {var_altura:.2f}cm')
    elif var_choice == 'Feminino': 
        var_altura_pai = float(input('Digite a altura do pai: '))
        var_altura_mae = float(input('Digite a altura da mãe: '))

        var_altura = meninaAltura(var_altura_pai, var_altura_mae)
        print(f'A altura da sua filha será de: {var_altura:.2f}cm') 
    else:
        print('Error002: unexpected_value!')
elif var_choice == 'Não': 
    print('Ok, saindo!')
else: 
    print('Error001: null_value or invalid_value!')