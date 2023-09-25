def mediaSimples(num1, num2):
    var_media = (num1 + num2) / 2
    return var_media

def mediaPonderada(cas1, num1, cas2, num2):
    var_media_ponderada = ((cas1 * num1) + (cas2 * num2)) / (cas1 + cas2)
    return var_media_ponderada

var_choice = input('Deseja descobrir a média de algo? Sim? ou Não? ').strip()

if var_choice.lower() == 'sim': 
    var_choice = input('Qual média deseja utilizar? Simples? ou Ponderada? ').strip()

    if var_choice.lower() == 'simples': 
        var_num = float(input('Digite o primeiro valor: ').strip())
        var_num_2 = float(input('Digite o segundo valor: ').strip())

        var_media = mediaSimples(var_num, var_num_2)

        print(f'A média dos valores {var_num} e {var_num_2} é de {var_media:.2f}')
    elif var_choice.lower() == 'ponderada': 
        var_num = float(input('Digite o primeiro valor: ').strip())
        var_cas = float(input('Digite a frequência do primeiro valor: ').strip())
        var_num_2 = float(input('Digite o segundo valor: ').strip())
        var_cas_2 = float(input('Digite a frequência do segundo valor: ').strip())

        var_media = mediaPonderada(var_cas, var_num, var_cas_2, var_num_2)

        print(f'A média ponderada dos valores {var_num} de {var_cas} e {var_num_2} de {var_cas_2}, é de {var_media:.2f}')
    else:
        print('Error002: unexpected_value!')
elif var_choice.lower() == 'não':
    print('Ok, saindo!')
else:
    print('Error001: null_value or invalid_value!')