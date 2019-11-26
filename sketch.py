from ezpg2 import *

def setup():
    createCanvas(600, 600)
    consoleClear()
    v1 = createVector(0, 30)
    v2 = v1.copy()
    v2.y = 20
    print(v1.toString())
    print(v2.toString())

def draw():
    pass

start(setup, draw)