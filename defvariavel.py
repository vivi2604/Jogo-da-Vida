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
#criação de variável
linhas = 10
colunas = 10
sim='s'
nao='n'
mortas='X'
matriz=[]
vizinhasvivas=0
tempo=5
vivas='O'
#Criação de uma função para verificar se todas as células estão mortas
def todasmortas(matriz):
    for linha in matriz:
        for celula in linha:
            if celula != 'X':
                return False
    return True
#Criação de uma função para printar a matriz
def mostrarmatriz(matriz):
    for l in range(len(matriz)):
        for c in range(len(matriz[0])):
            print(f"[{matriz[l][c]}]", end=' ')
        print()