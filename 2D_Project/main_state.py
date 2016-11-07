import random
from pico2d import *

# 06상태, main,

import game_framework
import title_state

name = "MainState"

back = None
stem = None
head = None
mario = None
seeds = None

class background:
    def __init__(self):
        self.absorb = False
        self.count = 230
        self.image = load_image('background1.png')
        self.image2 = load_image('background2.png')

    def update(self):
        self.count += 1

    def draw(self):
        if self.count % 150 >= 0 and self.count % 150 <= 80:
            self.absorb = True
            self.image2.clip_draw(0, 0, 256, 392, 275, 360, 550, 720)
        elif self.count % 150 > 80:  # and self.count % 100 < 100:
            self.absorb = False
            self.image.clip_draw(0, 0, 256, 392, 275, 360, 550, 720)


class character:
    STILL, UP, LEFT, RIGHT= 0, 1, 2, 3

    def __init__(self):
        self.absorb = False
        self.state = self.STILL
        self.chframe, self.chreframe, self.count = 0, 0, 0
        self.x, self.y = 275, 600
        self.chimage = load_image('character.png')
        self.chreimage = load_image('character_resist.png')

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            self.state = self.UP
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.state = self.LEFT
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.state = self.RIGHT
        else:
            self.state = self.STILL

    def update(self):
        self.count += 1

        if self.state == self.UP:
            self.y = min(700, self.y + 15)
        if self.state == self.LEFT:
            self.x = max(20, self.x - 10)
        if self.state == self.RIGHT:
            self.x = min(530, self.x + 10)

        if self.count % 5 == 0:
            self.chreframe += 1
        if self.chreframe % 4 == 0:
            self.chreframe = 0

        if self.absorb:
            if self.y > 140:
                self.y -= 7

    def draw(self):
        if self.absorb == False:
            self.chimage.clip_draw(self.chframe * 60, 0, 60, 160, self.x, self.y, 60, 90)
        else:
            self.chreimage.clip_draw(self.chreframe * 85, 0, 85, 160, self.x, self.y, 63, 90)


class bomb:
    boimage = None
    exploimage = None

    def __init__(self):
        self.absorb = False
        self.suck = random.randint(1, 7)
        self.x = 275
        self.y = 600
        self.boframe = random.randint(0, 10)
        self.count = random.randint(0, 9)
        if bomb.boimage == None:
            bomb.boimage = load_image('bomb.png')
        if bomb.exploimage == None:
            bomb.exploimage = load_image('explosion.png')

    def update(self):
        self.count += 1

        if self.count % 10 == 0:
            self.boframe = (self.boframe + 1) % 10

        if self.absorb:
            if self.boframe < 10:
                self.boframe = random.randint(10, 11)
            if self.count % 10 == 0:
                if self.boframe == 11:
                    self.boframe = 10
                else:
                    self.boframe = (self.boframe + 1) % 13

            if (self.suck % 3) or (self.suck % 7) == 0:
                if self.y > 140:
                    self.y -= 9

                if self.x < 280:
                    self.x += 7
                else:
                    self.x -= 7
        else:
            self.suck = random.randint(0, 7)

    def draw(self):
        self.boimage.clip_draw(self.boframe * 50, 0, 50, 60, self.x, self.y, 35, 45)


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

        if self.count % 11 == 0:
            self.legf1 += 1

        if self.legf1 % 2 == 0:
            self.legf1 = 0

        if self.count % 17 == 0:
            self.legf3 += 1

        if self.legf3 % 2 == 0:
            self.legf3 = 0

        if self.count % 23 == 0:
            self.legf4 += 1

        if self.legf4 % 3 == 0:
            self.legf4 = 1

    def draw(self):
        self.legimage1.clip_draw(self.legf1 * 100, 0, 100, 400, 50, 101, 50, 200)
        self.legimage2.draw(70, 26, 100, 50)
        self.legimage3.clip_draw(self.legf3 * 400, 0, 400, 400, 500, 116, 170, 230)
        self.legimage4.clip_draw(self.legf4 * 100, 0, 100, 240, 270, 40, 80, 100)


class flower_head:
    def __init__(self):
        self.absorb = False
        self.frame = 0
        self.abframe = 2
        self.count = 0
        self.image = load_image('flower_head.png')

    def update(self):
        self.count += 1

        if self.absorb:
            if self.count % 23 == 0:
                self.abframe += 1
                if self.abframe == 4:
                    self.abframe = 2
        else:
            if self.count % 25 == 0:
                self.frame += 1

            if self.frame % 2 == 0:
                self.frame = 0

    def draw(self):
        if self.absorb:
            self.image.clip_draw(self.abframe * 400, 0, 400, 400, 280, 160, 240, 240)
        else:
            self.image.clip_draw(self.frame * 400, 0, 400, 400, 280, 160, 240, 240)


def enter():
    global back, stem, head, mario, seeds
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
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)
        else:
            mario.handle_event(event)

    if back.absorb:
        head.absorb = True
        mario.absorb = True
        for bombs in seeds:
            bombs.absorb = True

    else:
        head.absorb = False
        mario.absorb = False
        for bombs in seeds:
            bombs.absorb = False


def update():
    back.update()
    mario.update()
    stem.update()
    for bombs in seeds:
        bombs.update()
    head.update()


def draw():
    clear_canvas()
    back.draw()
    mario.draw()
    stem.draw()
    for bombs in seeds:
        bombs.draw()
    head.draw()
    update_canvas()

    delay(0.05)