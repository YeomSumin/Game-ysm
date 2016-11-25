import random
from pico2d import *

import game_framework
import title_state

from back import background
from mario import character
from seeds import bomb
from head import flower_head
from stem import flower_leg

name = "MainState"

current_time = 0.0
back = None
stem = None
head = None
mario = None
seeds = None


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


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


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

    if back.wind:
        if back.state == back.ABSORB:
            head.open()
            mario.absorb()
            for bombs in seeds:
                bombs.absorb()
                if collide(bombs, head):
                    head.spit = True

        elif back.state == back.SPIT:
            head.open()
            # mario.spit()
            for bombs in seeds:
                bombs.spit()
            if head.spit:
                for bombs in seeds:
                    if collide(mario, bombs):
                        bombs.explode()
                        mario.life_minus()
                        back.change = 0
                    elif bombs.catch:
                        bombs.caught()
            else:
                mario.spit()
                mario.life_minus()
                back.change = 0

        elif back.state == back.A_ABSORB:
            head.open()
            mario.absorb()
            if collide(mario, head):
                head.spit = False
                back.change = 2

            for bombs in seeds:
                if collide(bombs, head):
                    bombs.explode()
                    head.life_minus()
    else:
        mario.suck = False
        head.state = head.CLOSE

        if back.state == back.NOT:
            back.state = back.ABSORB
"""
        if back.state == back.ABSORB:
            back.state = back.SPIT

        if back.state == back.SPIT:
            if back.change == 0:
                back.state = back.NOT
            back.state = back.A_ABSORB

        if back.state == back.A_ABSORB:
            if back.change == 2:
                back.state = back.SPIT
            back.state = back.ABSORB
"""


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