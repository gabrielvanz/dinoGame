import pygame
import os

def limparTela():
    os.system("cls")

def morreu(gameDisplay, pygameDisplay, cor):
    morteSound = pygame.mixer.Sound("sons/morte.wav")
    pygame.mixer.Sound.play(morteSound)
    fonte = pygame.font.Font("freesansbold.ttf", 50)
    fonteContinue = pygame.font.Font("freesansbold.ttf", 22)
    texto = fonte.render("GAME OVER", True, cor)
    textoContinue = fonteContinue.render("Press 'R' to continue...", True, cor)
    gameDisplay.blit(texto, (250, 100))
    gameDisplay.blit(textoContinue, (288, 180))
    pygameDisplay.update()

def salvar(nome,email):
    return (f"Nome: {nome}, email: {email}\n")