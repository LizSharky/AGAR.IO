#Créateurs : BENCHELLOUG Lazhar, COTE Lucas
#Description du code : Classe du joueur
#Contact : lazhar.benchelloug@etu.univ-lyon1.fr , lucas.cote@etu.univ-lyon1.fr
#Version 1.0

import random

import pygame
from pygame import Vector2

import core


class Player:
    def __init__(self):
        self.rayon=21
        self.couleur=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.position=Vector2 (800, 450)
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


    def dead (self):
        pass

    def draw (self, screen):
        pygame.draw.circle(screen,self.couleur, self.position, self.rayon)

    def deplacer (self, clic):
        if self.position.y < 0 or self.position.y > core.WINDOW_SIZE[0]:
            self.direction = Vector2(self.direction.x, self.direction.y * -1)

        if self.position.x < 0 or self.position.x > core.WINDOW_SIZE[1]:
            self.direction = Vector2(self.direction.x * -1, self.direction.y)

        if clic is not None:

            self.Ux = clic - self.position
            self.l = self.Ux.length()
            self.Ux = self.Ux.normalize()
            self.L = abs(self.l - self.l0)

            self.Fx = self.raideur * self.L * self.Ux
            self.direction = self.direction + self.Fx

        else:
            self.Ux = Vector2(0, 0)

        if self.direction.length() > self.vitessemax and self.direction.length() != 0:
            self.direction.normalize()
            self.direction.scale_to_length(self.vitessemax)

        self.position = self.direction + self.position

    def grossir(self):
        if self.rayon < 150:
            self.rayon = self.rayon + 1