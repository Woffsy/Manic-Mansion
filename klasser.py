from __future__ import annotations
import pygame as pg
from konstanter import *
import random

class Spiller:
    def __init__(self, startX:int, startY:int) -> None:
        self.img = pg.image.load(IMAGE_DIR/"farmer.png")
        self.img = pg.transform.scale(self.img, (125, 125))
        self.imgSauFarmer = pg.image.load(IMAGE_DIR/"farmerAndSheep.png")
        self.imgSauFarmer = pg.transform.scale(self.imgSauFarmer, (125,125))
        self.harSau:bool = False
        self.sau:Sau|None = None
        
        self.startX: int = startX
        self.startY: int = startY
        
        self.x:int = startX
        self.y:int = startY
        self.fart:int = 6
        
        self.liv:int = 3
        self.poeng:int = 0
        
        self.spiller_rect = self.img.get_rect(center=(self.x, self.y))
        
        
    def tegnSpiller(self, vindu:pg.Surface):
        if self.sau:
            rect = self.imgSauFarmer.get_rect(center=(self.x,self.y))
            self.sau.x = self.x
            self.sau.y = self.y
            vindu.blit(self.imgSauFarmer, rect)
            self.spiller_rect = self.img.get_rect(center=(self.x, self.y))
            
        else:
            rect = self.img.get_rect(center=(self.x, self.y))
            vindu.blit(self.img, rect)
            self.spiller_rect = self.img.get_rect(center=(self.x, self.y))
      
    
    def flyttSpiller(self, hinder:list[Hinder]):
        self.x = max(25, min(self.x, VINDU_BREDDE - 25))
        self.y = max(25, min(self.y, VINDU_HOYDE - 25))
        taster: tuple[bool, ...] = pg.key.get_pressed()
        dx = 0
        dy = 0
        if taster[pg.K_LEFT]:
            dx -= self.fart
        if taster[pg.K_RIGHT]:
            dx += self.fart
        if taster[pg.K_UP]:
            dy -= self.fart
        if taster[pg.K_DOWN]:
            dy += self.fart

        self.x += dx
        self.y += dy
        self.spiller_rect.x += dx
        self.spiller_rect.y += dy
        krasj = False
        
        for h in hinder:
            if self.spiller_rect.colliderect(h.rect):
                krasj = True
                break
        if krasj:
            self.x -= dx
            self.y -= dy
            self.spiller_rect.x -= dx
            self.spiller_rect.y -= dy

    def plukkOppSau(self, sauer: list[Sau]) -> None:
        for s in sauer:
            if not self.sau and not s.iSafeOmrade and self.spiller_rect.colliderect(s.rect):
                self.sau = s
                self.sau.plukketOpp = True
                self.fart = 4
    
    def leggFraSau(self) -> bool:
        if self.sau and self.x<SAFE_BREDDE:
            self.sau.iSafeOmrade = True
            self.sau.plukketOpp = False
            self.sau = None
            self.poeng += 1
            self.fart = 6
            return True
        return False

    
    def sjekkSpokelseKollisjon(self, spokelser: list[Spokelse]):
        for s in spokelser:
            spokelse_rect = pg.Rect(s.x, s.y, s.str, s.str)
            if self.spiller_rect.colliderect(spokelse_rect):
                if self.sau:
                    self.sau.plukketOpp = False
                self.sau = None
                self.x = self.startX
                self.y = self.startY
                self.liv -= 1
                self.fart = 6
                
    
    def oppdaterSpiller(self, sauer: list[Sau], spokelser: list[Spokelse]):
        self.plukkOppSau(sauer)
        self.sjekkSpokelseKollisjon(spokelser)
        return self.leggFraSau()

class Spokelse:
    def __init__(self, safezones:list[pg.Rect], startX:int, startY:int) -> None:
        self.img = pg.image.load(IMAGE_DIR/"spokelse.png")
        self.img = pg.transform.scale(self.img, (100, 100))
        self.safezones = safezones
        self.fartX = random.randint(2, 5)
        self.fartY = random.randint(2, 5)
        self.retningX = random.choice([-1, 1])
        self.retningY = random.choice([-1, 1])
        
        self.str: int = 100
        
        self.x:int = startX
        self.y:int = startY

    def tegnSpokelse(self, vindu: pg.Surface):
        rect = self.img.get_rect(center=(self.x, self.y))
        vindu.blit(self.img, rect)
    
    def trefferSafezone(self, rect: pg.Rect):
        for sone in self.safezones:
            if rect.colliderect(sone):
                return True
            return False
    
    def flyttSpokelse(self):
        self.x += self.retningX * self.fartX

        if self.x < SAFE_BREDDE:
            self.fartX = random.randint(2, 5)
            self.fartY = random.randint(2, 5)
            self.x = SAFE_BREDDE
            self.retningX *= -1

        if self.x > VINDU_BREDDE - SAFE_BREDDE - 100:
            self.fartX = random.randint(2, 5)
            self.fartY = random.randint(2, 5)
            self.x = VINDU_BREDDE - SAFE_BREDDE - 100
            self.retningX *= -1
        
        self.y += self.retningY * self.fartY
       
        if self.y <= 0 or self.y >= VINDU_HOYDE - 100:
            self.fartX = random.randint(2, 5)
            self.fartY = random.randint(2, 5)
            self.y -= self.retningY * self.fartY
            self.retningY *= -1

class Sau:
    def __init__(self, startX:int, startY:int) -> None:
        self.img = pg.image.load(IMAGE_DIR/"sheep.png")
        self.img = pg.transform.scale(self.img, (100, 100))
        self.iSafeOmrade:bool = False
        self.plukketOpp:bool = False
        
        self.x:int = startX
        self.y:int = startY
    
        self.rect:pg.Rect = self.img.get_rect(center=(self.x, self.y))
        
    def tegnSau(self, vindu: pg.Surface):
        if not self.plukketOpp:
            self.rect = self.img.get_rect(center=(self.x, self.y))
            vindu.blit(self.img, self.rect)
            
class Hinder:
    def __init__(self, vindu: pg.Surface) -> None:
        self.vindu = vindu
        
        self.omradeLeft = SAFE_BREDDE
        self.omradeRight = VINDU_BREDDE-2*SAFE_BREDDE
        self.omradeTop = 0
        self.omradeBottom = VINDU_HOYDE
        
        self.bredde = 35
        self.hoyde = 90
        
        self.x = random.randint(self.omradeLeft, self.omradeRight)
        self.y = random.randint(self.omradeTop, self.omradeBottom)
        
        self.rect = pg.Rect(self.x, self.y, self.bredde, self.hoyde)

    def tegnHinder(self):
        pg.draw.rect(self.vindu, BROWN, self.rect)

def tegnAlt(vindu: pg.Surface, spiller:Spiller, sauer:list[Sau], spokelser:list[Spokelse], hinder:list[Hinder]):
    spiller.tegnSpiller(vindu)
    for s in sauer:
        s.tegnSau(vindu)
    for s in spokelser:
        s.tegnSpokelse(vindu)
    for h in hinder:
        h.tegnHinder()
        
def oppdaterAlt(vindu:pg.Surface, spiller: Spiller, sauer: list[Sau], spokelser: list[Spokelse], hinder: list[Hinder]):
    tegnAlt(vindu, spiller, sauer, spokelser, hinder)
    return spiller.oppdaterSpiller(sauer, spokelser)
    