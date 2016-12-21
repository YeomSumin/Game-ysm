import random

from pico2d import *

class character:
    PIXEL_PER_METER = (40.0 / 0.1)  # 40 pixel 10cm
    RUN_SPEED_KMPH = 2.5  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)  # mpm = 1분에 몇미터
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)  # MPS = 1초당 몇미터
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # PPS = pulse per second(?)

    TIME_PER_ACTION = 4
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 10
    TIME_PER_RACTION = 1
    RACTION_PER_TIME = 1.0 / TIME_PER_RACTION
    FRAMES_PER_RACTION = 4

    STILL, UP, LEFT, RIGHT = 0, 1, 2, 3

    def __init__(self):
        self.suck = False
        self.state = self.STILL
        self.chframe, self.chreframe, self.life_frame, self.count, self.life_count = 0, 0, 5, 0, 0
        self.total_frames, self.total_rframes = 0.0, 0.0
        self.level = 0.5
        self.catch = False
        self.x, self.y = 275, 600
        self.chimage = load_image('character.png')
        self.chreimage = load_image('character_resist.png')
        self.life_image = load_image('mario_life.png')

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            self.state = self.UP
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT, self.UP, self.STILL):
                self.state = self.LEFT
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.LEFT, self.UP, self.STILL):
                self.state = self.RIGHT
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT,):
                self.state = self.STILL
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT,):
                self.state = self.STILL
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            if self.state in (self.UP,):
                self.state = self.STILL


    def update(self, frame_time):
        self.distance = character.RUN_SPEED_PPS * frame_time
        self.total_frames += character.FRAMES_PER_ACTION * character.ACTION_PER_TIME * frame_time
        self.total_rframes += character.FRAMES_PER_RACTION * character.RACTION_PER_TIME * frame_time
        self.count += 1
        self.y -= 0.01

        if self.state == self.UP:
            self.y += self.distance
        if self.state == self.LEFT:
            self.x -= self.distance
        if self.state == self.RIGHT:
            self.x += self.distance

        if self.count % 100 == 0:
            #self.chframe = (self.chframe + 1) % 10
            if self.catch == False:
                self.chframe = int(self.total_frames) % 10
            self.chreframe = int(self.total_rframes) % 4

    def absorb(self):
        self.suck = True

        if self.y > 140:
            self.y -= self.level

    def spit(self):
        pass

    def catching(self):
        self.catch = True
        self.chframe = 0

    def life_minus(self):
        pre_life = self.life_frame

        if self.life_frame == pre_life and self.life_count == 0:
            self.life_frame -= 1;
            self.life_count += 1

    def draw(self):
        self.life_image.clip_draw(0, self.life_frame * 90, 400, 90, 267, 690, 300, 48)  # 268 691 300 50

        if self.suck == False:
            self.chimage.clip_draw(self.chframe * 60, 0, 60, 160, self.x, self.y, 56, 86) #60 90
        else:
            self.chreimage.clip_draw(self.chreframe * 85, 0, 85, 160, self.x, self.y, 60, 87) #63 90

    def get_bb(self):
        return self.x - 3, self.y - 3, self.x + 3, self.y + 3 #28 43