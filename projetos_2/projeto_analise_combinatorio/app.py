import math

from functions import fatorialNum, principioFundamentalContagem, permutacaoSimples, permutacaoRepeticao, arranjoSimples, arranjoRepeticao, combinacaoSimples, combinacaoRepeticao

var_choice = input('Deseja utilizar alguma formula de Análise Combinátoria? Sim? ou Não? ')

if var_choice.lower() == 'sim': 
    var_choice = input('O que você deseja calcular? (Fatorial / Principio Fundamental da Contagem / Permutação simples / Permutação com repetição / Arranjo simples / Arranjo com repetição / Combinação simples / Combinação com repetição): ')

    if var_choice.lower() == 'fatorial': 
        var_num = int(input('Digite o número que deseja fatorar: '))

        var_fatorial = fatorialNum(var_num)

        print(f'O resultado da fatoração foi de: {var_fatorial}.')
    elif var_choice.lower() == 'principio fundamental da contagem': 
        var_pos = int(input('Digite as possibilidades desse evento: '))
        var_opcoes = int(input('Digite as opções do evento: '))

        var_pfc = principioFundamentalContagem(var_pos, var_opcoes)
        
        print(f'O resultado do principio fundamental da contagem foi de: {var_pfc:.2f}')
    elif var_choice.lower() == 'permutação simples': 
        var_total_evento = int(input('Digite o número total de eventos: '))

        var_ps = permutacaoSimples(var_total_evento)

        print(f'O resultado da permutação simples foi de: {var_ps:.2f}')
    elif var_choice.lower() == 'permutação com repetição': 
        var_total_evento = int(input('Digite o número total de eventos: '))
        var_elementos_repetidos = int(input('Digite o número total de elementos repetidos: '))

        var_pr = permutacaoRepeticao(var_total_evento, var_elementos_repetidos)

        print(f'O resultado da permutação com repetição foi de: {var_pr:.2f}')
    elif var_choice.lower() == 'arranjo simples': 
        var_total_elementos_eventos = int(input('Digite o número total de elementos no evento: '))
        var_total_agrupamentos = int(input('Digite o núemro total de agrupamentos: '))

        var_as = arranjoSimples(var_total_elementos_eventos, var_total_agrupamentos)

        print(f'O resultado do arranjo simples foi de: {var_as:.2f}')
    elif var_choice.lower() == 'arranjo com repetição': 
        var_total_elementos_eventos = int(input('Digite o número total de elementos no evento: '))
        var_total_num_escolhidos = int(input('Digite o núemro total de agrupamentos: '))

        var_ar = arranjoRepeticao(var_total_elementos_eventos, var_total_num_escolhidos)

        print(f'O resultado do arranjo simples foi de: {var_ar:.2f}')
    elif var_choice.lower() == 'combinação simples': 
        var_total_elementos_eventos = int(input('Digite o número de elementos no evento: '))
        var_total_agrupamentos = int(input('Digite o número total de agrupamentos: '))

        var_cs = combinacaoSimples(var_total_elementos_eventos, var_total_agrupamentos)

        print(f'O resultado da combinação simples foi de: {var_cs:.2f}')
    elif var_choice.lower() == 'combinação com repetição': 
        var_total_elementos_eventos = int(input('Digite o número de elementos no evento: '))
        var_total_agrupamentos = int(input('Digite o número total de agrupamentos: '))

        var_cr = combinacaoRepeticao(var_total_elementos_eventos, var_total_agrupamentos)

        print(f'O resultado da combinação com repetição foi de: {var_cr:.2f}')
    else: 
        print('Error002: unexpected_value!')
elif var_choice.lower() == 'não':
    print('Ok, saindo!')
else:
    print('Error001: invalid_choice!')