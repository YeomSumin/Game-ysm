import json

def bubble_sort(data_list):
    for i in range(0, len(data_list)):
        for j in range(i+1, len(data_list)):
            if data_list[i]['Time'] < data_list[j]['Time']:
                data_list[i], data_list[j] = data_list[j], data_list[i]

def draw_ranking():
    def print_score(score):
        print('(Time:%4.1f, x:%4d, y:%4d)' %
              (score['Time'], score['x'], score['y']))

    f = open('data_file.txt', "r")
    score_data = json.load(f)
    f.close()

    bubble_sort(score_data)
    print('RANKING')

    for score in score_data:
        print_score(score)

draw_ranking()