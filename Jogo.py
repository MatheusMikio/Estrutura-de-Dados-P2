from Personagens.Heroi import Personagem
from Personagens.Vampiro import Vampiro
from Personagens.Valdrak import Valdrak
from Habilidades.habilidadesHeroi import ataque1, ataque2, ataque3, ataque4
from time import sleep

#Função para contar a historia
def narrar(texto, delay=0.05):
    for letra in texto:
        print(letra, end="", flush=True)
        sleep(delay)
    print()

habilidades = [ataque1, ataque2, ataque3, ataque4]

HeroisPadrao = set([
    Personagem("Aric Stormblade", habilidades),
    Personagem("Liora Shadowhisper", habilidades),
    Personagem("Thalric Ironforge", habilidades),
    Personagem("Seraphina Brightflame", habilidades)
    ])

VampirosPadrao = set(
    [
        Vampiro("1"),
        Vampiro("2"),
        Vampiro("3")
    ]
)

valdrak = Valdrak()
heroisCriados = set()



while True:
    try:
        print("1 - Jogar")
        print("2 - Criar heroi")
        print("3 - Sair")
        opcao = int(input("Escolha: "))
        match opcao:
            case 1:
                if len(heroisCriados) < 4:
                    print("Nao ha herois suficientes(É necessário 4 personagens), dseja usar os herois padroes?")
                    opcao = input("S/N: ")[0].upper()
                    if opcao == "S":
                        print("Iniciando o jogo...")
                        #Usar heroisPadrao

                    elif opcao == "N":
                        print("Voltando...")
                    else:
                        print("Opcao invalida")
            case 2:
                if len(heroisCriados) >= 4:
                    print("Voce ja criou todos os herois possiveis")
                    break
                nome = input("Nome: ")
                heroisCriados.add(Personagem(nome, habilidades))
                print(f"Heroi {nome} criado com sucesso")
                print("Herois criados: ")
                for heroi in heroisCriados:
                    print(heroi.nome, end="  ")
                print()
                
            case 3:
                print("Saindo...")
                break

            case _:
                print("Opcao invalida")
    except ValueError:
        print("Opcao invalida")