import pygame as pg
from os import system
from time import time
from helpers.ezvector import *
from helpers.math import *

pg.init()

canvas = None                   #holds the canvas object
clock = pg.time.Clock()         #clock object
fillcolor = (255, 255, 255)     #holds the drawing fill color
strokecolor = (0, 0, 0)         #holds the drawing edge color
launchTime = time()             #holds the timestamp of launch
frameCountVar = 0               #holds number of passed frames
xtranslation = 0                #x offset for drawing
ytranslation = 0                #y offset for drawing
frameCap = 60                   #capped framerate
windowWidth = 0                 #width of the window
windowHeight = 0                #height of the window

def start(setupFunction, df):
    setupFunction()
    while True:
        df()
        update()

def update():
    pg.display.flip()
    global frameCountVar
    frameCountVar += 1
    clock.tick(frameCap)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

def createCanvas(width, height):
    global canvas
    global windowWidth
    global windowHeight
    windowWidth = width
    windowHeight = height
    canvas = pg.display.set_mode((width, height))
    pg.display.set_caption("sketch")

def setTitle(title):
    pg.display.set_caption(title)

def frameCount():
    return frameCountVar

def frameRate(fr=None):
    if fr == None:
        return clock.get_fps()
    else:
        global frameCap
        frameCap = fr

def consoleClear():
    system("cls")

def background(r, g, b):
	canvas.fill((constrain(r, 0, 255),constrain(g, 0, 255),constrain(b, 0, 255)))

def mouseX():
    return pg.mouse.get_pos()[0]

def mouseY():
    return pg.mouse.get_pos()[1]

def width():
    return windowWidth

def height():
    return windowHeight