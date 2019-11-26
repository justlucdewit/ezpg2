from ezpg2 import *

def setup():
    createCanvas(600, 600)
    consoleClear()
    v1 = createVector(1, 30)
    v2 = v1.copy()
    v2.y = 20
    v2.x = 0
    print(dist(v1.x, v1.y, v2.x, v2.y))

def draw():
    pass

start(setup, draw)