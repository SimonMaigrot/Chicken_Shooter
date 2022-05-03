import pygame

class Shoot(pygame.sprite.Sprite):
    def __init__(self):
        self.sniper = pygame.image.load('assets/shoot.png')
        self.sniper = pygame.transform.scale(self.sniper, (300, 300))
        self.sniper_rect = self.sniper.get_rect()

        self.gun = pygame.image.load("assets/lunette_pistolet.png")
        self.gun = pygame.transform.scale(self.gun, (128, 128))
        self.gun_rect = self.gun.get_rect()

        self.ak = pygame.image.load("assets/ak_viseur.png")
        self.ak = pygame.transform.scale(self.ak, (128, 128))
        self.ak_rect = self.ak.get_rect()