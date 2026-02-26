from __future__ import annotations
import pygame as pg
from konstanter import *
import random


class Spiller:
    def __init__(self, startX:int, startY:int) -> None:
        self.harSau:bool = False
        self.sau:Sau|None = None
        
        self.x:int = startX
        self.y:int = startY
        self.fart:int = 7
        
    def tegnSpiller(self, vindu:pg.Surface):
        pg.draw.circle(vindu, WHITE, (self.x, self.y), 25)
    
    def flyttSpiller(self):
        self.x = max(25, min(self.x, VINDU_BREDDE - 25))
        self.y = max(25, min(self.y, VINDU_HOYDE - 25))
        taster: tuple[bool, ...] = pg.key.get_pressed()
        if taster[pg.K_LEFT]:
            self.x -= self.fart
        if taster[pg.K_RIGHT]:
            self.x += self.fart
        if taster[pg.K_UP]:
            self.y -= self.fart
        if taster[pg.K_DOWN]:
            self.y += self.fart


    def plukkOppSau(self, sau:Sau) -> None:
        if not self.harSau:
            self.sau = sau
            self.harSau = True
    
    def leggFraSau(self) -> None:
        if self.harSau and self.sau:
            self.sau.x = self.x
            self.sau.y = self.y
            
            self.sau = None
            self.harSau = False

class Spokelse:
    def __init__(self, safezones:list[pg.Rect], startX:int, startY:int) -> None:
        self.safezones = safezones
        self.fart = random.randint(2, 5)
        self.retningX = random.choice([-1, 1])
        self.retningY = random.choice([-1, 1])
        
        self.x:int = startX
        self.y:int = startY

    def tegnSpokelse(self, vindu: pg.Surface):
        pg.draw.rect(vindu, WHITE, (self.x, self.y, 100, 100))
    
    def trefferSafezone(self, rect: pg.Rect):
        for sone in self.safezones:
            if rect.colliderect(sone):
                return True
            return False
    
    def flyttSpokelse(self):
        self.x += self.retningX * self.fart

        if self.x < SAFE_BREDDE:
            self.x = SAFE_BREDDE
            self.retningX *= -1

        if self.x > VINDU_BREDDE - SAFE_BREDDE - 100:
            self.x = VINDU_BREDDE - SAFE_BREDDE - 100
            self.retningX *= -1
        
        self.y += self.retningY * self.fart
       
        if self.y <= 0 or self.y >= VINDU_HOYDE - 100:
            self.y -= self.retningY * self.fart
            self.retningY *= -1

class Sau:
    def __init__(self, startX:int, startY:int) -> None:
        self.iSafeOmrade:bool = False
        
        self.x:int = startX
        self.y:int = startY
    
    def tegnSau(self, vindu: pg.Surface):
        pg.draw.circle(vindu, (0, 100, 0), (self.x, self.y), 25)


def tegnAlt(vindu: pg.Surface, spiller:Spiller, sauer:list[Sau], spokelser:list[Spokelse]):
    spiller.tegnSpiller(vindu)
    for s in sauer:
        s.tegnSau(vindu)
    for s in spokelser:
        s.tegnSpokelse(vindu)