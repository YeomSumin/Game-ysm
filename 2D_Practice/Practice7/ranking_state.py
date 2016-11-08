import game_framework
from pico2d import *
import json

import main_state

name = "RankingState"
image = None
font = None
score_data = None

def enter():
    global image, font
    image = load_image('blackboard.png')
    font = load_font('ENCR10B.TTF', 40)

def exit():
    global image, font, score_data

    f = open('score_data.txt', 'r')
    score_data = json.load(f)
    f.close()
    score_data.append({"Time: score.Time, "})
    del(image)
    del(font)


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
                game_framework.quit()


def update(frame_time):
    pass


def bubble_sort(data_list):
    for i in range(0, len(data_list)):
        for j in range(i + 1, len(data_list)):
            if data_list[i]['Time'] < data_list[j]['Time']:
                data_list[i], data_list[j] = data_list[j], data_list[i]

def draw_ranking():
    global score_data

    #def print_score(score):
        #print('(Time:%4.1f, x:%4d, y:%4d)' %
              #(score['Time'], score['x'], score['y']))

    f = open('data_file.txt', "r")
    score_data = json.load(f)
    f.close()

    bubble_sort(score_data)
    score_data = score_data[:10]

    print('RANKING')
    font.draw(300, 550, '[RANKING]', (255, 0, 0))

    def draw_score(score):
        y = 0

        for y in range(9):
            print('(Time:%4.1f, x:%4d, y:%4d)' %
                  (score[y]['Time'], score[y]['x'], score[y]['y']))

            font.draw(50, 500 - (50 * y), "Time:%4.1f, x:%4d, y:%4d" %
                      (score[y]['Time'], score[y]['x'], score[y]['y'])
                      , (255, 255, 255))
            y += 1

    draw_score(score_data)

def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300)
    draw_ranking()
    update_canvas()