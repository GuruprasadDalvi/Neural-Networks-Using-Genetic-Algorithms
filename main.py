import random
from pole import pole
from player import player
from pygame import display,event,key,K_SPACE
import time

global dead_counter

wid, hei = 800, 800
screen = display.set_mode((wid, hei))
bg_color=[0,0,0]
screen.fill(bg_color)
players=[]
population=[]
mutation_rate =70
genration=1
dead_counter=0

def get_score(p):
    return p.score

for i in range(200):
    players.append(player(screen))
pl= pole(screen)


def new_genration():
    players.sort(key=get_score,reverse=True)
    best = players[:5]
    new_gen=[]
    for i in range(200):
        a = best[random.randint(0,len(best)-1)]
        b = best[random.randint(0,len(best)-1)]
        c = a.crossover(b)
        if random.randint(1,100)<mutation_rate:
            c.mutate()
        new_gen.append(c)
    print(f"Genration {genration} Best Score: {best[0].score} ")
    return new_gen


def render():
    screen.fill(bg_color)
    for p in players:
        if p.alive:
            p.render()
    pl.render()
    display.update()


def update():
    global dead_counter
    # pressed = key.get_pressed()
    # if pressed[K_SPACE] and not p.jumping:
    #     p.jumping=True
    if pl.x<0:
        pl.new_pole()
        for p in players:
            if p.alive:
                p.score+=1
    for p in players:
        if p.alive:
            p.update(pl)
        else:
            dead_counter+=1
    pl.update()
    event.get()
while True:
    render()
    update()
    if dead_counter>199:
        players =new_genration()
        pl.new_pole()
        genration+=1
    dead_counter=0
    time.sleep(.005)