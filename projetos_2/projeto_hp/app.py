def horsePower(rpm, torque): 
    var_hp = (rpm * torque) / 5252 
    return var_hp

var_choice = input('Deseja calcular os cavalos de potência do seu carro? Sim? ou Não? ')

if var_choice == 'Sim': 
    var_rpm = float(input('Digite o rpm do seu carro: '))
    var_torque = float(input('Digite a quantidade de torque do seu carro: '))

    var_hp = horsePower(var_rpm, var_torque)

    print(f'Seu carro tem {var_hp:.2f}HP')
elif var_choice == 'Não': 
    print('Ok, saindo!')
else: 
    print('Error001: null_value or invalid_value!')