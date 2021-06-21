import random


opcoes = ["pedra", "papel", "tesoura"]

pontos_do_computador = 0
pontos_do_jogador = 0

print(" Bem Vindo ao Jogo JOkenPOHHH !!!!! Escolha uma das opçoes : Pedra, papel e tesoura\n\n")
jogada_do_jogador = ""

while jogada_do_jogador.lower() != "sair":
    jogada_do_jogador = input("Qual a sua jogada?")
    if jogada_do_jogador in opcoes:
        jogada_do_computador = random.choice(opcoes)
        print(f"Computador jogou: {jogada_do_computador}\n")

        # pedra irá ganhar tesoura
        if jogada_do_jogador == "pedra" and jogada_do_computador == "tesoura":
            print("Jogador ganhou!")
            pontos_do_jogador = pontos_do_jogador + 1
        elif jogada_do_computador == "pedra" and jogada_do_jogador == "tesoura":
            print("Computador ganhou!")
            pontos_do_computador = pontos_do_computador + 1
        
        # tesoura irá ganha de papel
        if jogada_do_jogador == "tesoura" and jogada_do_computador == "papel":
            print("Jogador ganhou!")
            pontos_do_jogador = pontos_do_jogador + 1
        elif jogada_do_computador == "tesoura" and jogada_do_jogador == "papel":
            print("Computador ganhou!")
            pontos_do_computador = pontos_do_computador + 1

        # papel irá ganha de pedra        
        if jogada_do_jogador == "papel" and jogada_do_computador == "pedra":
            print(" Jogador ganhou!")
            pontos_do_jogador = pontos_do_jogador + 1
        elif jogada_do_computador == "papel" and jogada_do_jogador == "pedra":
            print("Computador ganhou!")
            pontos_do_computador = pontos_do_computador + 1

        print(f"\n\njogador {pontos_do_jogador} x {pontos_do_computador} Computador")
    elif jogada_do_jogador.lower() != "sair":
        print(f"Escolha uma das opções: {opcoes}")
                
                
      