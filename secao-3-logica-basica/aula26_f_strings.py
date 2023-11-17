variavel = 'ABC'
print(f'{variavel}')
# saída: ABC

# total de 10 caracteres a esquerda
print(f'{variavel: >10}.')
# saída:        ABC.
# total de 10 caracteres a esquerda
print(f'{variavel:*>10}.')
# saída: *******ABC.

# total de 10 caracteres a direita
print(f'{variavel:*<10}.')
# saída: ABC*******.

# total de 10 caracteres centralizados
print(f'{variavel:*^10}.')
# saída: ***ABC****.

print(f'{1000.548945:.1f}')
# saída: 1000.5

print(f'{1000.548945:0=+10,.1f}')
# saída: +001,000.5

print(f'O hexadecimal de 1500 é {1500:08x}')
# saída: O hexadecimal de 1500 é 000005dc