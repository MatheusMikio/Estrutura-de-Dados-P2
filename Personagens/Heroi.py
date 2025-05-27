#Classe base para os heróis do jogo.
import random
from Habilidades import habilidadesHeroi
from historia.historia import narrar

class Personagem:
    def __init__(self, nome : str, habilidades : list):
        self.nome = nome
        self.vida = 100
        self.energia = 1
        self.habilidadesPersonagem = habilidades
        self.habilidades = []
        self.tipo = 0
        self.mao = []

        #Criando uma lista de habilidades com 5 cópias de cada habilidade.
        for habilidade in self.habilidadesPersonagem:
            self.habilidades.extend(
                [habilidade.copy() for _ in range(5)]
            )
        #Embaralha as cartas e distribui a mão inicial
        self.embaralhar()
        
    def embaralhar(self):
        random.shuffle(self.habilidades)
        self.pegarCartas(5)

    def regem(self):
        self.energia +=1


    #Adiciona cartas do baralho para a mão do personagem.
    def pegarCartas(self, quantidade : int = 1):
        if len(self.mao) >= 5:
            print("Você não pode pegar mais cartas (Maximo de 5 cartas na mão).")
            return

        for _ in range(quantidade):
            if len(self.habilidades) == 0:
                print("Você não possui mais cartas disponíveis")
                return
            self.mao.append(self.habilidades.pop())

    def atacar(self, alvo, numeroHabilidade : int): 
        if not self.mao:
            print("Você não possui cartas disponíveis")
            return
        
        if numeroHabilidade < 1 or numeroHabilidade > len(self.mao):
            narrar("Você tentou utilizar uma habilidade desconhecida ate por si mesmo, mas não deu certo .")
            return 

        # Executa o ataque se tiver energia suficiente
        if self.energia >= self.mao[numeroHabilidade-1]["custo"]:
            alvo.vida -= self.mao[numeroHabilidade-1]["dano"]
            self.energia -= self.mao[numeroHabilidade-1]["custo"]
            cartaUsada = self.mao.pop(numeroHabilidade - 1)

            print(f"{self.nome} atacou {alvo.nome} com {cartaUsada['nome']} e causou {cartaUsada['dano']} de dano.")

            if alvo.vida <= 0:
                print(f"{alvo.nome} foi derrotado!")
        else:
            print("Você não possui energia suficiente para usar essa carta.")
    
    def mostrarCartas(self):
        for index, carta in enumerate(self.mao):
            print(f"{index + 1} - {carta['nome']}: Dano: {carta['dano']}, Custo: {carta['custo']}")

    #Usado para resetar o personagem depois de finalizar o combate.
    def resetarPersonagem(self):
        self.vida = 100
        self.energia = 1
        self.mao = []
        self.habilidades = []
        for habilidade in self.habilidadesPersonagem:
            self.habilidades.extend(
                [habilidade.copy() for _ in range(5)]
            )
        self.embaralhar()