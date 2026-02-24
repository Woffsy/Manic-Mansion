from __future__ import annotations
import pygame as pg
from konstanter import *

class Spiller:
    def __init__(self, startX:int, startY:int) -> None:
        self.harSau:bool = False
        self.sau:Sau|None = None
        
        self.x:int = startX
        self.y:int = startY
        

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

class Sau:
    def __init__(self, startX:int, startY:int) -> None:
        self.iSafeOmrade:bool = False
        
        self.x:int = startX
        self.y:int = startY
