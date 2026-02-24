import pygame as pg
from konstanter import *

class Spiller:
    def __init__(self) -> None:
        self.harSau:bool = False

    def plukkOppSau(self) -> None:
        if self.harSau:
            pass
        else:
            self.harSau = True

class Spokelse:
    def __init__(self, omrade:pg.Rect) -> None:
        self.omrade = omrade

class Sau:
    def __init__(self) -> None:
        self.iSafeOmrade:bool = False