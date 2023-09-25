def machCalc(vel_media_obj, vel_media_som): 
    var_mach = vel_media_obj / vel_media_som
    return var_mach

var_choice = input('Deseja descubrir quantos Mach uma aeronave tem? Sim? ou Não? ')

if var_choice == 'Sim':
    var_vel_media_obj = float(input('Digite a velocidade média relativa do objeto (em metros por segundo): '))
    var_vel_media_som = float(input('Digite a velocidade média do som (em metros por segundo): '))

    var_mach = machCalc(var_vel_media_obj, var_vel_media_som)

    print(f'A velocida da aeronave é de {var_mach:.2f}Ma(MACH)')
elif var_choice == 'Não': 
    print('Ok, saindo!')
else: 
    print('Error001: null_value or invalid_value!')