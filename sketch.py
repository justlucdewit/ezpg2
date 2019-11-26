from ezpg2 import *

def setup():
    createCanvas(600, 600)

def draw():
    print(f"current fps: {frameRate()}")

start(setup, draw)