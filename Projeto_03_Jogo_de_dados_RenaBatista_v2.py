from random import randint
from time import sleep
from operator import itemgetter
# Nº RODADAS
max_rodadas = int(input("Digite o numero de rodadas: "))
vencedores_partida = list()
for i in range (max_rodadas):
        # DICIONÁRIO DE JOGADORES
    valores_do_dado = [randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
    giradas_do_dados = {}
    for j in range(1,5):
        giradas_do_dados[f'jogador{j}'] = valores_do_dado[j-1]
    # LISTA DE JOGADAS POR JOGADOR
    print(15*'-',f"{i+1}º RODADA",15*'-')
    valores = []
    for r,v in giradas_do_dados.items():
        print(f'--> {r} Saiu {v} no dado')
        valores.append(v)
    # LISTA ORDENADA DE JOGADORES
    resultado = sorted(giradas_do_dados.items(), key=itemgetter(1), reverse=True)
    vencedores_rodada = list()
    for k in resultado:
        if k[1] == max(valores_do_dado):
            vencedores_rodada.append(k[0])
        print('Ranking')
        print(f'--> {k[0]} Saiu {k[1]} no dado')
    if len(vencedores_rodada) > 1:
        print('Empate')
    else:
        vencedores_partida.append(vencedores_rodada[0])
# Demostração do campeão
if  vencedores_partida.count('jogador2') < vencedores_partida.count('jogador1') > vencedores_partida.count('jogador3') and vencedores_partida.count('jogador1') > vencedores_partida.count('jogador4'):
    print(' O Grande Campeão foi: jogador1') 
elif vencedores_partida.count('jogador1') < vencedores_partida.count('jogador2') > vencedores_partida.count('jogador3') and vencedores_partida.count('jogador2') > vencedores_partida.count('jogador4'):
    print(' O Grande Campeão foi: jogador2') 
elif  vencedores_partida.count('jogador1') < vencedores_partida.count('jogador3') > vencedores_partida.count('jogador2') and vencedores_partida.count('jogador3') > vencedores_partida.count('jogador4'):
    print(' O Grande Campeão foi: jogador3') 
elif  vencedores_partida.count('jogador1') < vencedores_partida.count('jogador4') > vencedores_partida.count('jogador2') and vencedores_partida.count('jogador4') > vencedores_partida.count('jogador3'):
    print(' O Grande Campeão foi: jogador4')
else:
    print('Empate')     
    
    


    