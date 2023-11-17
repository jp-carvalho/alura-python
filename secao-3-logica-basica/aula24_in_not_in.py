#strings são iteráveis pela posição positiva ou negativa:
#positivo:
# 0 1 2 3 4 5
# O t á v i o
#-6-5-4-3-2-1
#negativo

name = 'Otávio'
print(name[2]) # á
print(name[-4])# á 
print(10 * '-')
print('á' in name)
print('á' and 'O' in name)
print(10 * '-')
print('z' not in name)
print('vio' not in name)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')