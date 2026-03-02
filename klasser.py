from __future__ import annotations
import pygame as pg
from konstanter import *
import random
import math

class Spiller:
    def __init__(self, startX:int, startY:int) -> None:
        self.img = pg.image.load(IMAGE_DIR/"farmer.png")
        self.img = pg.transform.scale(self.img, (150, 150))
        self.harSau:bool = False
        self.sau:Sau|None = None
        
        self.startX: int = startX
        self.startY: int = startY
        
        self.x:int = startX
        self.y:int = startY
        self.fart:int = 6
        
    def tegnSpiller(self, vindu:pg.Surface):
        rect = self.img.get_rect(center=(self.x, self.y))
        vindu.blit(self.img, rect)
        if self.sau:
            self.sau.x = self.x
            self.sau.y = self.y
    
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


    def plukkOppSau(self, sauer: list[Sau]) -> None:
        for s in sauer:
            if not self.sau and not s.iSafeOmrade and math.sqrt((self.x-s.x)**2+(self.y-s.y)**2) < 25:
                self.sau = s
    
    def leggFraSau(self) -> None:
        if self.sau and self.x<SAFE_BREDDE:
            self.sau.iSafeOmrade = True
            self.sau = None
    
    def sjekkSpokelseKollisjon(self, spokelser: list[Spokelse]):
        spiller_rect = self.img.get_rect(center=(self.x, self.y))
        for s in spokelser:
            spokelse_rect = pg.Rect(s.x, s.y, s.str, s.str)
            if spiller_rect.colliderect(spokelse_rect):
                self.sau = None
                self.x = self.startX
                self.y = self.startY
    
    def oppdaterSpiller(self, sauer: list[Sau], spokelser: list[Spokelse]):
        self.plukkOppSau(sauer)
        self.leggFraSau()
        self.sjekkSpokelseKollisjon(spokelser)

class Spokelse:
    def __init__(self, safezones:list[pg.Rect], startX:int, startY:int) -> None:
        self.safezones = safezones
        self.fart = random.randint(2, 5)
        self.retningX = random.choice([-1, 1])
        self.retningY = random.choice([-1, 1])
        
        self.str: int = 100
        
        self.x:int = startX
        self.y:int = startY

    def tegnSpokelse(self, vindu: pg.Surface):
        pg.draw.rect(vindu, WHITE, (self.x, self.y, self.str, self.str))
    
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
        self.img = pg.image.load(IMAGE_DIR/"sheep.png")
        self.img = pg.transform.scale(self.img, (100, 100))
        self.iSafeOmrade:bool = False
        
        self.x:int = startX
        self.y:int = startY
    
    def tegnSau(self, vindu: pg.Surface):
        rect = self.img.get_rect(center=(self.x, self.y))
        vindu.blit(self.img, rect)
        


def tegnAlt(vindu: pg.Surface, spiller:Spiller, sauer:list[Sau], spokelser:list[Spokelse]):
    spiller.tegnSpiller(vindu)
    for s in sauer:
        s.tegnSau(vindu)
    for s in spokelser:
        s.tegnSpokelse(vindu)
        
def oppdaterAlt(vindu:pg.Surface, spiller: Spiller, sauer: list[Sau], spokelser: list[Spokelse]):
    tegnAlt(vindu, spiller, sauer, spokelser)
    spiller.oppdaterSpiller(sauer, spokelser)