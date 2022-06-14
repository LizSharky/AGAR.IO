#Créateurs : BENCHELLOUG Lazhar, COTE Lucas
#Description du code : Classe des creeps
#Contact : lazhar.benchelloug@etu.univ-lyon1.fr , lucas.cote@etu.univ-lyon1.fr
#Version 1.0

import random

import pygame
from pygame import Vector2


class Creep:
    def __init__(self):
        self.rayon = 5
        self.couleur=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.position=Vector2 (random.randint(0, 1600), (random.randint(0, 900)))

    def draw(self, screen):
        pygame.draw.circle(screen,self.couleur,self.position,self.rayon)

    def dead(self):
        self.position = Vector2(random.randint(0, 1600), (random.randint(0, 900)))