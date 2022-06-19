import imp
from funcoes import colisao,morreu
import pygame
import random
import time
pygame.init()
largura = 800
altura = 300

tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("Dino Game")
gameDisplay = pygame.display.set_mode(tamanho)
gameIcon = pygame.image.load("imagens/icone.ico")
pygameDisplay.set_icon(gameIcon)

#Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

clock = pygame.time.Clock()
gameEvents = pygame.event

def dead(pontos):
    #gameDisplay.blit(bg_destroy, (0, 0))
    pygame.mixer.music.stop()
    #pygame.mixer.Sound.play(explosaoSound)
    fonte = pygame.font.Font("freesansbold.ttf", 50)
    fonteContinue = pygame.font.Font("freesansbold.ttf", 25)
    texto = fonte.render("Você Perdeu com "+str(pontos) +
                         " pontos!", True, preto)
    textoContinue = fonteContinue.render(
        "Press enter to continue...", True, branco)
    gameDisplay.blit(textoContinue, (50, 200))
    gameDisplay.blit(texto, (50, 100))
    pygameDisplay.update()

def jogo():
    x = 0
    y = 230
    fpsDino = 0
    fpsPassaro = 0
    i = 0
    posicaoX = 800
    posicaoY = random.randrange(0, altura)
    
    velocidade = 5
    pontos = 0

    tamanhoPadrao = (70,70)

    dino1 = pygame.image.load("imagens/dino1.png")
    dino2 = pygame.image.load("imagens/dino2.png")
    dino3 = pygame.image.load("imagens/dino3.png")
    dino1 = pygame.transform.scale(dino1, tamanhoPadrao)
    dino2 = pygame.transform.scale(dino2, tamanhoPadrao)
    dino3 = pygame.transform.scale(dino3, tamanhoPadrao)

    dino = [dino2,dino1,dino2,dino3]

    cacto = pygame.image.load("imagens/cacto.png")
    cacto = pygame.transform.scale(cacto, (60,60))

    passaro1 = pygame.image.load("imagens/passaro1.png")
    passaro2 = pygame.image.load("imagens/passaro2.png")
    passaro1 = pygame.transform.scale(passaro1, (70,70))
    passaro2 = pygame.transform.scale(passaro2, (70,70))

    nuvem = pygame.image.load("imagens/nuvem.png")
    nuvem = pygame.transform.scale(nuvem, tamanhoPadrao)

    chao = pygame.image.load("imagens/chao.png")
    
    """pygame.mixer.music.load("assets/trilha.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    """
    
    nuvemAX = 800
    nuvemAY = random.randint(0,130)
    nuvemBX = 900
    nuvemBY = random.randint(0,130)
    nuvemCX = 1000
    nuvemCY = random.randint(0,130)

    gravidade = 0
    dinoX = 150
    dinoY = 206
    alturaDino = 70
    larguraDino = 70

    cactoX = largura
    varCactoX = 0
    
    passaroX = largura+cactoX
    varPassaroX = 100
    passaroY = random.randint(180,200)
    velocidadePassaro = random.randint(5,8)

    pulo = False
    dificuldade = 35

    while True:
        # aqui é lido os eventos da tela
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
                    
        gameDisplay.fill(branco)    

        pontos +=1

        #Chão
        gameDisplay.blit(chao,(x,230))
        gameDisplay.blit(chao,(largura+x,230))
        
        if (x==-largura):
            gameDisplay.blit(chao,(largura+x,230))
            x=0
        x-=velocidade

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

        # Analise de colisão com cacto
        colisao(pixelsYCacto,pixelsYDino,pixelsXCacto,pixelsXDino,dificuldade)
        # Analise de colisão com ave
        colisao(pixelsYPassaro,pixelsYDino,pixelsXPassaro,pixelsXDino,dificuldade)

        pygameDisplay.update()
        clock.tick(60)

jogo()