import random

from pico2d import *

class background:

    NOT, ABSORB, SPIT, A_ABSORB = 0, 1, 2, 3

    def __init__(self):
        self.wind = False
        self.state = self.NOT
        self.change = None
        self.count = 2300
        self.image = load_image('background1.png')
        self.image2 = load_image('background2.png')

    def update(self):
        self.count += 1

    def draw(self):
        if self.count % 1500 >= 0 and self.count % 1500 <= 800:
            self.wind = True
            self.image2.clip_draw(0, 0, 256, 392, 275, 360, 550, 720)
        elif self.count % 1500 > 800:
            self.wind = False
            self.image.clip_draw(0, 0, 256, 392, 275, 360, 550, 720)