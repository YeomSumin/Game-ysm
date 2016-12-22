import game_framework
from pico2d import *

import main_state
import title_state

name = "RankingState"
image = None
font = None

def enter():
    global image, font
    image = load_image('background1.png')
    font = load_font('YD여고시절md.TTF', 50)


def exit():
    global image, font
    del (image)
    del (font)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()


    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)


def update():
    pass


def draw():
    global image

    clear_canvas()
    image.clip_draw(0, 0, 256, 392, 275, 360, 550, 720)
    font.draw(180, 600, "[RANKING]", (0, 0, 0))
    draw_ranking()
    update_canvas()


def draw_ranking():
    def my_sort(a):
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i]['Score'] < a[j]['Score']:
                    a[i], a[j] = a[j], a[i]

    f = open('ranking_data.txt', 'r')
    ranking_data = json.load(f)
    f.close()

    print('[RANKING]')
    my_sort(ranking_data)

    for data in ranking_data[:10]:
        print('(Score:%d)' % (data['Score']))

    y = 0

    for data in ranking_data[:10]:
        font.draw(150, 500 - 40 * y, '%d : %d' % (y+1, data['Score']), (71, 102, 0))
        y += 1