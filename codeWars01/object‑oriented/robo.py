import sys
class Robo():

    def __init__(self, name:str) -> None:
        self.name = name
        self.ROBO = "\033[1;36;40m4\033[0;0m"
        self.CAMINHO_PERCORRIDO = "\033[1;33;40m2\033[0;0m"
        self.ESQUERDA = [0, -1]
        self.DIREITA  = [0, 1]
        self.CIMA     = [-1, 0]
        self.BAIXO    = [1, 0]
    
    def movimento(self, posicao: tuple, direcao: list):
        Labirinto.LABIRINTO[posicao[0]][posicao[1]] = self.CAMINHO_PERCORRIDO
        Labirinto.LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] = self.ROBO
        return [posicao[0] + direcao[0], posicao[1] + direcao[1]]
        
    def movimento_voltar(self, posicao: tuple, direcao: list):
        Labirinto.LABIRINTO[posicao[0]][posicao[1]] = self.CAMINHO_PERCORRIDO
        Labirinto.LABIRINTO[posicao[0] - direcao[0]][posicao[1] - direcao[1]] = self.ROBO
        return [posicao[0] - direcao[0], posicao[1] - direcao[1]]

    def verifica_movimento(self, posicao: tuple, direcao: list) -> bool:
        if Labirinto.LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] == Labirinto.SAIDA:
            print(f"\033[1;32;40m SUCESSO, {self.name} conseguiu sair!!!\033[0m")
            sys.exit()

        return (Labirinto.LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] == Labirinto.CAMINHO_LIVRE) 

class Labirinto:
    LABIRINTO = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
            ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'], 
            ['#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'], 
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#'], 
            ['#', '#', '#', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'], 
            ['#', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#'], 
            ['#', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#'], 
            ['#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', '#'], 
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '\033[1;32;40mS\033[0;0m', '#']
        ]
    PAREDE = '#'
    CAMINHO_LIVRE = ' '
    SAIDA = "\033[1;32;40mS\033[0;0m"

    def __init__(self) -> None:
        
        self.LABIRINTO = Labirinto.LABIRINTO
    
    def print_labirinto(self):
        print("")
        for linha in self.LABIRINTO:
            print("".join(linha))
        print("")