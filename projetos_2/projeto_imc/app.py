def IMC(peso, altura): 
    var_imc = peso / (altura * altura)
    if var_imc < 18.50:
        print(f'Seu IMC é de {var_imc:.2f} (Está abaixo do Peso)')
    elif var_imc >= 18.60 and var_imc <= 24.90:
        print(f'Seu IMC é de {var_imc:.2f} (Peso ideal)')
    elif var_imc >= 25.00 and var_imc <= 29.90:
        print(f'Seu IMC é de {var_imc:.2f} (Levemente acima do peso)')
    elif var_imc >= 30.00 and var_imc <= 34.90:
        print(f'Seu IMC é de {var_imc:.2f} (Obesidade grau I)')  
    elif var_imc >= 35.00 and var_imc <= 39.90:
        print(f'Seu IMC é de {var_imc:.2f} (Obesidade grau II)')
    elif var_imc >= 40.00:
        print(f'Seu IMC é de {var_imc:.2f} (Obesidade grau III)')
    else:
        print('Error002: unexpected_value!')

var_choice = input('Deseja descubrir o seu IMC? Sim? ou Não? ').strip()

if var_choice.lower() == 'sim': 
    var_peso = float(input('Digite seu peso: '))
    var_altura = float(input('Digite sua altura: '))

    var_imc = IMC(var_peso, var_altura)
 
elif var_choice.lower() == 'não':
    print('Ok, saindo!')
else: 
    print('Error001: null_value or invalid_value!')

