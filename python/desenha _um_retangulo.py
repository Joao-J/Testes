linha = 6
coluna = 4

for i in range(linha):
    for x in range(coluna):
        t = 'x' if x == 0 or x == coluna - 1 or i == 0 or i == linha - 1 else ' '
        print(t,end = '')
    print('')
