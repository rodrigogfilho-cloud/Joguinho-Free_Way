import pygame

class Jogador:
    def __init__ (self):
        self.davi_x = 800
        self.davi_y = 750
        #carregando imagens 
        self.imagem = pygame.image.load("src/img/DAVI-BRITO.png")
        self.imagem = pygame.transform.scale_by (self.imagem,0.5)
        #mascara jogador
        self.mascara = pygame.mask.from_surface(self.imagem)

        self.som = pygame.mixer.Sound("src/sound/calabreso.mp3")

        self.victory = 0
    def andar(self,tecla_pressionada):
    
        if tecla_pressionada [pygame.K_RIGHT] or tecla_pressionada [pygame.K_d]:
            if self.davi_x < 1700 - self.imagem.get_width(): # arrumado*
                self.davi_x += 10
        if tecla_pressionada [ pygame.K_LEFT]or tecla_pressionada [pygame.K_a]:     
            if self.davi_x > 0:
                self.davi_x -= 10
        if tecla_pressionada [pygame.K_UP]or tecla_pressionada [pygame.K_w]:
            if self.davi_y > 0 :
                self.davi_y -= 10
        if tecla_pressionada [pygame.K_DOWN]or tecla_pressionada [pygame.K_s]:
            if self.davi_y < 900 - self.imagem.get_height():
                self.davi_y += 10 # arrumado*

    def exibir (self,tela_do_jogo):
        tela_do_jogo.blit(self.imagem,(self.davi_x,self.davi_y))
    
    def voltar(self):
        self.davi_x = 800
        self.davi_y = 750
    
    def gritar (self):
        self.som.play()