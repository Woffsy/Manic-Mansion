import pygame as pg 
from konstanter import *

pg.init()

vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE), pg.RESIZABLE)
clock = pg.time.Clock()

def main():
    running = True
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        vindu.fill(WHITE)
        
        
        pg.display.flip()
        clock.tick(FPS)
        
if __name__ == "__main__":
    main()