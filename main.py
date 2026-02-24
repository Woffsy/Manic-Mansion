import pygame as pg
import os
from konstanter import *

pg.init()

vindu: pg.Surface = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE), pg.RESIZABLE)
clock: pg.time.Clock = pg.time.Clock()

BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))

bakgrunn: pg.Surface = pg.image.load(
    os.path.join(BASE_DIR, "Bilder", "gress.png")
).convert()

def tegn_bakgrunn(surface: pg.Surface, bilde: pg.Surface) -> None:
    bilde_bredde: int = bilde.get_width()
    bilde_hoyde: int = bilde.get_height()
    
    vindu_bredde: int = surface.get_width()
    vindu_hoyde: int = surface.get_height()
    
    for x in range(0, vindu_bredde, bilde_bredde):
        for y in range(0, vindu_hoyde, bilde_hoyde):
            surface.blit(bilde, (x, y))

def main() -> None:
    running: bool = True
    
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