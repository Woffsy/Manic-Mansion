from __future__ import annotations
import pygame as pg
from konstanter import *

class Spiller:
    def __init__(self, startX:int, startY:int) -> None:
        self.harSau:bool = False
        self.sau:Sau|None = None
        
        self.x:int = startX
        self.y:int = startY
        self.fart:int = 3
        
    def tegnSpiller(self, vindu:pg.Surface):
        pg.draw.circle(vindu, WHITE, (self.x, self.y), 25)
    
    def flyttSpiller(self):
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
    def __init__(self, omrade:pg.Rect, startX:int, startY:int) -> None:
        self.omrade = omrade
        
        self.x:int = startX
        self.y:int = startY
    
    def tegnSpokelse(self, vindu: pg.Surface):
        pg.draw.rect(vindu, WHITE, (self.x, self.y, 100, 100))

class Sau:
    def __init__(self, startX:int, startY:int) -> None:
        self.iSafeOmrade:bool = False
        
        self.x:int = startX
        self.y:int = startY
    
    def tegnSau(self, vindu: pg.Surface):
        pg.draw.circle(vindu, (0, 0, 0), (self.x, self.y), 25)


def tegnAlt(vindu: pg.Surface, spiller:Spiller, sauer:list[Sau], spokelser:list[Spokelse]):
    spiller.tegnSpiller(vindu)
    for s in sauer:
        s.tegnSau(vindu)
    for s in spokelser:
        s.tegnSpokelse(vindu)