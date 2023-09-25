import base64

def encodeBase64(texto): 
    texto_bytes = texto.encode('utf-8')
    texto_encode = base64.b64encode(texto_bytes)
    return texto_encode

def decodeBase64(texto_cripto): 
    texto_bytes = base64.b64decode(texto_cripto)
    texto_decode = texto_bytes.decode('utf-8')
    return texto_decode

var_choice = input('Deseja criptografar um texto utilizando Base64? Sim? ou Não? ')

if var_choice == 'Sim':
    var_texto = input('Digite o texto para ser criptografado: ')
    var_cripto_texto = encodeBase64(var_texto)
    print(f'O texto foi criptografado: {var_cripto_texto}')

    var_choice = input('Deseja descriptografar o texto? Sim? ou Não? ')

    if var_choice == 'Sim': 
        var_decripto_texto = decodeBase64(var_cripto_texto)  
        print(f'O texto foi descriptografado: {var_decripto_texto}')
    elif var_choice == 'Não':
        print('Ok!')
    else:
        print('Error002: unexpected_value!')
    
elif var_choice == 'Não':
    print('Ok, saindo!')
else:
    print('Error001: null_value or invalid_value!')