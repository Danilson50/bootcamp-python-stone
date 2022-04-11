from ast import Continue
from time import sleep


PAREDE = '#'
CAMINHO_LIVRE = ' '
CAMINHO_PERCORRIDO = "2"
ROBO = "4"
SAIDA = "S"

ESQUERDA = [0, -1]
DIREITA  = [0, 1]
CIMA     = [-1, 0]
BAIXO    = [1, 0]

LABIRINTO = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
    ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'], 
    ['#', '#', '#', '#', '#', '#', ' ', ' ', '4', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#'], 
    ['#', '#', '#', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'], 
    ['#', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#'], 
    ['#', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#'], 
    ['#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', '#'], 
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'S', '#']
]


def print_labirinto():
    print("")
    for linha in LABIRINTO:
        print("".join(linha))
    print("")


def movimento(posicao: tuple, direcao: list):
    LABIRINTO[posicao[0]][posicao[1]] = CAMINHO_PERCORRIDO
    LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] = ROBO
    return [posicao[0] + direcao[0], posicao[1] + direcao[1]]
    
def movimento_voltar(posicao: tuple, direcao: list):
    LABIRINTO[posicao[0]][posicao[1]] = CAMINHO_PERCORRIDO
    LABIRINTO[posicao[0] - direcao[0]][posicao[1] - direcao[1]] = ROBO
    return [posicao[0] - direcao[0], posicao[1] - direcao[1]]

def verifica_movimento(posicao: tuple, direcao: list) -> bool:
    if LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] == SAIDA:
        raise print("SUCESSO")

    return (LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] == CAMINHO_LIVRE) 


def main():
    POSICAO_INICIAL = [3, 8]

    LABIRINTO[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]] = ROBO

    print_labirinto()

    POSICAO_ATUAL = POSICAO_INICIAL

    Tentativas = []
              
    while POSICAO_ATUAL != SAIDA:
        if verifica_movimento(POSICAO_ATUAL, CIMA) :
            Tentativas.append(CIMA)
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, CIMA)
            print_labirinto()
            sleep(1)
        
        elif verifica_movimento(POSICAO_ATUAL, BAIXO):
            Tentativas.append(BAIXO)
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, BAIXO)
            print_labirinto()
            sleep(1)
        
        elif verifica_movimento(POSICAO_ATUAL, ESQUERDA):
            Tentativas.append(ESQUERDA)
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, ESQUERDA)
            print_labirinto()
            sleep(1)

        elif verifica_movimento(POSICAO_ATUAL, DIREITA):
            Tentativas.append(DIREITA)
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, DIREITA)
            print_labirinto()
            sleep(1)
        else:
            movimento_anterior = Tentativas[len(Tentativas)-1]
            POSICAO_ATUAL = movimento_voltar(POSICAO_ATUAL,[movimento_anterior[0],movimento_anterior[1]])
            Tentativas.remove(movimento_anterior)
            print_labirinto()
            sleep(1)
            Continue

if __name__ == "__main__":
    main()

