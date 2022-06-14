#Créateurs : BENCHELLOUG Lazhar, COTE Lucas
#Description du code : Main du code
#Contact : lazhar.benchelloug@etu.univ-lyon1.fr , lucas.cote@etu.univ-lyon1.fr
#Version 1.0

import pygame
import core
from enemy import Enemy
from creep import Creep
from player import Player


def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [1080, 720]

    core.memory("Player", Player())
    core.memory("Enemy", Enemy())
    core.memory("Quadrillage", 90)
    core.memory("CouleurGrille", (10, 10, 10))

    # Couleur du fond de l'écran
    core.bgColor = (255, 255, 255)

    # Creeps
    core.memory("TableauDeCreeps", [])

    for c in range(150):
        core.memory("TableauDeCreeps").append(Creep())

    # Enemy
    core.memory("TableauDEnemy", [])

    for e in range(8):
        core.memory("TableauDEnemy").append(Enemy())


def run():
    core.cleanScreen()
    for x in range(0, 1080, core.memory("Quadrillage")):
        for y in range(0, 720, core.memory("Quadrillage")):
            rect = pygame.Rect(x, y, core.memory("Quadrillage"), core.memory("Quadrillage"))
            pygame.draw.rect(core.screen, core.memory("CouleurGrille"), rect, 1)

    core.memory("Player").draw(core.screen)
    core.memory("Player").deplacer(core.getMouseLeftClick())

    # Dessiner les Creeps :
    for c in core.memory("TableauDeCreeps"):
        c.draw(core.screen)

    # Manger creep :
    for c in core.memory("TableauDeCreeps"):
        if c.position.distance_to(core.memory("Player").position) < (core.memory("Player").rayon + c.rayon):
            c.dead()
            core.memory("Player").grossir()

    # Manger creep (ennemies):
    for c in core.memory("TableauDeCreeps"):
        if c.position.distance_to(core.memory("Enemy").position) < (core.memory("Enemy").rayon + c.rayon):
            c.dead()
            core.memory("Enemy").grossir()

    # Dessiner les enemy
    for e in core.memory("TableauDEnemy"):
        e.draw(core.screen)
        e.deplacer(core.memory("Player").position)

    # Manger enemy :
    for e in core.memory("TableauDEnemy"):
        if e.position.distance_to(core.memory("Player").position) < (core.memory("Player").rayon + e.rayon):
            e.dead()
            core.memory("Player").grossir()


core.main(setup, run)