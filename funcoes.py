import pygame
import random
from palavras import medio, dificeis


#Setup inicial
pygame.init()
WIDTH = 1080
HEIGHT = 720
preto = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
pygame.display.set_caption('Soletra Insper')
imagem_fundo_inicial = pygame.image.load('') #colocar iamgem de fundo aq
imagem_fundo_inicial = pygame.transform.scale(imagem_fundo_inicial, (WIDTH, HEIGHT))  
fonte = pygame.font.Font('Algerian', 40)
fonte_jogo = pygame.font.match_font('Algerian')
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



def texto(texto, tamanho, i, j):
    font = pygame.font.Font(fonte_jogo, tamanho)
    palavra_para_acertar = font.render(texto, True, preto)
    acertando = palavra_para_acertar.get_rect()
    acertando.midtop = (i, j)
    screen.blit(palavra_para_acertar, acertando)


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
