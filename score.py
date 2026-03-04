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
    
    if spiller.liv == 0:
        vindu.fill(WHITE, (0, 0, VINDU_BREDDE, VINDU_HOYDE))
        gameoverTekst = font.render(f"Game Over\nScore: {spiller.poeng}", True, BLACK)
        tekstRect = gameoverTekst.get_rect(center=vindu.get_rect().center)
        
        vindu.blit(gameoverTekst, tekstRect)