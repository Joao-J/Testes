import sys
import os

n_c = 0.0 #numero de casas
v_c = 100000 #valor da casa
dinheiro = 15000000 #dinheiro
n_c = int(dinheiro / v_c) #numero de casas = a quantidade de casas compradas com o dinheiro arrecadado
dinheiro -= n_c * v_c #dinheiro restante é a sobra da compra das casas
aluguel = 450 #valor do aluguel
a_a = 0 #arrecadação do aluguel
c_c = 0 #casas compradas
c_c_t = 0 #casas compradas total
anos = 1 
ano = 0
j = 1
t_p = 0 #total do patrimonio
r_a = 1.79 #reajuste anual da taxa de aluguel

def clear():
    try:
        if sys.platform == 'linux':
            os.system('clear')
        else:
            os.system('cls')
    except:
        print('erro')

def m_m(i):
    print('MÊS ** ' + str(i+1) + ' **')
    igual()
    print('casas compradas: \t' + str( c_c_t ))

def igual():
    print('arrecadado em aluguel: \t {a:.2f}'.format(a = a_a))
    print('numero de casas: \t' + str(int(n_c)))
    print('total de patrimonio: \t {p:.2f}'.format(p = t_p))
    print('total = \t {d:.2f}'.format(d = dinheiro))
    
def m_t():
    print('ANO ** ' +  str(anos) + ' **')
    igual()
    print('casas compradas: \t' + str( c_c_t ))
    print('Reajuste do aluguel: \t {a:.2f} '.format(a=(aluguel + aluguel * r_a_p)))


while True:
    print('CALCULO DE CASA SYSTEM 2.0\n')
    
    ano = int(input('Numero de anos a serem calculados: '))
    
    r_a_p = r_a / 100.00
    
    for i in range(ano * 12):
        
        c_c = int(dinheiro / v_c)
        n_c += c_c
        a_a += n_c * (aluguel +( aluguel * r_a_p))
        dinheiro += a_a
        t_p = ((n_c + c_c) * v_c + dinheiro )
        if ano > 1:
            c_c_t += c_c
            if j == 12:
                r_a_p +=  r_a / 100.00
                m_t()
                anos += 1
                j = 1
                c_c_t = 0
                print()
            else:
                j += 1
        else:
            m_m(i)
            print()
        a_a = 0
        dinheiro -=  c_c * v_c
        
        
            
    input('press any key for continue')
    clear()
