import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None


def enter():
    global image
    image = load_image('gamestart.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)
                # 게임 상태를 main_state로 변화. 이전 게임 상태를 완전히 나옴


def draw():
    clear_canvas()
    image.clip_draw(0, 0, 800, 600, 275, 360, 550, 720)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






