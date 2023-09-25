def forcaResultante (massa, aceleracao): 
    var_res = massa * aceleracao
    return var_res

def pesoResultante (massa, aceleracao_grav):
    var_res = massa * aceleracao_grav
    return var_res

def forcaAtrito (coeficiente_atrito, forca_normal): 
    var_res = coeficiente_atrito * forca_normal
    return var_res

def forcaElastica (constante_elastica_mola, deformacao_mola): 
    var_res = constante_elastica_mola * deformacao_mola
    return var_res

var_choice = input('Deseja calcular alguma formula envolvendo dinâmica? Sim? ou Não? ')

if var_choice == 'Sim': 
    var_choice = input('Qual formula você deseja usar? Força Resultante, Peso, Força de Atrito ou Força Elástica: ')
    
    if var_choice == 'Força Resultante': 
        var_massa = float(input('Digite a massa (em quilogramas): '))
        var_aceleracao = float(input('Digite a aceleração (em metros por segundo ao quadrado): '))

        var_fr = forcaResultante(var_massa, var_aceleracao)

        print(f'A força resultante é de {var_fr:.2f}N (Newtons).')
    elif var_choice == 'Peso':
        var_massa = float(input('Digite a massa (em quilogramas): '))
        var_aceleracao_grav = float(input('Digite a aceleração da gravidade (em metros por segundo ao quadrado): '))

        var_peso = pesoResultante(var_massa, var_aceleracao_grav)

        print(f'O peso é de {var_peso:.2f}N (Newtons).')
    elif var_choice == 'Força de Atrito': 
        var_coeficiente_atrito = float(input('Digite o coeficiente de atrito: '))
        var_forca_normal = float(input('Digite a força normal (em newtons): '))

        var_forca_atrito = forcaAtrito(var_coeficiente_atrito, var_forca_normal)

        print(f'A força de atrito é de {var_forca_atrito:.2f}N (Newtons).')
    elif var_choice == 'Força Elástica': 
        var_cons_elastica_mola = float(input('Digite a constante elástica da mola (em newtons por metro): '))
        var_deformacao_mola = float(input('Digite a deformação da mola (em metros): '))

        var_forca_elastica = forcaElastica(var_cons_elastica_mola, var_deformacao_mola)

        print(f'A força elástica é de {var_forca_elastica:.2f}N (Newtons).')
    else: 
        print('Error002: unexpected_value!')
elif var_choice == 'Não': 
    print('Ok, saindo!')
else: 
    print('Error001: null_value or invalid_value!')