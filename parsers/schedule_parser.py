import os

from scripts.text_data import text_data


def schedule_open_img(name_image):
    directory = 'static/img'
    files = os.listdir(directory)
    if name_image in files:
        path_img = directory + '/' + name_image
        return path_img


def schedule_day(text_data):
    acc = []
    for key, value in text_data['Дневные мероприятия'].items():
        for pos in value:
            time = pos[0]
            desc = pos[1]
            point = pos[2]
            acc.append(f'{time} | {desc.upper()}\n{point}\n')
    acc_string = '\n'.join(acc)
    return acc_string


schedule_day_parser = schedule_day(text_data)