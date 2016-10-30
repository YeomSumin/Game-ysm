import random
from pico2d import *

class background:
    def __init__(self):
        self.absorb = False
        self.count = 230;
        self.image = load_image('background1.png')
        self.image2 = load_image('background2.png')

    def update(self):
        self.count += 1

    def draw(self):
        if self.count % 150 >= 0 and self.count % 150 <= 80:
            self.absorb = True
            self.image2.clip_draw(0, 0, 256, 392, 275, 360, 550, 720)
        elif self.count % 150 > 80: #and self.count % 100 < 100:
            self.absorb = False
            self.image.clip_draw(0, 0, 256, 392, 275, 360, 550, 720)

class character:
    def __init__(self):
        self.absorb = False
        self.chframe = 0; self.chreframe = 0; self.count = 0
        self.x = 0; self.y = 0;
        self.chimage = load_image('character.png')
        self.chreimage = load_image('character_resist.png')

    def update(self):
        self.count += 1

        if self.count % 5 == 0:
            self.chframe += 1
            self.chreframe += 1

        if self.chframe % 10 == 0:
            self.chframe = 0

        if self.chreframe % 4 == 0:
            self.chreframe = 0

    def draw(self):
        if self.absorb == False:
            self.chimage.clip_draw(self.chframe * 60, 0, 60, 160, 275 + 1 * self.x, 600 + 1 * self.y, 60, 90)
        else:
            self.chreimage.clip_draw(self.chreframe * 85, 0, 85, 160, 275 + 1 * self.x, 600 + 1 * self.y, 63, 90)

class bomb:
    boimage = None

    def __init__(self):
        self.x = 0; self.y = 0
        self.boframe = 0; self.count = 0
        if bomb.boimage == None:
            bomb.boimage = load_image('bomb.png')
        self.exploimage = load_image('explosion.png')

    def update(self):
        self.count += 1

        if self.count % 10 == 0:
            self.boframe += 1

        if self.boframe % 10 == 0:
            self.boframe = 0

    def draw(self):
        self.boimage.clip_draw(self.boframe * 50, 0, 50, 60, 275 + 1 * self.x, 600 + 1 * self.y, 35, 45)

class flower_leg:
    def __init__(self):
        self.count = 0
        self.legf1 = 0; self.legf3 = 0; self.legf4 = 1
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
        self.frame = 0; self.abframe = 2
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

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            char.y += 15
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            char.x -= 8
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            char.x += 8

    if back.absorb:
        fhead.absorb = True
        char.absorb = True
        if 600 + 1 * char.y > 140:
            char.y -= 7
    else:
        fhead.absorb = False
        char.absorb = False


open_canvas(550, 720)

running = True;

back = background()
fleg = flower_leg()
fhead = flower_head()
char = character()
bomb = bomb()

while running:
    handle_events()

    back.update()
    char.update()
    fleg.update()
    fhead.update()
    bomb.update()

    clear_canvas()
    back.draw()
    char.draw()
    fleg.draw()
    fhead.draw()
    bomb.draw()
    update_canvas()

    delay(0.05)

close_canvas()