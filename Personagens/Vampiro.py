#Classe para os vampiros comuns
class Vampiro:
    def __init__(self, numero):
        self.nome = f"Vampiro Comum {numero}"
        self.vida = 50
        self.ataque = 5
    def atacar(self, alvo):
        alvo.vida -= self.ataque
        print(f"{self.nome} atacou {alvo.nome} e causou {self.ataque} de dano")
            