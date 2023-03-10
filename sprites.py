import pygame
import random

class Numero(pygame.sprite.Sprite):
    
    def __init__(self, dicionario_de_arquivos, numero):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.numero = numero
        self.image = dicionario_de_arquivos['caixa'] # assets é um dicionário de imagens, sons e fonts
        self.image = pygame.transform.scale(self.image, (70, 70))
    
        #todo objeto precisa de um rect
        # rect é a representação de retangulo feita pelo pygame
        self.rect = self.image.get_rect()
        self.rect.x =  random.randint(0,900-70)# defina posicao em x
        self.rect.y = random.randint(0,700-70) # defina posicao em y
        
    

class Botao(pygame.sprite.Sprite):
    def __init__(self, assets, nome_do_jogo):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.assets = assets
        self.image = assets['btn'] # assets é um dicionário de imagens, sons e fonts
        self.mask = pygame.mask.from_surface(self.image)
        #todo objeto precisa de um rect
        # rect é a representação de retangulo feita pelo pygame
        self.rect = self.image.get_rect()
        # é preciso definir onde a imagem deve aparecer no jogo
        self.rect.x = 0
        self.rect.y = 0

        self.nome_do_jogo = nome_do_jogo

    def mouse_over(self, over):
        # Toda a lógica de movimentação deve ser feita aqui
        # Atualização da posição da nave
        if over:
            self.image = self.assets['btn_hover']
        else:
            self.image = self.assets['btn']
