import random

from pico2d import *

class flower_head:

    CLOSE, OPEN = 0, 1

    TIME_PER_ACTION = 4
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 2

    def __init__(self):
        self.state = self.CLOSE
        self.spit = False
        self.level_up = False
        self.x = 280; self.y = 160
        self.frame, self.life_frame, self.life_count = 0, 3, 0
        self.total_frames = 0
        self.abframe = 2
        self.count = 0
        self.image = load_image('flower_head.png')
        self.life_image = load_image('flower_life3.png')

    def update(self, frame_time):
        self.total_frames += flower_head.FRAMES_PER_ACTION * flower_head.ACTION_PER_TIME * frame_time
        self.count += 1

        if self.state == self.OPEN:
            if self.count % 230 == 0:
                self.abframe += 1
                if self.abframe == 4:
                    self.abframe = 2
        else:
            if self.count % 25 == 0:
                self.frame = int(self.total_frames + 1) % 2

    def open(self):
        self.state = self.OPEN

    def close(self):
        self.state = self.CLOSE

    def life_minus(self):
        pre_life = self.life_frame

        if self.life_frame == pre_life and self.life_count == 0:
            self.life_frame -= 1;
            self.life_count += 1

        if self.life_frame == 0:
            self.level_up = True
            self.life_frame = 3

    def draw(self): # 280, 160, 240, 240
        if self.state == self.OPEN:
            self.image.clip_draw(self.abframe * 400, 0, 400, 400, 280, 100, 260, 260)
        else:
            self.image.clip_draw(self.frame * 400, 0, 400, 400, 280, 100, 260, 260)

        self.life_image.clip_draw(0, self.life_frame * 90, 270, 90, 270, 30, 200, 50)
        #267, 20, 200, 48

    def get_bb(self): # 130 110 130 110
        return self.x - 130, self.y - 110, self.x + 130, self.y + 110