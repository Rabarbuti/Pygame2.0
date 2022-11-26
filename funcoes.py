import pygame, sys
import random
from palavras import medio, dificeis
import random
from turtle import pos
from pygame.locals import *
import time
import jogo

#Setup inicial
pygame.init()
WIDTH = 1080
HEIGHT = 720
preto = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
pygame.display.set_caption('Soletra Insper')
imagem_fundo_inicial = pygame.image.load('imagens/inicio.png') #colocar iamgem de fundo aq
imagem_fundo_inicial = pygame.transform.scale(imagem_fundo_inicial, (WIDTH, HEIGHT))  
fonte = pygame.font.Font('comic.ttf', 40)
fonte_jogo = pygame.font.match_font('comic.ttf')
velocidade_da_palavra_medio = 0.5
velocidade_da_palavra_dificil = 0.5
pontuacao = 0
morreu = True
inicio = True




def setando_jogo(nivel):
    global palavras_jogo, jogador_escrevendo, x, y, velocidade_da_palavra_medio, velocidade_da_palavra_dificil
    x = 700
    y = 200  
    velocidade_da_palavra_medio += 0.1
    velocidade_da_palavra_dificil += 0.15
    jogador_escrevendo = ''
    if nivel == 'medio':
        palavras = medio
        palavras_jogo = random.choice(palavras)
    else:
        palavras = dificeis
        palavras_jogo = random.choice(palavras)




def texto(screen, texto, tamanho, i, j):
    font = pygame.font.Font(fonte_jogo, tamanho)
    palavra_para_acertar = font.render(texto, True, preto)
    acertando = palavra_para_acertar.get_rect()
    acertando.midtop = (i, j)
    screen.blit(palavra_para_acertar, acertando)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def telaInicial_telaFinal():
    screen.blit(imagem_fundo_inicial, (0, 0))
    if not morreu:
        texto(screen, "Infelizmente você perdeu", 90, WIDTH / 2, HEIGHT / 4)
        texto(screen, "Mas sua pontuação foi de: " + str(pontuacao), 70, WIDTH / 2, HEIGHT / 2)
    else:
        texto(screen, "Clique qualquer tecla para iniciar o Soletra Insper", 54, WIDTH / 2, 500)
    pygame.display.flip()
    bandeira = True
    while bandeira:

        for t in pygame.event.get():
            if t.type == pygame.QUIT:
                pygame.quit()
            if t.type == pygame.KEYUP:
                bandeira = False



def main_menu():
    while True:
        fonte = pygame.font.SysFont(None, 40)
        screen.fill((0,0,0))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(255, 545, 100, 45)
        button_2 = pygame.Rect(450, 545, 180, 45)
        button_3 = pygame.Rect(710, 545, 180, 45)
        tela_fundo = pygame.image.load('imagens/inicio.png')
        tela_fundo = pygame.transform.scale(tela_fundo,(WIDTH, HEIGHT))
        draw_text('main menu', fonte, (255, 255, 255), screen, 20, 20)
        screen.blit(tela_fundo,(0,0))
        if button_1.collidepoint((mx, my)):
            if click:
                setando_jogo('medio')
                

        if button_2.collidepoint((mx, my)):
            if click:
                setando_jogo('dificil')
                #main()
        
        '''if button_3.collidepoint((mx, my)):
            if click:
                options()'''
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        draw_text('Médio', fonte, (255, 255, 255), screen, 270, 556)
        draw_text('Dificil', fonte, (255, 255, 255), screen, 500, 556)
        draw_text('How To Play', fonte, (255, 255, 255), screen, 720, 556)

        pygame.display.update()

main_menu()