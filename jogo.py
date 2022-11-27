import pygame
import random
from palavras import medio
import random
from turtle import pos
from pygame.locals import *
import pygame, sys
import time
import funcoes
from funcoes import *




#Setup inicial
pygame.init()
WIDTH = 1080
HEIGHT = 720
pontuacao = 0
preto = (0, 0, 0)
pygame.mixer.init()
pygame.mixer.music.load('sons/musica_jogo.wav')
pygame.mixer.music.set_volume(0.5)
som_perdeu = pygame.mixer.Sound('sons/fim_jogo.wav')
som_ponto = pygame.mixer.Sound('sons/som_ponto.wav')

mainClock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
pygame.display.set_caption('Soletra Insper')
imagem_fundo_inicial = pygame.image.load('imagens/inicio.png') #colocar iamgem de fundo aq
imagem_fundo_inicial = pygame.transform.scale(imagem_fundo_inicial, (WIDTH, HEIGHT))  
fonte_jogo = pygame.font.match_font('Algerian')
velocidade_da_palavra_medio = 0.5
morreu = True
inicio = True


#sorteia a palavra que o jogador terá que escrever
#também sorteia a posição no eixo x que a palavra sera colocada
def setando_jogo():
    global palavras_jogo, jogador_escrevendo, xp, yp, velocidade_da_palavra_medio
    xp = random.randint(100, WIDTH-100)
    yp = 200  
    velocidade_da_palavra_medio += 0.1
    jogador_escrevendo = ''
    palavra = medio
    palavras_jogo = random.choice(palavra)
    palavras_jogo = palavras_jogo.lower()

#funcao para conseguir escrever dentro do jogo
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



def main_menu():
    pygame.mixer.music.play()
    setando_jogo()
    while True:

        fonte = pygame.font.SysFont(None, 40)
        screen.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(255, 545, 100, 45)
        button_3 = pygame.Rect(710, 545, 180, 45)
        tela_fundo = pygame.image.load('imagens/inicio.png')
        tela_fundo = pygame.transform.scale(tela_fundo,(WIDTH, HEIGHT))
        draw_text('main menu', fonte, (255, 255, 255), screen, 20, 20)
        screen.blit(tela_fundo,(0,0))
        if button_1.collidepoint((mx, my)):
            if click:
                setando_jogo()
                game()
        
        if button_3.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
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
            draw_text('Return', fonte, (255, 255, 255), screen, 3, 2)

        
            draw_text('jogar', fonte, (255, 255, 255), screen, 270, 556)

            draw_text('How To Play', fonte, (255, 255, 255), screen, 720, 556)
            pygame.display.update()


#tela inicial que funciona a base do clique em alguma tecla do jogador
def telaFinal():
    screen.blit(imagem_fundo_inicial, (0, 0))

    texto(screen, "Infelizmente você perdeu", 30, WIDTH / 2, HEIGHT - 200)

    pygame.display.flip()
    bandeira = True
    while bandeira:

        for t in pygame.event.get():
            if t.type == pygame.QUIT:
                pygame.quit()
            if t.type == pygame.KEYUP:
                bandeira = False
def options():
    running = True
    while running:
        screen.fill((0,0,0))

        font = pygame.font.SysFont(None, 40)
        mx, my = pygame.mouse.get_pos()
        button_3 = pygame.Rect(0,0, 100, 30)
        tela_fundo = pygame.image.load('Regras.png')
        tela_fundo = pygame.transform.scale(tela_fundo,(WIDTH, HEIGHT))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        screen.blit(tela_fundo,(0,0))

        if button_3.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0] == True:
                main_menu()
        pygame.draw.rect(screen, (255, 0, 0), button_3)

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
            draw_text('Return', font, (255, 255, 255), screen, 3, 2)
            pygame.display.update()
        mainClock.tick(60)


#loop principal do jogo
def game():
    pontuacao = 0
    global palavras_jogo, jogador_escrevendo, xp, yp, velocidade_da_palavra_medio
    xp = random.randint(100, WIDTH-100)
    yp = 200  
    velocidade_da_palavra_medio += 0.1
    jogador_escrevendo = ''
    palavra = medio
    palavras_jogo = random.choice(palavra)
    palavras_jogo = palavras_jogo.lower()
    while True:
        #carregando as imagens e alterando o tamanho delas
        fundo_jogo = pygame.image.load('imagens/fundo.jpg')
        fundo_jogo = pygame.transform.scale(fundo_jogo, (WIDTH,HEIGHT))
        personagem = pygame.image.load('imagens/raposa.png')
        personagem = pygame.transform.scale(personagem, (75,75))

        #alterando tela de fundo
        screen.blit(fundo_jogo, (0,0))

        #indicando a posição onde cada elemento da tela vai ficar
        yp += velocidade_da_palavra_medio
        screen.blit(personagem, (xp, yp))
        texto(screen, palavras_jogo, 40, xp+35,yp-40)
        texto(screen, 'Pontos:  ' + str(pontuacao), 40, WIDTH/2,5)
        texto(screen, jogador_escrevendo, 50, WIDTH/2, 150)


        #sistema para conferir as letras que o jogador está digitando
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif i.type == pygame.KEYDOWN:
                jogador_escrevendo += pygame.key.name(i.key)

                #conferindo se as letras do jogador correspondem a palavra sorteada
                if palavras_jogo.startswith(jogador_escrevendo):
                    if palavras_jogo == jogador_escrevendo:
                        pontuacao +=len(palavras_jogo)
                        setando_jogo()
                        som_ponto.play()
                else:
                    #jogador perdeu
                    som_perdeu.play()
                    telaFinal()
                    time.sleep(3)
                    pygame.quit()
        
        #colocando uma altura minima que a figura do personagem possa chegar, caso ultrapasse, ele ira perder
        if yp < HEIGHT - 80:
            pygame.display.update()
        else:
            telaFinal()
setando_jogo()
main_menu()
