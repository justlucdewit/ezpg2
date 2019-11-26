from ezpg2 import *

def setup():
    createCanvas(600, 600)
    consoleClear()
    print(mouseX, mouseY)

def draw():
    x = mapping(mouseX(), 0, width(), 0, 255)
    y = mapping(mouseY(), 0, height(), 0, 255)
    background(x, y, 255)
    #print(frameRate())

start(setup, draw)