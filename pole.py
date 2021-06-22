import pygame
from pygame import draw
import random

class pole:
    def __init__(self,screen ):
        self.height=random.randint(100,500)
        self.width = 20
        self.x=750
        self.y=750-self.height
        self.vy=100
        self.ay=9.81
        self.t =1/120
        self.screen=screen
        self.color=[255,158,130]
        self.r=10
        self.speed=random.uniform(0.8,3)

    def render(self):
        draw.rect(self.screen,self.color,(self.x,self.y,self.width,self.height))

    def update(self):
        self.x-=self.speed
    def new_pole(self):
        self.height=random.randint(50,600)
        self.width = 20
        self.x=750
        self.y=750-self.height
        self.speed=random.uniform(0.8,3)