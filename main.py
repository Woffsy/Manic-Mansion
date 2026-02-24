import pygame as pg 
import os
from konstanter import *

pg.init()

vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE), pg.RESIZABLE)
clock = pg.time.Clock()

# RESSURSER
BASE_DIR = os.path.dirname(__file__)

bakgrunn = pg.image.load(
    os.path.join(BASE_DIR, "Bilder", "gress.png")
).convert()

def tegn_bakgrunn(surface, bilde):
    bilde_bredde = bilde.get_width()
    bilde_hoyde = bilde.get_height()
    
    vindu_bredde = surface.get_width()
    vindu_hoyde = surface.get_height()
    
    # Looper gjennom hele vinduet
    for x in range(0, vindu_bredde, bilde_bredde):
        for y in range(0, vindu_hoyde, bilde_hoyde):
            surface.blit(bilde, (x, y))


def main():
    running = True
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        tegn_bakgrunn(vindu, bakgrunn)
        
        
        pg.display.flip()
        clock.tick(FPS)
        
if __name__ == "__main__":
    main()