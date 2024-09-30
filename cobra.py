import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
largura, altura = 600, 400
tamanho_cobra = 20
velocidade = 10
pontuacao = 0

# Cores
cor_cobra = (0, 255, 0)
cor_comida = (255, 0, 0)
cor_fundo = (0, 0, 0)

# Inicialização da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')

# Função principal
def jogo():
    global pontuacao
    game_over = False

    # Inicialização da cobra
    cobra = [(largura // 2, altura // 2)]
    direcao = (0, 0)

    # Inicialização da comida
    comida = gerar_comida()

    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direcao != (0, 1):
                    direcao = (0, -1)
                elif evento.key == pygame.K_DOWN and direcao != (0, -1):
                    direcao = (0, 1)
                elif evento.key == pygame.K_LEFT and direcao != (1, 0):
                    direcao = (-1, 0)
                elif evento.key == pygame.K_RIGHT and direcao != (-1, 0):
                    direcao = (1, 0)

        # Movimentação da cobra
        cobra = mover_cobra(cobra, direcao)

        # Verificação de colisões
        if cobra[0] == comida:
            cobra.append((0, 0))  # Adiciona uma nova parte à cobra
            pontuacao += 1
            comida = gerar_comida()

        if verificar_colisao(cobra):
            game_over = True

        # Desenho na tela
        tela.fill(cor_fundo)
        desenhar_cobra(cobra)
        desenhar_comida(comida)
        desenhar_pontuacao()

        pygame.display.flip()
        pygame.time.Clock().tick(velocidade)

# Função para movimentar a cobra
def mover_cobra(cobra, direcao):
    cabeca = list(cobra[0])
    cabeca[0] += direcao[0] * tamanho_cobra
    cabeca[1] += direcao[1] * tamanho_cobra
    cobra = [tuple(cabeca)] + cobra[:-1]
    return cobra

# Função para desenhar a cobra na tela
def desenhar_cobra(cobra):
    for parte in cobra:
        pygame.draw.rect(tela, cor_cobra, (parte[0], parte[1], tamanho_cobra, tamanho_cobra))

# Função para gerar uma nova posição para a comida
def gerar_comida():
    x = random.randrange(0, largura, tamanho_cobra)
    y = random.randrange(0, altura, tamanho_cobra)
    return x, y

# Função para desenhar a comida na tela
def desenhar_comida(comida):
    pygame.draw.rect(tela, cor_comida, (comida[0], comida[1], tamanho_cobra, tamanho_cobra))

# Função para verificar colisões
def verificar_colisao(cobra):
    if cobra[0] in cobra[1:]:
        return True
    if (
        cobra[0][0] < 0 or
        cobra[0][1] < 0 or
        cobra[0][0] >= largura or
        cobra[0][1] >= altura
    ):
        return True
    return False

# Função para desenhar a pontuação na tela
def desenhar_pontuacao():
    fonte = pygame.font.Font(None, 36)
    texto = fonte.render(f'Pontuação: {pontuacao}', True, (255, 255, 255))
    tela.blit(texto, (10, 10))

# Execução do jogo
jogo()
