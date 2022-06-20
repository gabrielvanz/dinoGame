from funcoes import limparTela, morreu, salvar 
import pygame
import random
import time

limparTela()
nome = input("Informe o seu nome: ")
email = input("Informe o seu email: ")
try:
    print("\n")
    arquivo = open('arquivoLogs.txt','a')
    arquivo.write(salvar(nome,email))
    arquivo.close()
    
except:
    arquivo = open('arquivoLogs.txt','w')
    arquivo.write(salvar(nome,email))
    arquivo.close()

time.sleep(3)

pygame.init()
largura = 800
altura = 300
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("Dino Game")
gameDisplay = pygame.display.set_mode(tamanho)
gameIcon = pygame.image.load("imagens/icone.ico")
pygameDisplay.set_icon(gameIcon)
clock = pygame.time.Clock()
gameEvents = pygame.event

#Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

def jogo():
    chao = pygame.image.load("imagens/chao.png")
    chaoX = 0
    chaoY = 230
    cactoX = largura
    varCactoX = 0

    nuvem = pygame.image.load("imagens/nuvem.png")
    nuvem = pygame.transform.scale(nuvem, (70,70))

    nuvemAX = 800
    nuvemAY = random.randint(0,130)
    nuvemBX = 900
    nuvemBY = random.randint(0,130)
    nuvemCX = 1000
    nuvemCY = random.randint(0,130)
    
    alturaDino = 70
    larguraDino = 70
    dino1 = pygame.image.load("imagens/dino1.png")
    dino2 = pygame.image.load("imagens/dino2.png")
    dino3 = pygame.image.load("imagens/dino3.png")
    dino1 = pygame.transform.scale(dino1, (larguraDino,alturaDino))
    dino2 = pygame.transform.scale(dino2, (larguraDino,alturaDino))
    dino3 = pygame.transform.scale(dino3, (larguraDino,alturaDino))
    dino = [dino2,dino1,dino2,dino3]

    dinoX = 150
    dinoY = 206

    fpsDino = 0
    fpsPassaro = 0
    gravidade = 0
    pulo = False
        
    cacto = pygame.image.load("imagens/cacto.png")
    cacto = pygame.transform.scale(cacto, (60,60))

    passaro1 = pygame.image.load("imagens/passaro1.png")
    passaro2 = pygame.image.load("imagens/passaro2.png")
    passaro1 = pygame.transform.scale(passaro1, (70,70))
    passaro2 = pygame.transform.scale(passaro2, (70,70))

    passaroX = largura+400
    varPassaroX = 100
    passaroY = random.randint(180,200)
    velocidadePassaro = random.randint(5,8)
    
    puloSound = pygame.mixer.Sound("sons/pulo.wav")
    pontosSound = pygame.mixer.Sound("sons/pontos.wav")

    fonte = pygame.font.Font("freesansbold.ttf", 20)
    pontos = 0

    velocidade = 5
    dificuldade = 40
    jogando = True

    while True:
        # Eventos da tela
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    jogo()
                if pulo == True:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
                        gravidade = -10
                        pygame.mixer.Sound.play(puloSound)

        if jogando==True:           
            gameDisplay.fill(branco)    

            pontos +=1
            pontuacao = fonte.render(f"Score: {pontos}", True, preto)
            gameDisplay.blit(pontuacao, (20, 20))
            if pontos%1000==0:
                pygame.mixer.Sound.play(pontosSound)

            #Chão
            gameDisplay.blit(chao,(chaoX, chaoY))
            gameDisplay.blit(chao,(largura+chaoX, chaoY))
            
            if (chaoX==-largura):
                gameDisplay.blit(chao,(largura+chaoX, chaoY))
                chaoX=0
            chaoX-=velocidade

            #Nuvens
            nuvemAX-=velocidade
            nuvemBX-=velocidade
            nuvemCX-=velocidade
            gameDisplay.blit(nuvem,(nuvemAX,nuvemAY))
            gameDisplay.blit(nuvem,(nuvemBX,nuvemBY))
            gameDisplay.blit(nuvem,(nuvemCX,nuvemCY))
            if nuvemAX<-largura:
                nuvemAX=largura+random.randint(0,70)
                nuvemAY=random.randint(0,120)
            if nuvemBX<-largura:
                nuvemBX=largura+random.randint(70,140)
                nuvemBY=random.randint(0,120)
            if nuvemCX<-largura:
                nuvemCX=largura+random.randint(140,210)
                nuvemCY=random.randint(0,120)

            #Dino
            if dinoY == 206:
                pulo=True
            else:
                pulo=False

            gravidade = gravidade + 0.4
            dinoY+=gravidade
            if dinoY > 206:
                dinoY = 206
            if pulo==True:
                if fpsDino <5:
                    fpsDino+=1.5
                    gameDisplay.blit(dino[0], (dinoX, dinoY))
                elif fpsDino<=10:
                    fpsDino+=1.5
                    gameDisplay.blit(dino[1], (dinoX, dinoY))
                elif fpsDino<=15:
                    fpsDino+=1.5
                    gameDisplay.blit(dino[2], (dinoX, dinoY))
                elif fpsDino<=20:
                    fpsDino+=1.5
                    gameDisplay.blit(dino[3], (dinoX, dinoY))
                else:
                    fpsDino=0
                    gameDisplay.blit(dino[0], (dinoX, dinoY))
            else:
                gameDisplay.blit(dino[0], (dinoX, dinoY))

            #Cacto
            cactoPosX = cactoX + varCactoX
            cactoX-=velocidade
            gameDisplay.blit(cacto, (cactoPosX,204))
            if cactoX<-largura:
                varCactoX = random.randint(50,250)
                cactoX = largura+varCactoX
            
            #Pássaro
            passaroPosX = passaroX + varPassaroX
            passaroX-=velocidadePassaro
            fpsPassaro+=1
            if fpsPassaro < 10:
                gameDisplay.blit(passaro1, (passaroPosX, passaroY))
            elif fpsPassaro < 20:
                gameDisplay.blit(passaro2, (passaroPosX, passaroY))
            else:
                fpsPassaro = 0
                gameDisplay.blit(passaro1, (passaroPosX,passaroY))
            if passaroX<-largura:
                passaroX = largura+varPassaroX
                passaroY = random.randint(100,200)
                varPassaroX = random.randint(250,400)
                velocidadePassaro = random.randint(5,10)
                
            # Análise de Colisão
            pixelsYDino = list(
                range(int(dinoY), int(dinoY) + alturaDino+1))
            pixelsXDino = list(
                range(dinoX, dinoX + larguraDino+1))
            
            pixelsYCacto = list(
                range(204, 204 + 60+1))
            pixelsXCacto = list(
                range(cactoPosX, cactoPosX + 60+1))

            pixelsYPassaro = list(
                range(passaroY, passaroY + 71))
            pixelsXPassaro = list(
                range(passaroPosX, passaroPosX + 71))

            # Analise de colisão com Cacto
            if len(list(set(pixelsYCacto) & set(pixelsYDino))) > dificuldade:
                if len(list(set(pixelsXCacto) & set(pixelsXDino))) > dificuldade:
                    jogando=False
                    morreu(gameDisplay, pygameDisplay, preto)
            
            # Analise de colisão com ave
            if len(list(set(pixelsYPassaro) & set(pixelsYDino))) > dificuldade:
                if len(list(set(pixelsXPassaro) & set(pixelsXDino))) > dificuldade:
                    jogando=False
                    morreu(gameDisplay, pygameDisplay, preto)

        pygameDisplay.update()
        clock.tick(60)
jogo()
