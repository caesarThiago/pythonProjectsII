def periodoUniversal (const_proporcionalidade, raio_medio): 
    var_periodo_planeta = const_proporcionalidade * raio_medio
    return var_periodo_planeta

def forçaGravitacional (const_gravitacao_universal, massa_corpo_1, massa_corpo_2, distancia):
    var_forca_gravitacional = (const_gravitacao_universal * massa_corpo_1 * massa_corpo_2) / distancia
    return var_forca_gravitacional

var_choice = input('Deseja utilizar alguma formula de gravitação universal? Sim? ou Não? ')

if var_choice == 'Sim': 
    var_choice = input('Deseja descobrir o Periodo Universal? ou Força Gravitacional? ')
    if var_choice == 'Periodo Universal': 
        var_const_proporcionalidade = float(input('Digite a constante de proporcionalidade: '))
        var_raio_medio = float(input('Digite o raio médio (em raios cúbicos): '))

        var_periodo_planeta = periodoUniversal(var_const_proporcionalidade, var_raio_medio)
        print(f'O periodo universal é de {var_periodo_planeta:.2f} (ao quadrado)')
    elif var_choice == 'Força Gravitacional': 
        var_const_gravitacao_universal = float(input('Digite a constante de gravitação universal: '))
        var_massa_corpo_1 = float('Digite a massa do primeiro corpo: ')
        var_massa_corpo_2 = float('Digite a massa do segundo corpo: ')
        var_distancia = float('Digite a distância: ')

        var_forca_gravitacional = forçaGravitacional(var_const_gravitacao_universal, var_massa_corpo_1, var_massa_corpo_2, var_distancia)
        print(f'A força gravitacional é de: {var_forca_gravitacional:.2f}')
    else: 
        print('Error002: unexpected_value!')
elif var_choice == 'Não': 
    print('Ok, saindo!')
else: 
    print('Error001: null_value or invalid_value!')