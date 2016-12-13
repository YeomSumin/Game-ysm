import random

from pico2d import *

class bomb:
    TIME_PER_ACTION = 4
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 10

    boimage = None
    exploimage = None

    def __init__(self):
        self.turn = False
        self.coll = False
        self.put = False
        self.z = False
        self.catch = False
        self.catching = False
        self.explosion = False
        self.suck = random.randint(1, 6)
        self.dir = 0
        self.x = 0
        self.y = 0
        self.originx = 0
        self.originy = 0
        self.total_frames = 0
        self.boframe = random.randint(0, 10)
        self.exframe = 0
        self.count = random.randint(0, 9)
        if bomb.boimage == None:
            bomb.boimage = load_image('bomb.png')
        if bomb.exploimage == None:
            bomb.exploimage = load_image('explosion.png')


    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
            self.coll = False
            #self.put = True

            if self.catching:
                self.catch = False
                #self.put = True
            else:
                self.z = True
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_z):
            self.z = False


    def absorb(self, frame_time):
        self.total_frames += bomb.FRAMES_PER_ACTION * bomb.ACTION_PER_TIME * frame_time
        self.turn = True
        #self.dir = random.randint(1, 5)
        if self.boframe < 10:
            self.boframe = random.randint(10, 11)
        if self.count % 100 == 0:
            if self.boframe == 11:
                self.boframe = 10
            else:
                self.boframe = (self.boframe + 1) % 13

        if (self.suck % 3) == 0: #and (self.coll == False):
            if self.y < 720 and self.y > 140:
                self.y -= 0.9

            if self.x < 280:
                self.x += 0.4
            else:
                self.x -= 0.4

    def spit(self):
        if (self.suck % 3) == 0:
            #if self.coll == False:
            if self.explosion == False:
                self.y += 1
                if (self.dir % 2) == 0:
                    self.x += 3 / 10
                else:
                    self.x -= 3 / 10

    def caught(self):
        if self.z:
            self.catch = True
            self.catching = True

    def no_catching(self):
        self.catching = False

    def re_position(self):
        self.x = self.originx
        self.y = self.originy

    def re_random(self):
        self.suck = random.randint(1, 6)

    def update(self, frame_time, mario):
        self.total_frames += bomb.FRAMES_PER_ACTION * bomb.ACTION_PER_TIME * frame_time
        self.count += 1

        if self.count % 100 == 0:
            self.boframe = int(self.total_frames + 1) % 10

        if self.explosion:
            if self.count % 10 == 0:
                if self.exframe < 6:
                    self.exframe += 1

                    if self.exframe == 5:
                        self.explosion = None

        if self.catch:
            self.x = mario.x
            self.y = mario.y - 10

    def explode(self):
        self.explosion = True

    def unexplode(self):
        self.put = False
        self.explosion = False

    def draw(self):
        if self.explosion == True:
            self.exploimage.clip_draw(self.exframe * 120, 0, 120, 100, self.x, self.y, 70, 60) #60 50
        else:
            self.boimage.clip_draw(self.boframe * 50, 0, 50, 60, self.x, self.y, 35, 45)

    def get_bb(self):
        return self.x - 18, self.y - 28, self.x + 18, self.y + 28