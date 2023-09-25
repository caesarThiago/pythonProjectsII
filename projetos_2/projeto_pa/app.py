def PA_Termo_Geral(primeiro_termo, pos_termo_geral, diferenca_comum): 
    var_termo_geral = primeiro_termo + (pos_termo_geral - 1) * diferenca_comum
    return var_termo_geral

def PA_Termo_Finito(primeiro_termo, enesimo_termo, num_termo): 
    soma_termo = ((primeiro_termo + enesimo_termo) * num_termo) / 2
    return soma_termo

var_choice = input('Deseja descobrir a progressão aritmética? Digite "Sim" ou "Não": ')

if var_choice == 'Sim': 
    var_tipo_termo = input('Qual seria o termo da PA (progressão aritmética)? Digite "Termo Geral" ou "Termo Finito": ')

    if var_tipo_termo == 'Termo Geral': 
        var_primeiro_termo = float(input('Digite o primeiro termo: '))
        var_pos_termo_geral = float(input('Digite a posição do termo geral: '))
        var_diferenca_comum = float(input('Digite a diferença comum: '))

        var_termo_geral = PA_Termo_Geral(var_primeiro_termo, var_pos_termo_geral, var_diferenca_comum)

        print(f'O termo geral da PA é de: {var_termo_geral:.2f}')
    elif var_tipo_termo == 'Termo Finito': 
        var_primeiro_termo = float(input('Digite o primeiro termo: '))
        var_enesimo_termo = float(input('Digite o enésimo termo: '))
        var_num_termo = float(input('Digite o número de termos: '))

        var_termo_finito = PA_Termo_Finito(var_primeiro_termo, var_enesimo_termo, var_num_termo)

        print(f'A soma dos termos da PA é de: {var_termo_finito:.2f}')
    else: 
        print('Error002: Valor inválido!')
elif var_choice == 'Não': 
    print('Ok, Saindo!!')
else: 
    print('Error001: Valor nulo ou inválido!')