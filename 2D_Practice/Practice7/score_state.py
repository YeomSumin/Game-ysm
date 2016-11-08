import game_framework
import json
from pico2d import *

import main_state
import title_state

name = "ScoreState"
image = None
Boy = None
font = None

class Boy:
    x = 0
    life_time = 0.0

def enter():
    global image, font
    font = load_font('ENCR10B.TTF')
    image = load_image('blackboard.png')

def exit():
    global image
    #del(image)

def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)

def update(frame_time):
    pass

def draw(frame_time):
    global image, font
    clear_canvas()
    image.draw(400, 300)

    [Boy.x, Boy.life_time] = [0, 0.0]
    f = open('save.txt', 'r')
    [Boy.x, Boy.life_time] = json.load(f)
    f.close()
    font.draw(10, 550, 'Position: %d, Time: %3.2f' %(Boy.x, Boy.life_time))

    update_canvas()