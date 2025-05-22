class Personagem:
    def __init__(self, nome : str, habilidades : list):
        self.nome = nome
        self.habilidades = habilidades
        self.vida = 100
        self.energia = 0
    def atacar(self, alvo, numeroHabilidade : int):
        if self.energia >= self.habilidades[numeroHabilidade-1]["custo"]:
            alvo.vida -= self.habilidades[numeroHabilidade-1]["dano"]
            print(f"{self.nome} atacou {alvo.nome} e causou {self.habilidades[habilidade]['dano']} de dano")   