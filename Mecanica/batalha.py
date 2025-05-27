from Mecanica.turno import Turno
import random
from historia.historia import narrar

def combate(heroisCriados,inimigos,chefe :int = 0):
    #criando variaveis
    rodadas = 1
    sequencia = set()
    duelo = True
    posicaoinimigo =set()
    turno = Turno()
    qtdIni = 0
    qtdHeroi = 0
    j=0

    #contagem de herois no turno
    for heroi in heroisCriados:
        qtdHeroi += 1
        sequencia.add(heroi)
    
    #contagem de inimigos no turno
    for inimigo in inimigos:
        qtdIni += 1
        sequencia.add(inimigo)
    if chefe == 0:
        narrar("--Apareceu "+ str(qtdIni) + " inimigo(s)-----")
    else:
        narrar("Valdrak Apareceu essa sera a ultima batalha cuidado!!") 
        narrar("--Apareceu mais "+ str(qtdIni-1) + " inimigo(s) com Valdrak-----")
        


    #encadeando os participantes do duelo
    for s in sequencia:
        turno.append(s)

    for i in range(len(turno)):
        if turno[i].tipo == 1:
            posicaoinimigo.add(i)

    
    input("-press any key-")
    narrar("Inicio de combate, Turno 1:",0.02)
    # incio do duelo em turnos
    while(duelo):
        p=0
        if turno[j].vida > 0:
            #Turno do inimigo
            if turno[j].tipo == 1:
                narrar("Turno do: "+ turno[j].nome,0.02)                
                input()
                atacado = random.randint(0,len(turno)-1)
                if turno[atacado].tipo == 1:
                    print("inimigo Errou o ataque")
                else:
                    if turno[j].chefe == 0:
                        turno[j].atacar(turno[atacado])
                    else:
                        habilidade = random.randint(1,4)
                        turno[j].atacar(turno[atacado],habilidade)
                    if turno[atacado].vida < 0:
                        qtdHeroi-=1
                        if qtdHeroi == 0:
                            duelo = False
                input()
            else:
                #Turno do Heroi
                narrar("Turno do heroi:"+turno[j].nome,0.02)
                narrar("Vida:"+ str(turno[j].vida),0.02)
                narrar("Energia:"+ str(turno[j].energia),0.02)
                narrar("Escolha uma habilidade: ",0.02)
                turno[j].mostrarCartas()
                print("0 - Passar turno")
                opcao = int(input())
                if opcao == 0:
                    turno[j].regem()
                else:
                    narrar("Escolha o inimigos",0.02)
                    for p in range(len(turno)):
                        if turno[p].tipo == 1 and turno[p].vida > 0:
                            print( str(p) +"-" +turno[p].nome +" Vida:" +str(turno[p].vida))
                    opcaoInimigos = int(input())
                    turno[j].atacar(turno[opcaoInimigos],opcao)
                    if turno[opcaoInimigos].vida <= 0:
                        qtdIni -= 1
                        if qtdIni == 0:
                            duelo = False
                turno[j].pegarCartas()

            if len(turno)-1 == j:
                rodadas += 1
                j = 0
                narrar("Turno:"+ str(rodadas),0.02)
                input()
            j+=1
        else:
            j+=1
            
    #resetar os personagens

    