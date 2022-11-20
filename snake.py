import pygame
from pygame.locals import *
from sys import exit
from time import sleep
from random import randint

pygame.init()

# SOM
pygame.mixer.music.set_volume(0.05)
musica_de_fundo = pygame.mixer.music.load('MarioSounds\soundtrack.mp3')
pygame.mixer.music.play(-1)
barulho_colisao = pygame.mixer.Sound('MarioSounds\mariocoin.wav')

# TELA
largura = 1000
altura = 800
# VARIAVEIS DE CONTROLE

membros = 0
direcoes = [-20, 20]
direcao = [direcoes[1], 0]
sentido = 'direita'
pontos = 0

# CORPO COBRA
x_maca = randint(2, 48) * 20
y_maca = randint(2, 38) * 20
pos_cabeca = [20 * 20, 20 * 20]
corpo_cobra = []
tick = 0

# TEXTO
fonte = pygame.font.SysFont('arial', 40, True, True)
fonte_xy = pygame.font.SysFont('arial', 10, True, True)
pygame.display.set_caption('Snake')

relogio = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))

while True:
    
    stage = 0
    relogio.tick(10)
    tela.fill((255, 255, 255))
    msg = f'Pontuação: {pontos}'
    msg_x = f'{corpo_cobra}'
    texto_formatado = fonte.render(msg, True, (0, 0, 0))
    texto_formatado_x = fonte_xy.render(msg_x, True, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        # CONTROLE DE DIREÇÂO ( W A S D ) E FUNÇOES DEBUG
        if event.type == pygame.KEYDOWN and stage == 0:
            if sentido == 'direita':
                if event.key == K_w: # CIMA
                    direcao = [0, direcoes[0]]
                    sentido = 'cima'
                    stage = 1
                if event.key == K_s: # BAIXO
                    direcao = [0, direcoes[1]]
                    sentido = 'baixo'
                    stage = 1

            if sentido == 'esquerda':
                if event.key == K_w: # CIMA
                    direcao = [0, direcoes[0]]
                    sentido = 'cima'
                    stage = 1
                if event.key == K_s: # BAIXO
                    direcao = [0, direcoes[1]]
                    sentido = 'baixo'
                    stage = 1

            if sentido == 'cima':
                if event.key == K_a: # ESQUERDA
                    direcao = [direcoes[0], 0]
                    sentido = 'esquerda'
                    stage = 1
                if event.key == K_d: # DIREITA
                    direcao = [direcoes[1], 0]
                    sentido = 'direita'
                    stage = 1
            
            if sentido == 'baixo':
                if event.key == K_a: # ESQUERDA
                    direcao = [direcoes[0], 0]
                    sentido = 'esquerda'
                    stage = 1
                if event.key == K_d: # DIREITA
                    direcao = [direcoes[1], 0]
                    sentido = 'direita'
                    stage = 1

            if event.key == K_UP:
                corpo_cobra.append(pos_cabeca)

    # MOVIMENTO CABEÇA ( ORIGEM )
    pos_cabeca[0] = int(pos_cabeca[0] + direcao[0])
    pos_cabeca[1] = int(pos_cabeca[1] + direcao[1])

    # MOVIMENTO DO CORPO 
    corpo_cobra_anterior = corpo_cobra.copy()
    for c in range(0, len(corpo_cobra)):
        if c != 0:
            corpo_cobra[c] = corpo_cobra_anterior[c-1].copy()

    # RENDERIZAÇÃO
    cobra = pygame.draw.rect(tela, (0, 255, 0), (pos_cabeca[0], pos_cabeca[1], 20, 20))
    maca = pygame.draw.rect(tela, (200, 0, 0), (x_maca, y_maca, 20, 20))
    for c in range(0, len(corpo_cobra)):
        corpo_render = pygame.draw.rect(tela, (0, 255, 0), (corpo_cobra[c][0], corpo_cobra[c][1], 20, 20))
        if 2 < c:
            if cobra.colliderect(corpo_render):
                pygame.quit()
                exit()

    #GAMBIARRA PRO JOGO FUNCIONAR
    if tick < 4:
        corpo_cobra.append(pos_cabeca)

    # CONSEQUENCIAS DA COLISÃO COM MAÇA
    if cobra.colliderect(maca):
        x_maca = randint(2, 48) * 20
        y_maca = randint(2, 38) * 20
        pontos = pontos + 1
        barulho_colisao.play()
        membros = membros + 1
        corpo_cobra.append(pos_cabeca)


    # IMPRESSÃO DE TEXTO NA TELA ( PARA DEPURAÇÃO )
    tela.blit(texto_formatado_x, (40, 700))

    # IMPRESSÃO DA PONTUAÇÃO
    tela.blit(texto_formatado, (350, 40))

    tick = tick + 1

    pygame.display.update()
