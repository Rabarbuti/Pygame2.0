import pygame
import random
from palavras import medio
import random
from turtle import pos
from pygame.locals import *
import pygame, sys



#Setup inicial
pygame.init()
WIDTH = 1080 #eixo x
HEIGHT = 720 #altura
pontuacao = 0
pygame.mixer.init()
pygame.mixer.music.load('sons/musica_jogo.wav') #musica
pygame.mixer.music.set_volume(0.5)
som_perdeu = pygame.mixer.Sound('sons/fim_jogo.wav') #sons
som_ponto = pygame.mixer.Sound('sons/som_ponto.wav')

#condicoes iniciais para as funções
mainClock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
pygame.display.set_caption('Soletra Insper')
imagem_fundo_inicial = pygame.image.load('imagens/inicio.png') 
imagem_fundo_inicial = pygame.transform.scale(imagem_fundo_inicial, (WIDTH, HEIGHT))  
fonte_jogo = pygame.font.match_font('Algerian')
velocidade_da_palavra_medio = 0.5

#flags
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
    palavra_para_acertar = font.render(texto, True, (0,0,0))
    acertando = palavra_para_acertar.get_rect()
    acertando.midtop = (i, j)
    screen.blit(palavra_para_acertar, acertando)

#funcao para escrever dentro do jogo também, porem de forma diferente
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)



#funcao para desenhar nosso menu na tela
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
            if pygame.mouse.get_pressed()[0] == True:
                setando_jogo()
                game()
        
        if button_3.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0] == True:
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


#tela final, para que possa iniciar outro jogo
def telaFinal():
    
    bandeira = True
    while bandeira:
        tela_fundo = pygame.image.load('imagens/perdeu.png')
        tela_fundo = pygame.transform.scale(tela_fundo,(WIDTH, HEIGHT))
        screen.blit(tela_fundo,(0,0))
        texto(screen, "Infelizmente você perdeu", 30, WIDTH / 2, HEIGHT - 200)
        fonte = pygame.font.SysFont(None, 40)
        mx, my = pygame.mouse.get_pos()
        button_4 = pygame.Rect(425, 600, 250, 45)
        pygame.draw.rect(screen, (255, 0, 0), button_4)
        draw_text('Jogar Novamente', fonte, (255, 255, 255), screen, 430, 610)
        pygame.display.update()
        mainClock.tick(60)

        if button_4.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0] == True:
                main_menu()

        for t in pygame.event.get():
            if t.type == pygame.QUIT:
                pygame.quit()
            if t.type == pygame.KEYUP:
                bandeira = False

            pygame.display.update()


#tela de HOW TO PLAY
def options():
    running = True
    while running:
        screen.fill((0,0,0))
        tela_fundo = pygame.image.load('imagens/options.png')
        font = pygame.font.SysFont(None, 40)
        tela_fundo = pygame.transform.scale(tela_fundo,(WIDTH, HEIGHT))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        screen.blit(tela_fundo,(0,0))
        mx, my = pygame.mouse.get_pos()
        button_3 = pygame.Rect(0,0, 100, 30)


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
    pygame.display.update()
    setando_jogo()
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
                        pygame.display.update()

                        
                else:
                    #jogador perdeu
                    som_perdeu.play()
                    yp = HEIGHT - 80

        #colocando uma altura minima que a figura do personagem possa chegar, caso ultrapasse, ele ira perder
        if yp < HEIGHT - 80:
            pygame.display.update()
        else:
            telaFinal()
            velocidade_da_palavra_medio = 0.5 #reiniciano a velocidade das palavras
            pygame.display.update()
setando_jogo()
main_menu()
