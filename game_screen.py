import pygame
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos
from sprites import Numero
def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    e = 1
    dicionario_de_arquivos = carrega_arquivos()

    lista_caixas = pygame.sprite.Group()
    
    for i in range(5):
        caixa = Numero(dicionario_de_arquivos, i+1)
        lista_caixas.add(caixa)
        
    DONE = 0
    PLAYING = 1
    state = PLAYING
    last_update = pygame.time.get_ticks()
    
    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)
        segundos = int((pygame.time.get_ticks() - last_update)/1000)
        quarentao = 40- segundos
        print(quarentao)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.MOUSEBUTTONDOWN:
                state = PLAYING 
                
                for caixa in lista_caixas:
                    
                    if caixa.rect.collidepoint(event.pos):
                        print (caixa.numero)
                        if caixa.numero == e:
                            caixa.image = dicionario_de_arquivos['caixa_correto']
                            caixa.image = pygame.transform.scale(caixa.image, (70, 70))
                            e += 1
                        else:
                            e = 1
                            lista_caixas = pygame.sprite.Group()
    
                            for i in range(5):
                                caixa = Numero(dicionario_de_arquivos, i+1)
                                lista_caixas.add(caixa)
                                    
        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        
        lista_caixas.draw(window)
        for caixa in lista_caixas:
            font = pygame.font.SysFont(None, 48)
            text = font.render(str(caixa.numero), True, (0, 0, 255))
            window.blit(text, (caixa.rect.x + 5, caixa.rect.y + 5))
        text = font.render(str(quarentao), True, (0, 0, 255))
        window.blit(text, (0,0))
        pygame.display.update()  # Mostra o novo frame para o jogador
        
            
    return state
