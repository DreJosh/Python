import forca
import Adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        Adivinhacao.jogar()

# Quando colocamos essa validação o sistema verifica se o main está ativo.
if(__name__ == "__main__"):
    escolhe_jogo()
