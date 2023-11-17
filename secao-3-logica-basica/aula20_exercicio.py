primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

prim = int(primeiro_valor)
seg = int(segundo_valor)


if prim > seg:
    print(f'{prim=} é maior que {seg=}')
elif seg > prim:
    print(f'{seg=} é maior que {prim=}')
else:
    print('Os valores são iguais')