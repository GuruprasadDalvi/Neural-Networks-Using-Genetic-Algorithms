import random
from pole import pole
from player import player
from pygame import display,event,key,K_SPACE,font
import time

global dead_counter, saved_score

wid, hei = 800, 800
screen = display.set_mode((wid, hei))
bg_color=[0,0,0]
screen.fill(bg_color)
players=[]
population=[]
population_cont=200
mutation_rate =70
genration=1
dead_counter=0
saved_score=0

font.init()
def get_score(p):
    return p.score

for i in range(population_cont):
    players.append(player(screen))
pl= pole(screen)


def new_genration():
    global saved_score
    players.sort(key=get_score,reverse=True)
    best = players[:5]
    new_gen=[]
    if best[0].score>saved_score:
        best[0].save()
        saved_score=best[0].score
    for i in range(population_cont):
        a = best[random.randint(0,len(best)-1)]
        b = best[random.randint(0,len(best)-1)]
        c = a.crossover(b)
        if random.randint(1,100)<mutation_rate:
            c.mutate()
        new_gen.append(c)
    print(f"Genration {genration} Best Score: {best[0].score} ")
    return new_gen


def render():
    global dead_counter
    screen.fill(bg_color)
    for p in players:
        if p.alive:
            p.render()
    pl.render()
    fot = font.Font('freesansbold.ttf', 32)
    text = fot.render(f'Alive: {population_cont - dead_counter} Genration: {genration} Best Score: {saved_score} ', True, [255,255,0], [0,0,255])
    textRect = text.get_rect()
    textRect.center = (wid // 2, 100)
    screen.blit(text, textRect)
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
    update()
    render()
    if dead_counter>199:
        players =new_genration()
        pl.new_pole()
        genration+=1
    dead_counter=0
    time.sleep(.005)