print("Você está em uma basilica escura. Há dois caminhos à frente.")
print("1. Seguir pelo caminho da direita.")
print("2. Seguir pelo caminho da esquerda.")

escolha = input("Digite 1 ou 2: ")

if escolha == "1":
    print("\nVocê encontra um objeto mistico. O que deseja fazer?")
    print("1. pegar o abjeto.")
    print("2. seguir em frente.")

    escolha = input("Digite 1 ou 2: ")

    if escolha == "1":
        print("\num ser mistico sai do abjeto")
    else:
        print("\nnada acontecera")

elif escolha == "2":
    print("\nvoce recebera um desejo ")
    print("1. qual pedido voce fara")
    print("2. Ignorar o ser mistico e continuar andando.")

    escolha = input("Digite 1 ou 2: ")

    if escolha == "1":
        print("\nseu desejo e se tornar rico")
    else:
        print("\nvoce segue a sua vida monotona")

else:
    print("\nOpção inválida. O jogo terminou.")
