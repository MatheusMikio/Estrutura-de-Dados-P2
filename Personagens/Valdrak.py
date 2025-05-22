#Classe para o chefe final
class Valdrak:
    def __init__(self):
        self.nome = "Valdrak"
        self.vida = 250
        self.habilidades = {
            "1" :{
                "nome" : "Garra",
                "dano" : 10,
            },
            "2" :{
                "nome" : "Grito Apavorante",
                "dano" : 20,
            },
            "3" :{
                "nome" : "Bola de Fogo",
                "dano" : 30,
            },
            "4" :{
                "nome" : "Abraço da Morte",
                "dano" : 40,
            },
        }
    
    def atacar(self, alvo, numeroHabilidade : int):
        alvo.vida -= self.habilidades[numeroHabilidade]["dano"]