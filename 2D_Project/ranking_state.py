import game_framework
from pico2d import *

import main_state
import title_state

name = "RankingState"
image = None
font = None

def enter():
    global image, font
    image = load_image('blackboard.png')
    font = load_font('ENCR10B.TTF', 40)


def exit():
    global image, font
    del (image)
    del (font)


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
    global image

    clear_canvas()
    image.draw(400, 300)
    font.draw(300, 500, "[RANKING]", (255, 255, 255))
    draw_ranking()
    update_canvas()


def draw_ranking():
    def my_sort(a):
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i]['time'] < a[j]['time']:
                    a[i], a[j] = a[j], a[i]

    f = open('ranking_data.txt', 'r')
    ranking_data = json.load(f)
    f.close()

    print('[RANKING]')
    my_sort(ranking_data)

    for data in ranking_data[:10]:
        print('(Time:%4.1f,  x:%3d,  y:%3d)' % (data['time'], data['x'], data['y']))

    y = 0

    for data in ranking_data[:10]:
        font.draw(150, 450 - 40 * y, 'Time:%4.1f, x:%3d, y:%3d' % (data['time'], data['x'], data['y']), (255, 255, 255))

    y += 1