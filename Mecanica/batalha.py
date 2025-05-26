from Mecanica.Turno import Turno
import random

def combate(heroisCriados,inimigos):
    #criando variaveis
    rodadas = 0
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



    #encadeando os participantes do duelo
    for s in sequencia:
        turno.append(s)

    for i in range(len(turno)):
        if turno[i].tipo == 1:
            posicaoinimigo.add(i)

            
    # incio do duelo em turnos
    print(turno)
    while(duelo):
        p=0
        if turno[j].vida > 0:
                
            #Turno do inimigo
            if turno[j].tipo == 1:
                atacado = random.randint(0,len(turno)-1)
                if turno[atacado].tipo == 1:
                    print("inimigo Errou o ataque")
                else:
                    turno[j].atacar(turno[atacado])
                    if turno[atacado].vida < 0:
                        qtdHeroi-=1
                        if qtdHeroi == 0:
                            duelo = False
            else:
                #Turno do Heroi
                print("Turno do heroi:"+turno[j].nome)
                print("Vida:"+ str(turno[j].vida))
                print("Energia:"+ str(turno[j].energia))
                print("Escolha uma habilidade: ")
                turno[j].mostrarCartas()
                print("0 - Passar turno")
                opcao = int(input())
                if opcao == 0:
                    turno[j].regem()
                else:
                    print("Escolha o inimigos")
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
                print("Turno:"+ str(rodadas))
            j+=1
        else:
            j+=1
            
    #resetar os personagens

    