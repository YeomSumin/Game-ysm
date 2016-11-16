import random
from pico2d import *

import game_framework
import title_state

name = "MainState"

current_time = 0.0
change = False
moment = False
pick = False
back = None
stem = None
head = None
mario = None
seeds = None

class background:
    def __init__(self):
        self.absorb = False
        self.turn = 0
        self.sturn = 0
        self.spit = False
        self.count = 3800
        self.image = load_image('background1.png')
        self.image2 = load_image('background2.png')

    def update(self):
        self.count += 1

    def draw(self):
        if self.count % 3000 >= 0 and self.count % 3000 <= 800:
            self.absorb = True
            self.image2.clip_draw(0, 0, 256, 392, 275, 360, 550, 720)
        elif self.count % 3000 > 800:  # and self.count % 100 < 100:
            self.absorb = False
            self.image.clip_draw(0, 0, 256, 392, 275, 360, 550, 720)


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
        self.absorb = False
        self.state = self.STILL
        self.chframe, self.chreframe, self.count = 0, 0, 0
        self.total_frames, self.total_rframes = 0.0, 0.0
        self.level = 0.5
        self.stage = False
        self.x, self.y = 275, 600
        self.chimage = load_image('character.png')
        self.chreimage = load_image('character_resist.png')

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
            self.chframe = int(self.total_frames) % 10
            self.chreframe = int(self.total_rframes) % 4

        if self.absorb:
            if self.y > 140:
                self.y -= self.level

    def draw(self):
        if self.absorb == False:
            self.chimage.clip_draw(self.chframe * 60, 0, 60, 160, self.x, self.y, 56, 86) #60 90
        else:
            self.chreimage.clip_draw(self.chreframe * 85, 0, 85, 160, self.x, self.y, 60, 87) #63 90

    def get_bb(self):
        return self.x - 3, self.y - 3, self.x + 3, self.y + 3 #28 43

class bomb:
    TIME_PER_ACTION = 4
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 10

    boimage = None
    exploimage = None

    def __init__(self):
        self.absorb = False
        self.spit = False
        self.turn = False
        self.coll = False
        self.put = False
        self.explosion = False
        self.suck = random.randint(1, 7)
        self.move = 0
        self.x = 275
        self.y = 600
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
            self.put = True

    def update(self, frame_time):
        self.total_frames += bomb.FRAMES_PER_ACTION * bomb.ACTION_PER_TIME * frame_time
        self.count += 1

        if self.count % 100 == 0:
            self.boframe = int(self.total_frames + 1) % 10

        if self.put:
            if self.count % 10 == 0:
                if self.exframe == 4:
                    self.explosion = False
                self.exframe = (self.exframe + 1) % 5

        if self.absorb:
            if self.spit:
                if (self.suck % 3) == 0:
                    if self.coll == False:
                        self.y += 1
                        if (self.move % 2) == 0:
                            self.x += 3/10
                        else:
                            self.x -= 3/10

                        #self.turn = False
            else:
                self.turn = True
                self.move = random.randint(1, 5)
                if self.boframe < 10:
                    self.boframe = random.randint(10, 11)
                if self.count % 10 == 0:
                    if self.boframe == 11:
                        self.boframe = 10
                    else:
                        self.boframe = (self.boframe + 1) % 13

                if (self.suck % 3) == 0 and (self.coll == False):
                    if self.y < 720 and self.y > 140:
                        self.y -= 0.9

                    if self.x < 280:
                        self.x += 0.7
                    else:
                        self.x -= 0.7

        else:
            if self.turn == False and self.coll == False:
                self.suck = random.randint(0, 7)


    def draw(self):
        if self.explosion == True:
            self.exploimage.clip_draw(self.exframe * 120, 0, 120, 100, self.x, self.y, 60, 50)
        else:
            self.boimage.clip_draw(self.boframe * 50, 0, 50, 60, self.x, self.y, 35, 45)

    def get_bb(self):
        return self.x - 18, self.y - 28, self.x + 18, self.y + 28


