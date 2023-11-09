# Ordem de precedência: 
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = 1 + 1 ** 5 + 5
conta_2 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)
print(conta_2)

nome = 'JP'
altura = 1.73
peso = 136
imc = peso / (altura * altura)

print(f'{nome} tem {altura} de altura, pesa {peso} quilos e o seu IMC é {imc}')
