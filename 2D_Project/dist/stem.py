import random

from pico2d import *

class flower_leg:
    def __init__(self):
        self.count = 0
        self.legf1 = 0
        self.legf3 = 0
        self.legf4 = 1
        self.legimage1 = load_image('flower_leg.png')
        self.legimage2 = load_image('flower_leg2.png')
        self.legimage3 = load_image('flower_leg3.png')
        self.legimage4 = load_image('flower_leg4.png')

    def update(self):
        self.count += 1

        if self.count % 110 == 0:
            self.legf1 = (self.legf1 + 1) % 2

        if self.count % 170 == 0:
            self.legf3 = (self.legf3 + 1) % 2

        if self.count % 230 == 0:
            self.legf4 = (self.legf4 + 1) % 3

    def draw(self):
        self.legimage1.clip_draw(self.legf1 * 100, 0, 100, 400, 50, 101, 50, 200)
        self.legimage2.draw(70, 26, 100, 50)
        self.legimage3.clip_draw(self.legf3 * 400, 0, 400, 400, 500, 116, 170, 230)
        self.legimage4.clip_draw(self.legf4 * 100, 0, 100, 240, 270, 40, 80, 100)