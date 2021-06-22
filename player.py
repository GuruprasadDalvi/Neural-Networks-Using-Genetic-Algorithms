import random
import pygame
import math
from nNet import nNetwork

class player:
    '''
        Player Class Which Takes Decision To Jump Based on Neural Network
    '''
    def __init__(self,screen ):
        self.x=50
        self.y=750
        self.vy=100
        self.ay=9.81
        self.t =1/120
        self.jumping=False
        self.screen=screen
        self.color=[random.randint(0,255),158,random.randint(0,255)]
        self.r=10
        self.brain = nNetwork([3,3,3,2])
        self.alive= True
        self.enegry=0
        self.jump_prob=0
        self.score=0


    def render(self):
        pygame.draw.circle(self.screen,self.color,(self.x,self.y),self.r)

    def update(self,pole):
        if self.check_collison(pole) or self.y<-10:
            self.alive=False
        self.jump(pole)

    def check_collison(self,pole):
        '''Collision Detection Code for pole and player'''
        return (self.x>pole.x) and (self.x < pole.x+pole.width) and (self.y>pole.y)

    def jump(self,pole):
        '''
            Jumping Logic code 
        '''
        if not self.jumping :
            preds= self.brain.predict([pole.height,math.sqrt((self.x-pole.x)**2),pole.speed])
            self.enegry=float(preds[0])
            self.jump_prob=float(preds[1])
            self.jumping=self.jump_prob>0.5

        if self.jumping and self.vy>=-100 :
            self.y-=self.vy*self.enegry
            self.vy-=1
            if self.vy< -100:
                self.jumping=False
                self.vy=100
    def mutate(self):
        '''Mutate Color and Neural network of player'''
        self.brain.mutate()
        if random.randint(0,50)<10:
            self.color[0]=(self.color[0]+random.randint(5,50))%256
        
        if random.randint(0,50)<10:
           self.color[1]=(self.color[1]+random.randint(5,50))%256
        
        if random.randint(0,50)<10:
           self.color[2]=(self.color[2]+random.randint(5,50))%256
    def crossover(self,partner):
        b=self.brain.crossover(partner.brain)
        child= player(self.screen)
        child.brain= b
        child.color=self.color
        return child

    def save(self):
        self.brain.save(self.score)