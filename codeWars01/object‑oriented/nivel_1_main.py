from ast import Continue
from time import sleep
from robo import Labirinto
from robo import Robo


def main():
    POSICAO_INICIAL = [4, 8]
    robo1 = Robo("THE ROBOT")
    labirinto1 = Labirinto()
    

    labirinto1.LABIRINTO[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]] = robo1.ROBO

    labirinto1.print_labirinto()

    POSICAO_ATUAL = POSICAO_INICIAL

    Tentativas = []
              
    while POSICAO_ATUAL != labirinto1.SAIDA:
        if robo1.verifica_movimento(POSICAO_ATUAL, robo1.CIMA) :
            Tentativas.append(robo1.CIMA)
            POSICAO_ATUAL = robo1.movimento(POSICAO_ATUAL, robo1.CIMA)
            labirinto1.print_labirinto()
            sleep(1)
        
        elif robo1.verifica_movimento(POSICAO_ATUAL, robo1.BAIXO):
            Tentativas.append(robo1.BAIXO)
            POSICAO_ATUAL = robo1.movimento(POSICAO_ATUAL, robo1.BAIXO)
            labirinto1.print_labirinto()
            sleep(1)
        
        elif robo1.verifica_movimento(POSICAO_ATUAL, robo1.ESQUERDA):
            Tentativas.append(robo1.ESQUERDA)
            POSICAO_ATUAL = robo1.movimento(POSICAO_ATUAL, robo1.ESQUERDA)
            labirinto1.print_labirinto()
            sleep(1)

        elif robo1.verifica_movimento(POSICAO_ATUAL, robo1.DIREITA):
            Tentativas.append(robo1.DIREITA)
            POSICAO_ATUAL = robo1.movimento(POSICAO_ATUAL, robo1.DIREITA)
            labirinto1.print_labirinto()
            sleep(1)
        else:
            movimento_anterior = Tentativas[len(Tentativas)-1]
            POSICAO_ATUAL = robo1.movimento_voltar(POSICAO_ATUAL,[movimento_anterior[0],movimento_anterior[1]])
            Tentativas.remove(movimento_anterior)
            labirinto1.print_labirinto()
            sleep(1)
            Continue

if __name__ == "__main__":
    main()