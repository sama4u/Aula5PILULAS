def validarSenha(senha):
    if len(senha) < 8:
        return 'Senha invalida, muito curta'
    
    temNumero = False
    temMaiuscula = False
    
    for letra in senha:
        if letra == ' ':
            return 'Senha inválida, não pode conter espaços.'
        if letra >= '0' and letra <= '9':
            temNumero = True
        if letra >= 'A' and letra <= 'Z':
            temMaiuscula = True
            
    if not temNumero:
        return 'Senha inválida, não possui número.'
    
    if not temMaiuscula:
        return 'Senha inválida, não possui maiúscula'
    
    return 'Senha válida'

#main
senha = input('Digite sua senha: ')
print(validarSenha(senha))