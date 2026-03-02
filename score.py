from konstanter import *
import pygame as pg
from klasser import *

pg.font.init()

font = pg.font.SysFont("Arial", 24)

def tavle(vindu:pg.Surface, spiller:Spiller):
    scoreTekst = font.render(f"Score: {spiller.poeng}", True, BLACK)
    livTekst = font.render(f"Liv: {spiller.liv}", True, BLACK)
    
    vindu.blit(scoreTekst, (10, 10))
    vindu.blit(livTekst, (10, 40))