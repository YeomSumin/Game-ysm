import game_framework
import title_state
from pico2d import *

name = "StartState"
image = None
logo_time = 0.0

def enter(): #게임 상태에 들어올 때 초기화
    global image
    open_canvas(550, 720)
    image = load_image('kpu_credit.png')

def exit(): #게임 상태에서 나갈때 종료화
    global image
    del(image)
    close_canvas

def update():
    global logo_time

    if (logo_time > 1.0):
        logo_time = 0
        game_framework.push_state(title_state)
        #게임 상태를 title_state로 변화. 이전 게임 상태는 남아 있음

    delay(0.01)
    logo_time += 0.01

def draw():
    global image
    clear_canvas()
    image.clip_draw(120, 0, 520, 600, 275, 360, 550, 720)
    update_canvas()

def handle_events():
    events = get_events()
    pass

def pause(): pass

def resume(): pass