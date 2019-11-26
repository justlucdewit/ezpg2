from ezpg2 import *

def setup():
    createCanvas(600, 600)
    frameRate(30)

def draw():
    print(f"current fps: {frameRate()}")

start(setup, draw)