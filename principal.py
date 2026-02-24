#*******************************************************************************
#Autor: Vivian Martins Moura
#Componente Curricular: MI Algoritmos
#Concluido em: 30/04/2025
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************
from defvariavel import *
import time
#Criação da matriz com todas as células mortas inicialmente
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(mortas)
    matriz.append(linha)
print('Seja bem-vindo ao jogo da vida!')
#Loop criado para perguntar ao usuário quais células ele quer reviver
while True:
    try:
        vivasresposta=input(f'Quer reviver alguma célula ? digite {sim} para sim e {nao} para não:').lower()
        assert vivasresposta in ['s','n'], 'Digite apenas s ou n'
        break
    except AssertionError as erro:
        print(f'Erro:{erro}')
while vivasresposta!=nao:
        try:
            linhareviver=int(input('Digite qual é a linha da célula que você deseja reviver, de 0 a 9:'))
            colunareviver=int(input('Digite qual é a coluna da célula que você deseja reviver, de 0 a 9:'))
            if 0 <= linhareviver < linhas and 0 <= colunareviver < colunas:
                matriz[linhareviver][colunareviver] = vivas
            else:
                print("Posição inválida.")
        except ValueError:
            print("Erro: Digite apenas números inteiros válidos.")
        try:
            vivasresposta=input(f'Quer reviver alguma célula ? digite {sim} para sim e {nao} para não:').lower()
            assert vivasresposta in ['s','n'], 'Digite apenas s ou n'
        except AssertionError as erro:
            print(f'Erro:{erro}')
            vivasresposta=input(f'Quer reviver alguma célula ? digite {sim} para sim e {nao} para não:').lower()
mostrarmatriz(matriz)
print ('                                                               ')
#Loop criado para o programa rodar até todas as células estarem mortas de novo, como no início
while not todasmortas(matriz):
    for i in range(linhas):
        for j in range(colunas):
            # Verifica as 8 vizinhas(se tá viva ou morta) e armazena a quantidade de células vizinhas vivas
            vizinhas = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if (x == i and y == j) or not (0 <= x < linhas and 0 <= y < colunas):
                        continue
                    if matriz[x][y] == vivas:
                        vizinhas += 1

            # Aplica as regras do jogo
            if matriz[i][j] == vivas:
                if vizinhas < 2 or vizinhas > 3:
                    matriz[i][j] = mortas  #morre
            else:
                if vizinhas == 3:
                    matriz[i][j] = vivas  #revive

    mostrarmatriz(matriz)
    time.sleep(tempo)
    print ('                                                               ')
print('Fim do jogo!')