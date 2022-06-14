#Créateurs : BENCHELLOUG Lazhar, COTE Lucas
#Description du code : Classe des ennemis
#Contact : lazhar.benchelloug@etu.univ-lyon1.fr , lucas.cote@etu.univ-lyon1.fr
#Version 1.0

import random

import pygame
from pygame import Vector2
from math import pi

import core


class Enemy:
    def __init__(self):
        self.rayon = 15
        self.couleur=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.position=Vector2 (random.randint(0, 1600), (random.randint(0, 900)))
        self.f = Vector2()
        self.vitesse = Vector2()

        self.raideur = 0.5
        self.vitesse = 1
        self.vitessemax = 5
        self.direction = Vector2(0,0)
        self.Ux = Vector2(0,0)
        self.l = 0
        self.l0 = 10
        self.L = 0
        self.Fx = 0
        self.h = 0


    def draw(self, screen):
        pygame.draw.circle(screen,self.couleur,self.position,self.rayon)

    def dead(self):
        self.position = Vector2(random.randint(0, 1600), (random.randint(0, 900)))

    def deplacer(self, playerposition):
        print(playerposition)
        self.Ux = playerposition - self.position
        self.l = self.Ux.length()
        self.Ux = self.Ux.normalize()
        self.L = abs(self.l - self.l0)

        self.Fx = self.raideur * self.L * self.Ux
        self.direction = self.direction + self.Fx

        if self.direction.length() > self.vitessemax and self.direction.length() != 0:
            self.direction.normalize()
            self.direction.scale_to_length(self.vitessemax)

        self.position = self.direction + self.position

    def grossir(self):
        if self.rayon < 150:
            self.rayon = self.rayon + 1