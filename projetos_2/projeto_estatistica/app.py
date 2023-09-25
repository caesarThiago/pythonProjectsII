import math

def mediaAritmetica(valor_1, valor_2, valor_3, todos_valores):
    var_media_aritmetica = (valor_1 + valor_2 + valor_3) / todos_valores
    return var_media_aritmetica

def variancia(media_aritmetica, dados_serie_1, dados_serie_2, dados_serie_3, tamanho_populacional):
    var_variancia = (math.pow((dados_serie_1 - media_aritmetica), 2) +
                    math.pow((dados_serie_2 - media_aritmetica), 2) +
                    math.pow((dados_serie_3 - media_aritmetica), 2)) / tamanho_populacional
    return var_variancia

def desvioPadrao(variancia):
    var_desvio_padrao = math.sqrt(variancia)
    return var_desvio_padrao

var_choice = input('Deseja utilizar alguma fórmula de estatística? Sim? ou Não?: ')

if var_choice == 'Sim':
    var_formula = input('Qual fórmula deseja usar? (Média Aritmética / Variância / Desvio Padrão): ').lower()

    if var_formula == 'média aritmética':
        var_valor_1 = float(input('Insira o primeiro valor: '))
        var_valor_2 = float(input('Insira o segundo valor: '))
        var_valor_3 = float(input('Insira o terceiro valor: '))
        var_todos_valores = float(input('Insira a quantidade de valores: '))

        var_media = mediaAritmetica(var_valor_1, var_valor_2, var_valor_3, var_todos_valores)
        print(f'A média aritmética é de {var_media:.2f}')

    elif var_formula == 'variância':
        var_media = float(input('Insira a média aritmética: '))
        var_dados_serie_1 = float(input('Insira o primeiro valor da série: '))
        var_dados_serie_2 = float(input('Insira o segundo valor da série: '))
        var_dados_serie_3 = float(input('Insira o terceiro valor da série: '))
        var_tamanho_populacional = float(input('Insira o tamanho populacional: '))

        var_variancia = variancia(var_media, var_dados_serie_1, var_dados_serie_2, var_dados_serie_3, var_tamanho_populacional)
        print(f'A variância é de {var_variancia:.2f}')

    elif var_formula == 'desvio padrão':
        var_variancia = float(input('Insira a variância: '))

        var_desvio = desvioPadrao(var_variancia)
        print(f'O desvio padrão é de {var_desvio:.2f}')

    else:
        print('Error002: unexpected_value!')

elif var_choice == 'Não': 
    print('Ok, saindo!')
else:
    print('Error001: null_value or invalid_value!')