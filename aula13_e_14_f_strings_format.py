nome = 'JP'
altura = 1.73
peso = 136
imc = peso / (altura * altura)
valor = 1500.5658


print(f'{nome} tem {altura} de altura, pesa {peso} quilos e o seu IMC é {imc}')
print(f'Exemplo de limitação de casas decimais: {imc:.2f}')
print(f'Exemplo de valor separado por virgula na formatação: {valor:,.2f}')

# Parametro posicional
a = 'A'
b = 'B'
c = 1.1
string = 'a={} b={} c={:.2f}'
# USANDO VALOR INDEX -> string = 'a={0} b={1} c={2:.2f}'
formato = string.format(a, b, c)

# Parametro nomeado
d = 'D'
e = 'E'
f = 2.2
string = 'd={nome1} e={nome2} f={nome3:.2f}'
formato2 = string.format(nome1=d, nome2=e, nome3=f)

print(formato)
print(formato2)
