from collections import deque
from time import sleep

#Função para contar a historia
def narrar(texto, delay=0.05):
    for letra in texto:
        print(letra, end="", flush=True)
        sleep(delay)
    print()

def criarHistoria():

    # Capítulo 1
    capitulo1 = "Capítulo 1 - Sob o luar sanguíneo, a vila de Eldermere acorda com gritos. Casas estão marcadas com símbolos antigos pintados em sangue seco, o cheiro de terra úmida misturado com ferro, enquanto sombras se movem nos telhados. Os aldeões sussurram sobre figuras pálidas que visitam suas casas à noite, deixando apenas corpos esvaziados e crianças desaparecidas, heróis que estavam de passagem aparecem e enfrentam os vampiros."

    precombate1 = "Inimigos estão se aproximando!!"

    combate = 1

    endCap1= "Entre os pertences de um servo derrotado, encontram um pergaminho manchado com o selo do Conde Valdrak, senhor dos vampiros, e um mapa marcando seu covil nas montanhas sombrias."

    # Capítulo 2
    capitulo2 = "Capítulo 2 - A trilha para as montanhas sombrias é ladeada por árvores retorcidas. O vento carrega sussurros em línguas esquecidas. O castelo do Conde Valdrak surge no horizonte, suas torres perfurando as nuvens como presas, as paredes parecem respirar, pulsando com uma energia maligna. Nos salões decadentes do castelo, o grupo encontra o próprio Conde Valdrak."

    precombate2 = "Inimigo está se aproximando!!"

    combate = 1

    endCap2 = "Com o vampiro temporariamente derrotado, os heróis encontram um antigo tomo revelando a única fraqueza do Conde: um artefato sagrado escondido nas catacumbas abaixo da catedral abandonada."

    # Capítulo 3
    capitulo3 = "Capítulo - 3 A catedral em ruínas guarda segredos antigos. Vitrais quebrados projetam padrões de luz manchada no chão de mármore rachado. Um silêncio sepulcral paira no ar, interrompido apenas pelo rangido das madeiras antigas e o sussurro do vento através das frestas. " \
    " Na cripta profunda, o Conde Valdrak revela sua verdadeira forma - uma criatura de pura escuridão com asas membranosas."

    precombateFinal = "Prepare - se, essa é a última batalha!!"

    combateFinal = 2

    endCap3 = "O artefato emana uma aura celestial, banhando a câmara em clarões que afastam as sombras. Quando a estaca de prata encontra seu alvo, um urro bestial rasga a noite. As primeiras luzes da aurora iluminam Eldermere, dissipando séculos de escuridão como se fossem apenas pesadelos ao amanhecer."

    eventos = deque([capitulo1, precombate1, combate, endCap1, capitulo2, precombate2, combate, endCap2, capitulo3, precombateFinal, combateFinal, endCap3])
    
    historia = (eventos)

    return historia