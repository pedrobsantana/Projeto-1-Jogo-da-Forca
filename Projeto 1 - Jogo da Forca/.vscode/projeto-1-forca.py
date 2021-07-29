import random
import os

# função do boneco da forca, com os erros
def desenhaBoneco(qtdErros):
    if qtdErros == 0:
        print(" +---+ ")
        print(" |     ")
        print(" |     ")
        print(" |     ")
        print(" |     ")
        print("--------")
    elif qtdErros == 1:
        print(" +---+ ")
        print(" |   o ")
        print(" |     ")
        print(" |     ")
        print(" |     ")
        print("--------")
    elif qtdErros == 2:
        print(" +---+ ")
        print(" |   o ")
        print(" |   | ")
        print(" |     ")
        print(" |     ")
        print("--------")
    elif qtdErros == 3:
        print(" +---+ ")
        print(" |   o ")
        print(" |  /| ")
        print(" |     ")
        print(" |     ")
        print("--------")
    elif qtdErros == 4:
        print(" +---+ ")
        print(" |   o ")
        print(" |  /|\\")
        print(" |     ")
        print(" |     ")
        print("--------")
    elif qtdErros == 5:
        print(" +---+ ")
        print(" |   o ")
        print(" |  /|\\")
        print(" |   | ")
        print(" |     ")
        print("--------")
    elif qtdErros == 6:
        print(" +---+ ")
        print(" |   o ")
        print(" |  /|\\")
        print(" |   | ")
        print(" |  /  ")
        print("--------")
    elif qtdErros == 7:
        print(" +---+ ")
        print(" |   o ")
        print(" |  /|\\")
        print(" |   | ")
        print(" |  / \\")
        print("--------")

# função com as letras utilizadas, validação para letras repetidas e caracteres inválidos
def pedeLetra(letrasEscolhidas):
    letrasPossiveis = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", 
                  "S", "T", "U", "V", "W", "X", "Y", "Z"]
    print()
    letra = input("Digite a próxima letra: ")
    letra = letra.upper()
    
    while letra in letrasEscolhidas:
        letra = input("Letra repetida. Digite a próxima letra: ")
        letra = letra.upper()
    
    while letra not in letrasPossiveis:
        print("Caracter inválido. Presta atenção, mané! Digite outra letra mané!")
        letra = pedeLetra(letrasEscolhidas)
        
    return letra

# função para testar se a palavra contém a letra inserida
def testaLetra(letra, palavra):
    palavraMaiuscula = palavra.upper()
    listaPalavra = [letra for letra in palavraMaiuscula]
    if letra.upper() in listaPalavra:
        return True
    else:
        return False

# função para mostrar a palavra com o underline ao invés das letras
def mostraPalavra (letrasEscolhidas, palavra):
    # letrasEscolhidas já deve estar em maiúsculas
    palavraMaiuscula = palavra.upper()
    listaPalavra = [letra for letra in palavraMaiuscula]
    for letra in listaPalavra:
        if letra not in letrasEscolhidas:
            listaPalavra[listaPalavra.index(letra)] = "__"
    return " ".join(listaPalavra)

# função para verificar se a letra inserida existe na palavra ou não
def verificaAcerto(letrasEscolhidas, palavra):
    palavraMaiuscula = palavra.upper()
    listaPalavra = [letra for letra in palavraMaiuscula]
    for letra in listaPalavra:
        if letra not in letrasEscolhidas:
            return False
    else:
        return True
    
palavrasPossiveis = ["MULAMBO", "LA BOMBONERA", "FAVELA", "MISTER", "VACINA", "GASOLINA ADITIVADA", "MANTO SAGRADO", "CACETE DE AGULHA", 
                    "QUEROSENE", "PASSARALHO", "AROMASTICK", "ZARALHO", "ESTRADINHA", "FLAMENGO", "AGULHADA", "O MAIS QUERIDO", "LIBERTADORES DA AMERICA", 
                    "FRIGOBAR", "ARRASCAETA", "JAMAL", "DARTH", "DIFUSOR DE AROMAS"]

def menu():
    palavra = palavrasPossiveis[random.randint(0, len(palavrasPossiveis))]
    letrasEscolhidas = [" "]
    erro = 0
    print("***************************************")
    print("************ JOGO DA FORCA ************")
    print("***************************************")
    print("**************** MENU *****************")
    print("***************************************")
    print()
    print("1. Começar novo jogo")
    print("2. Encerrar")
    print()
    opt = input("Digite a opção desejada: ")
    if opt == "1":
        while erro <7:
            print(mostraPalavra(letrasEscolhidas, palavra))
            if verificaAcerto(letrasEscolhidas, palavra):
                print()
                print("É TEEETRA! É TEEETRA! Você acertou a palavra!")
                print()
                print("Sabemos que foi sorte né!? Que tal mais uma partida?")
                print()
                menu()
            novaLetra = pedeLetra(letrasEscolhidas).upper()
            letrasEscolhidas.append(novaLetra)
            if testaLetra(novaLetra, palavra):
                print("Letra digitada:", novaLetra)
                print("Boa, meu filho!\n")
            else:
                print("Letra digitada: ", novaLetra)
                print("Na traaaaave! Errou filhão!\n")
                erro += 1
                desenhaBoneco(erro)
        print("Chupa que é de uva! Perdeu, trouxa.")
        print()
        print("A palavra correta era...")
        print()
        print(palavra)
        print()
        print("Jogou como nunca e perdeu como sempre! Que tal mais uma partida?")
        print()
        menu()

    if opt == "2":
        print("Jogo encerrado.")
        os._exit(1)

            
    else:
        print("Opção inválida. Digite 1 para jogar ou 2 para encerrar: ")
        menu()

menu()