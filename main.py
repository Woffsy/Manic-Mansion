import pygame as pg
import os
from konstanter import *
from klasser import *
from score import *
import random

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
    safezones = [
    pg.Rect(0, 0, SAFE_BREDDE, VINDU_HOYDE),
    pg.Rect(VINDU_BREDDE - SAFE_BREDDE, 0, SAFE_BREDDE, VINDU_HOYDE)
]
    running: bool = True

    spiller = Spiller(100, 100)
    
    sauer = [Sau(1100, 200), Sau(1100, 400), Sau(1100, 600)]
    
    spokelser = [Spokelse(safezones,0,random.randint(0,VINDU_HOYDE - 100))]
    
    hinder = [Hinder(vindu) for _ in range(3)]

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False
        
        spiller.flyttSpiller(hinder)
        for spokelse in spokelser:
            spokelse.flyttSpokelse()

        tegn_bakgrunn(vindu, bakgrunn)
        for s in safezones:
            pg.draw.rect(vindu, WHITE, s, 2)
        if oppdaterAlt(vindu, spiller, sauer, spokelser, hinder):
            sauer.append(Sau(1100,random.randint(0,VINDU_HOYDE)))
            spokelser.append(Spokelse(safezones,random.randint(100, VINDU_BREDDE-2*SAFE_BREDDE),random.randint(0, VINDU_HOYDE - 100)))
            hinder.append(Hinder(vindu))


        tavle(vindu, spiller)

        pg.display.flip()
        clock.tick(FPS)
        
if __name__ == "__main__":
    main()
