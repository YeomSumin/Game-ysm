from pico2d import *
import math

def handle_events():
    global running
    global x, y, rx, middlex, middley
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            show_cursor()
            middlex, middley = event.x, event.y
        elif event.key == SDLK_UP:
            hide_cursor()
            middley = middley - 20
        elif event.key == SDLK_DOWN:
            hide_cursor()
            middley = middley + 20
        elif event.key == SDLK_LEFT:
            hide_cursor()
            middlex = middlex - 20
        elif event.key == SDLK_RIGHT:
            hide_cursor()
            middlex = middlex + 20
        elif event.key == SDLK_a:
            rx = min(rx + 20, 300)
        elif event.key == SDLK_d:
            rx = max(rx - 20, 20)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

running = True
x, y = 100, 100
middlex, middley = 400, 300
rx = 100
roll = 0
frame = 0
while (running):
    clear_canvas()
    grass.draw(400, 30)
    roll = ((roll + 0.2) % 360)
    x, y = middlex + rx * math.sin(roll), 600 - middley + rx * math.cos(roll)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.05)
    handle_events()

close_canvas()




