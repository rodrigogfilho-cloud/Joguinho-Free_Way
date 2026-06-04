import pygame
import random

class Viloes:
    
    def __init__(self, endereco_imagem):
       
        self.imagem = pygame.image.load(endereco_imagem)
        self.imagem = pygame.transform.scale_by (self.imagem,0.6)

        #posicao  do vilão
        self.pos_x_inimigo= -60
        
        #criando uma posição y aleatoria
        self.ruas = [230, 560, 440,330]
        self.pos_y_inimigo = random.choice(self.ruas)
        self.velocidade = random.randint(15,30)

        #criando a mascara p/ a colisão
        self.mascara = pygame.mask.from_surface(self.imagem)

    def andar(self):
        
        self.pos_x_inimigo = self.pos_x_inimigo + self.velocidade
        if self.pos_x_inimigo > 1700:
            self.voltar()

    def exibir(self, tela_do_jogo):
        tela_do_jogo.blit(self.imagem,(self.pos_x_inimigo,self.pos_y_inimigo))

    def voltar (self):
        
        self.pos_x_inimigo= -60
        self.pos_y_inimigo = random.choice(self.ruas)
        self.velocidade = random.randint(5,30)
    