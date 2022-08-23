# Um dos esportes favoritos na Robolandia e o Rali dos Robos. Este rali e praticado em uma arena retangular gigante de N linhas
# por M colunas de celulas quadradas. Algumas das celulas estao vazias, algumas contem figurinhas da Copa (muito apreciadas pelas
# inteligencias artificiais da Robolandia) e algumas sao ocupadas por pilastras que sustentam o teto da arena. Em seu percurso os
# robos podem ocupar qualquer celula da arena, exceto as que contem pilastras, que bloqueiam o seu movimento. O percurso do robo na
# arena durante o rali e determinado por uma sequencia de instrucoes. Cada instrucao e representada por um dos seguintes caracteres:
# 'D', 'E' e 'F', significando, respectivamente, 'gire 90 graus para a direita', 'gire 90 graus para a esquerda' e 'ande uma celula
# para a frente'. O robo comeca o rali em uma posicao inicial na arena e segue fielmente a sequencia de instrucoes dada (afinal, eles
# sao robos!). Sempre que o robo ocupa uma celula que contem uma figurinha da Copa ele a coleta. As figurinhas da Copa nao sao repostas,
# ou seja, cada figurinha pode ser coletada uma única vez. Quando um robo tenta andar para uma celula onde existe uma pilastra ele
# patina, permanecendo na celula onde estava, com a mesma orientacao. O mesmo tambem acontece quando um robo tenta sair da arena.
# Dados o mapa da arena, descrevendo a posicao de pilastras e figurinhas, e a sequencia de instrucoes de um robo, voce deve escrever um
# programa para determinar o número de figurinhas coletadas pelo robo.
# A entrada contem uma matriz representando a arena e uma lista com as instrucoes do robo. Cada elemento na matriz pode conter um dos
# seguintes caracteres:

# "." -> celula normal;
# "*" -> celula que contem uma figurinha da Copa;
# "#" -> celula que contem uma pilastra;
# "N", "S", "L", "O" -> celula onde  o robo inicia o percurso (unica na arena). A letra representa a orientacao inicial do robo (Norte,
# Sul, Leste, Oeste, respectivamente). A lista de entrada contem uma sequencia de S caracteres dentre 'D', 'E' e 'F', representando as
# instrucoes do robo.

def imprimirArena(arena):
    print("||", "===" * len(arena), "||")
    for linha in arena:
        print("||", end="  ")
        for elemento in linha:
            print(elemento, end="  ")
        print("||")
    print("||", "===" * len(arena), "||")

def ocorrencias(lista, elementoDesejado):
    ocorrencia = 0
    for elemento in lista:
        if elemento == elementoDesejado:
            ocorrencia += 1
    return ocorrencia

def roboColecionador(arena, comandos):
    orientacao = ["N","L","S","O"]
    figurinhasTotais = 0
    figurinhasRestantes = 0

    print("Arena a ser usada: ")
    imprimirArena(arena)

    #% Posicao Inicial da Peca
    for linha in arena: 
        for coluna in linha:
            if (coluna != ".") and (coluna != "*") and (coluna != "#"):
                posicaoY = arena.index(linha)
                posicaoX = linha.index(coluna)
                indice = orientacao.index(coluna)

    #% Figurinhas Totais na Arena
    for linha in arena:
        figurinhasTotais += ocorrencias(linha, "*")

    #% Definicao da Orientacao
    for comando in comandos:
        print(f"\nComando inserido = {comando}")
        if comando == 'D':
            indice += 1
            arena[posicaoY][posicaoX] = orientacao[indice]
        elif comando == 'E':
            indice -= 1
            arena[posicaoY][posicaoX] = orientacao[indice]

        #% Validacao/Movimentacao da Peca
        if comando == "F":
            if indice % 4 == 0:
                if posicaoY - 1 in range(len(arena)) and posicaoX in range(len(arena)):
                    if arena[posicaoY - 1][posicaoX] != "#":
                        arena[posicaoY][posicaoX], arena[posicaoY - 1][posicaoX] = ".", orientacao[indice]
                        posicaoY -= 1
            elif indice % 4 == 1:
                if posicaoY in range(len(arena)) and posicaoX + 1 in range(len(arena)):
                    if arena[posicaoY][posicaoX + 1] != "#":
                        arena[posicaoY][posicaoX], arena[posicaoY][posicaoX + 1] = ".", orientacao[indice]
                        posicaoX += 1
            elif indice % 4 == 2:
                if posicaoY + 1 in range(len(arena)) and posicaoX in range(len(arena)):
                    if arena[posicaoY + 1][posicaoX] != "#":
                        arena[posicaoY][posicaoX], arena[posicaoY + 1][posicaoX] = ".", orientacao[indice]
                        posicaoY += 1
            elif indice % 4 == 3:
                if posicaoY in range(len(arena)) and posicaoX - 1 in range(len(arena)):
                    if arena[posicaoY][posicaoX - 1] != "#":
                        arena[posicaoY][posicaoX], arena[posicaoY][posicaoX - 1] = ".", orientacao[indice]
                        posicaoX -= 1

        imprimirArena(arena)
    
    #% Figurinhas Restantes na Arena
    for linha in arena:
        figurinhasRestantes += ocorrencias(linha, "*")

    figurinhasColetadas = figurinhasTotais - figurinhasRestantes
    print(f'\nFigurinhas coletadas = {figurinhasColetadas}')


# Alguns casos de teste

# arena1 = [["*","*","*"],["*","N","*"],["*","*","*"]]
# comandos1 = ["D","E"]
# roboColecionador(arena1, comandos1)
# print("\n","=" * 50,"\n")

# arena2 = [[".",".",".","#"],["*","#","O","."],["*",".","*","."],["*",".","#","."]]
# comandos2 = ["F","F","E","F","F"]
# roboColecionador(arena2, comandos2)
# print("\n","=" * 50,"\n")

# arena3 = [[".",".",".",".","*",".",".",".",".","."],[".",".",".",".",".",".",".","*",".","."],[".",".",".",".",".","*",".",".",".","."],[".",".","*",".","#",".",".",".",".","."],[".",".",".","#","N",".","*",".",".","*"],[".",".",".","*",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."]]
# comandos3 = ["F","D","F","F","F","F","F","F","E","E","F","F","F","F","F","F","E","F","D","F"]
# roboColecionador(arena3, comandos3)