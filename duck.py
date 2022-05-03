import pygame
from random import *

class Duck(pygame.sprite.Sprite):
    def __init__(self, height):
        self.image = pygame.image.load('assets/chicken.png')
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = randint(0, height - 100)
        self.speed = 4

    def move(self):
        self.rect.x += self.speed 