def create_bombgroup():
    bombgroup_data_file = open('bomb_data.txt', 'r')
    bombgroup_data = json.load(bombgroup_data_file)
    bombgroup_data_file.close()

    bombgroup = []

    for name in bombgroup_data:
        bombs = bomb()
        bombs.name = name
        bombs.x = bombgroup_data[name]['x']
        bombs.y = bombgroup_data[name]['y']
        bombgroup.append(bombs)

    return bombgroup

def load_bombgroup():
    bombgroup_data_file = open('bomb_data.txt', 'r')
    bombgroup_data = json.load(bombgroup_data_file)
    bombgroup_data_file.close()
    """
    bombgroup = []

    for name in bombgroup_data:
        bombs = bomb()
        bombs.name = name
        bombs.x = bombgroup_data[name]['x']
        bombs.x = bombgroup_data[name]['x']
        bombs.y = bombgroup_data[name]['y']
        bombgroup.append(bombs)

    return bombgroup
    """


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


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


class flower_head:
    TIME_PER_ACTION = 4
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 2

    def __init__(self):
        self.absorb = False
        self.x = 280; self.y = 160
        self.frame = 0
        self.total_frames = 0
        self.abframe = 2
        self.count = 0
        self.image = load_image('flower_head.png')

    def update(self, frame_time):
        self.total_frames += flower_head.FRAMES_PER_ACTION * flower_head.ACTION_PER_TIME * frame_time
        self.count += 1

        if self.absorb:
            if self.count % 230 == 0:
                self.abframe += 1
                if self.abframe == 4:
                    self.abframe = 2
        else:
            if self.count % 25 == 0:
                self.frame = int(self.total_frames + 1) % 2

    def draw(self):
        if self.absorb:
            self.image.clip_draw(self.abframe * 400, 0, 400, 400, 280, 160, 240, 240)
        else:
            self.image.clip_draw(self.frame * 400, 0, 400, 400, 280, 160, 240, 240)

    def get_bb(self):
        return self.x - 130, self.y - 110, self.x + 130, self.y + 110

def get_frame_time():
    global current_time
    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def enter():
    global back, stem, head, mario, seeds, current_time

    current_time = get_time()

    back = background()
    stem = flower_leg()
    mario = character()
    seeds = create_bombgroup()
    head = flower_head()


def exit():
    global back, stem, head, mario, seeds
    del(back)
    del(stem)
    del(head)
    del(mario)
    del(seeds)


def pause():
    pass

def resume():
    pass

def handle_events():
    global change, moment, pick, seeds
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)
        else:
            mario.handle_event(event)
            for bombs in seeds:
                bombs.handle_event(event)

    if back.absorb:
        if change:
            head.absorb = True
            for bombs in seeds:
                bombs.absorb = True
                bombs.spit = True
                if collide(mario, bombs):
                    bombs.coll = True
                    bombs.x = mario.x
                    bombs.y = mario.y - 10

            moment = False
        else:
            for bombs in seeds:
                if bombs.coll and bombs.put == False:
                    bombs.x = mario.x
                    bombs.y = mario.y - 10
                if collide(head, bombs) and bombs.put:
                    bombs.explosion = True
            head.absorb = True
            mario.absorb = True
            for bombs in seeds:
                bombs.absorb = True
            moment = True
    else:
        if moment:
            change = True
            mario.absorb = False
            head.absorb = False
            for bombs in seeds:
                bombs.absorb = False
        else:
            for bombs in seeds:
                if bombs.coll:
                    bombs.x = mario.x
                    bombs.y = mario.y - 10
            head.absorb = False
            mario.absorb = False
            for bombs in seeds:
                bombs.absorb = False
                bombs.spit = False
            change = False

def update():
    global frame_time
    frame_time = get_frame_time()
    back.update()
    mario.update(frame_time)
    stem.update()
    for bombs in seeds:
        bombs.update(frame_time)
    head.update(frame_time)


def draw():
    clear_canvas()
    back.draw()
    mario.draw()
    stem.draw()
    for bombs in seeds:
        if bombs.put:
            head.draw()
            bombs.draw()
        else:
            bombs.draw()
            head.draw()
    update_canvas()