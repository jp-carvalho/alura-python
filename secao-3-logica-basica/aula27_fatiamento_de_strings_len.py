# 012345678
# Olá mundo
#-987654321

variavel = 'Olá mundo'
print(variavel[4:])
# omite o index final para ele ir até o fim
# saída: mundo

print(variavel[4:8])
# saída: mund

print(variavel[:5])
# omite o index inicial e vai até o informado
# saída: Olá m

print(variavel[-8:-2])
# saída: lá mun

print(variavel[0:len(variavel):2])
# saída: Oámno

print(variavel[::-1])
# saída: odnum álO

print(variavel[-1:-10:-1])
# saída: odnum álO

variavel2 = 'teste123'
print(len(variavel2))
# saída: 8