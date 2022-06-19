from re import X
import pygame
import random
import time
pygame.init()
largura = 800
altura = 300

tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("Star Wars")
gameDisplay = pygame.display.set_mode(tamanho)
#gameIcon = pygame.image.load("assets/TrupperIco.ico")
#pygameDisplay.set_icon(gameIcon)

branco = (255, 255, 255)



clock = pygame.time.Clock()
gameEvents = pygame.event

def jogo():
    x = 0
    fps = 0
    i = 0
    posicaoX = 0
    posicaoY = random.randrange(0, altura)
    
    velocidade = 1
    pontos = 0
    lista = []

    for teste in range(0,largura,70):
        lista.append(teste)

    tamanhoPadrao = (70,70)

    print (lista)

    dino1 = pygame.image.load("imagens/dino1.png")
    dino2 = pygame.image.load("imagens/dino2.png")
    dino3 = pygame.image.load("imagens/dino3.png")
    dino1 = pygame.transform.scale(dino1, tamanhoPadrao)
    dino2 = pygame.transform.scale(dino2, tamanhoPadrao)
    dino3 = pygame.transform.scale(dino3, tamanhoPadrao)

    dino = [dino2,dino1,dino2,dino3]

    chao = pygame.image.load("imagens/chao.png")
    chao = pygame.transform.scale(chao, tamanhoPadrao)
    
    """
    pygame.mixer.music.load("assets/trilha.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    """
    
    gravidade = 0
    dinoY = 206

    alturaDino = 32
    larguraDino = 32

    alturaMissel = 52
    larguraMissel = 150
    dificuldade = 19

    while True:
        # aqui é lido os eventos da tela
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    jogo()
                if event.key == pygame.K_SPACE:
                    gravidade = -15
                    
                    
        gravidade = gravidade + 1
        x -=1
        if x<-1:
            x=largura
        dinoY+=gravidade

        if dinoY > 206: dinoY = 206

        gameDisplay.fill(branco)    
        
        gameDisplay.blit(chao,(lista[0]+x,230))
        gameDisplay.blit(chao,(lista[1]+x,230))
        gameDisplay.blit(chao,(lista[2]+x,230))
        gameDisplay.blit(chao,(lista[3]+x,230))
        gameDisplay.blit(chao,(lista[4]+x,230))
        gameDisplay.blit(chao,(lista[5]+x,230))
        gameDisplay.blit(chao,(lista[6]+x,230))
        gameDisplay.blit(chao,(lista[7]+x,230))
        gameDisplay.blit(chao,(lista[8]+x,230))
        gameDisplay.blit(chao,(lista[9]+x,230))
        gameDisplay.blit(chao,(lista[10]+x,230))
        gameDisplay.blit(chao,(lista[11]+x,230))

        
            
        

        if fps <15:
            fps+=1
            gameDisplay.blit(dino[0], (100, dinoY))
        elif fps<=30:
            fps+=1
            gameDisplay.blit(dino[1], (100, dinoY))
        elif fps<=45:
            fps+=1
            gameDisplay.blit(dino[2], (100, dinoY))
        elif fps<=60:
            fps+=1
            gameDisplay.blit(dino[3], (100, dinoY))
        else:
            fps=0
            gameDisplay.blit(dino[0], (100, dinoY))
            











        
       

        pygameDisplay.update()
        clock.tick(60)


jogo()