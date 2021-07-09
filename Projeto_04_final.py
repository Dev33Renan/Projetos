from datetime import date  # Biblioteca date time
from random import randint

contagem = [] #listas vazia referente a contagem.
eleicao = [] #listas vazia referente 

while True:
    def autorizacao_voto(ano):

    # Nesse trecho do código que faz a verificação da obrigatoriedade do voto.
        idade_atual = date.today().year
        idade = idade_atual - ano
        if idade < 16:
            return 'NEGATIVO'
        elif 16 <= idade < 18 or idade > 70:
            return 'Opicional'
        else:
         return 'Obrigatorio'
         

    def votacao(autorizacao, voto): #verificação se você pode ou não votar
        if autorizacao == 'NEGADO':
            print('Você não poderá votar')
        else:
            contagem_de_votos(voto)
        


    def contagem_de_votos(voto):# faz a contagem de votos da lista de candidatos
        global candidatos
        candidatos = ['Goku', 'Vegita', 'Freeza', 'Branco','Nulo']
        
        for i,v in enumerate(candidatos):
            if voto -1 == i:
                eleicao.append(v)
        
        
        
    def resultados():  # printa resultados
        global candidato_goku, candidato_vegita, candidato_freeza
        for i in candidatos:
            cont = 0 
            contagem.append(i)
            for x,v in enumerate(eleicao):
                if v == i:
                    cont += 1
                
            contagem.append(cont)
        for k,v in enumerate(candidatos):
           if k % 2 == 0:
                print(f'Candidatos: {v}', end= ' ')
        else:
            print(f'Votos: {v}', end= ' ')
            print()    
     
        nascimento = autorizacao_voto(int(input('Qual a sua data de nascimento? ')))
        nascimento = randint(1900,2020)

        if nascimento != 'NEGATIVO':
            print(''' Lista da Candidatos
                [1]- Goku
                [2]- Vegita
                [3]- Freeza
                [4]- Votar em Branco
                [5]- Votar Nulo 
                Escolha uma das Opções a cima
                ''')
        voto = votacao(nascimento,int(input('Digita seu voto: ')))
        voto = votacao (nascimento, randint(1,5))  
    resultados
  
    
