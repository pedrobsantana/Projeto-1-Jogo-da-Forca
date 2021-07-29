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
    palavraMaiuscula = palavra.upper()
    listaPalavra = [letra for letra in palavraMaiuscula]
    for letra in listaPalavra:
        if letra not in letrasEscolhidas:
            listaPalavra[listaPalavra.index(letra)] = "__"
    return " ".join(listaPalavra)

# função para verificar se a letra inserida existe na palavra ou não
def verificaAcerto (letrasEscolhidas, palavra):
    palavraMaiuscula = palavra.upper()
    listaPalavra = [letra for letra in palavraMaiuscula]
    for letra in listaPalavra:
        if letra not in letrasEscolhidas:
            return False
    else:
        return True
    
palavrasPossiveis = ["DIEGO ALVES", "RAFINHA", "RODRIO CAIO", "PABLO MARI", "FILIPE LUIS", "WILLIAM ARAO", "GERSON",
                     "EVERTON RIBEIRO", "DE ARRASCAETA", "BRUNO HENRIQUE", "GABIGOL", "JORGE JESUS", "MULAMBO", "FAVELA",
                     "URUBINHA", "MISTER", "DIEGO", "LUCAS PAQUETA", "VINICIUS JUNIOR", "OBINA", "HERNANE BROCADOR",
                     "PEDRO", "MANTO SAGRADO", "O MAIS QUERIDO", "URUBU", "RAUL PLASSMANN", "LEANDRO", "MARINHO",
                     "MOZER", "JUNIOR", "ANDRADE", "ADILIO", "ZICO", "TITA", "NUNES", "LICO", "CARPEGIANI", "RONDINELLI",
                     "FESTA NA FAVELA", "MAIOR DO MUNDO"]

listaFrases = {"OBINA":"Ôôôôôô Obina é melhor que Eto´o! Obina é melhor que Eto´o!",
               "GABIGOL": "Pode levantar a plaquinha porque hoje tem GOL do GABIGOL!",
               "HERNANE BROCADOR": "Uh terror, o Hernane é BROCADOR!", 
               "GERSON": "Tá difícil de parar os coringa do Flamengo. Vapo!",
               "FESTA NA FAVELA": "Favelaaaa, favelaaaa...FESTA NA FAVELA!",
               "MISTER": "Miiiiiister! Miiiister!! Miiiiister!!!"
              }

# se a palavra sorteada estiver presente no dicionário, caso o usuário saia vitorioso, aparece uma frase especial
def menu():
    palavra = palavrasPossiveis[random.randint(0, len(palavrasPossiveis))]
    letrasEscolhidas = [" "]
    erro = 0
    print("*******************************************")
    print("************ FORCA RUBRO-NEGRA ************")
    print("*******************************************")
    print("******** BONDE DO MENGÃO SEM FREIO ********")
    print("*******************************************")
    print("**************F*L*A*M*E*N*G*O**************")
    print()
    
    opt = input("Qual o maior time do mundo?\nPara encerrar, digite 2. ")  
    opt = opt.upper()
    
    if opt == "2":
        print("Jogo encerrado.")
        os._exit(1)
    
    elif opt == "FLAMENGO" or opt == "FLA" or opt == "MENGO":
        while erro <7:
            print(mostraPalavra(letrasEscolhidas, palavra))
            if verificaAcerto(letrasEscolhidas,palavra):
                if palavra in listaFrases:
                    print()
                    print(listaFrases[palavra])
                    print("\nSaudações Rubro Negras! Que tal mais uma partida?\n")
                    menu()
                else: 
                    print()
                    print("Golaço! Gol de placa! Você acertou a palavra.")
                    print()
                    print("Saudações Rubro Negras! Que tal mais uma partida?")
                    print()
                    menu()
                    
            novaLetra = pedeLetra(letrasEscolhidas).upper()
            letrasEscolhidas.append(novaLetra)
            if testaLetra(novaLetra, palavra):
                print("Letra digitada: ", novaLetra)
                print("Boa! Vai pra cima deles Mengo!\n")
            else:
                print("Letra digitada: ", novaLetra)
                print("Na traaaaave!!\n")
                erro += 1
                desenhaBoneco(erro)
        print("Chupa que é de uva! Perdeu, trouxa.")
        print()
        print("A palavra correta era...")
        print()
        print(palavra)
        print()
        print("Jogou como nunca e perdeu como sempre! Que tal mais uma partida?\n")
        print()
        menu()
               
    elif opt == "VASCO" or opt == "FLUMINENSE" or opt == "BOTAFOGO" or opt == "CORINTHIANS" or opt == "PALMEIRAS":
        print()
        print("Amigão, eu to falando de time GRANDE e não de time rebaixado né!? Vai, tenta de novo.")
        print()
        menu()
        
    while opt != "FLAMENGO":
        print()
        print("Esse aí é timinho né!? Vai, tenta de novo.")
        print()
        menu()
        
menu()