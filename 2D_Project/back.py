import random

from pico2d import *

class background:
    def __init__(self):
        self.still = True
        self.absorb = False
        self.spit = False
        self.a_absorb = False
        self.count = 2300
        self.image = load_image('background1.png')
        self.image2 = load_image('background2.png')

    def update(self):
        self.count += 1

    def draw(self):
        if self.count % 1500 >= 0 and self.count % 1500 <= 800:
            if self.still:
                self.absorb = True
                self.still = False
            if self.absorb:
                self.image2.clip_draw(0, 0, 256, 392, 275, 360, 550, 720)
            if self.spit:
                self.image2.clip_draw(0, 0, 256, 392, 275, 360, 550, 720)
            if self.a_absorb:
                self.image2.clip_draw(0, 0, 256, 392, 275, 360, 550, 720)
        elif self.count % 1500 > 800:
            self.image.clip_draw(0, 0, 256, 392, 275, 360, 550, 720)