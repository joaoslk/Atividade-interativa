print("Você está em uma floresta escura. Há dois caminhos à frente.")
print("1. Seguir pelo caminho da direita.")
print("2. Seguir pelo caminho da esquerda.")

escolha = input("Digite 1 ou 2: ")

if escolha == "1":
    print("\nVocê encontra um rio. O que deseja fazer?")
    print("1. Tentar atravessar a nado.")
    print("2. Procurar uma ponte.")

    escolha = input("Digite 1 ou 2: ")

    if escolha == "1":
        print("\nA correnteza está forte e você se afoga. Fim de jogo!")
    else:
        print("\nVocê encontra uma ponte e atravessa em segurança. Parabéns, você sobreviveu!")

elif escolha == "2":
    print("\nVocê entra em uma caverna escura. Você vê algo brilhando.")
    print("1. Se aproximar para investigar.")
    print("2. Ignorar e continuar andando.")

    escolha = input("Digite 1 ou 2: ")

    if escolha == "1":
        print("\nEra um tesouro! Você fica rico. Parabéns!")
    else:
        print("\nUm urso aparece e te ataca. Fim de jogo!")

else:
    print("\nOpção inválida. O jogo terminou.")