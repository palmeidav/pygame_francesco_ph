import pygame
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos
from sprites import Numero
def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()
    lista_caixas = pygame.sprite.Group()
    caixa = Numero(dicionario_de_arquivos)
    lista_caixas.add(caixa)
    DONE = 0
    PLAYING = 1
    state = PLAYING
    last_update = pygame.time.get_ticks()
    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)
        segundos = int(pygame.time.get_ticks() - last_update)
        print(segundos)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        lista_caixas.draw(window)
        pygame.display.update()  # Mostra o novo frame para o jogador

    return state
