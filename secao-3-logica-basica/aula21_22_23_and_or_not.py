# AND

# entrada = input('[E]ntrar [S]air: ')
# senha = input('Senha: ')

# senha_correta = '123456'

# if entrada == 'E' and senha == senha_correta:
#     print('Entrar')
# else:
#     print('Sair')


# OR
entrada = input('[E]ntrar [S]air: ')
senha = input('Senha: ')

senha_correta = '123456'

if (entrada == 'E' or entrada == 'e') and senha == senha_correta:
    print('Entrar')
else:
    print('Sair')


password = input('Senha: ') or 'Sem senha'
print(password)


# NOT (inverte valores)

print(not True) #False
print(not False) #True
print(not 1) #False