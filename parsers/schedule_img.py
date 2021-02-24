import os


def schedule_open_img(name_image):
    directory = 'static/img'
    files = os.listdir(directory)
    if name_image in files:
        path_img = directory + '/' + name_image
        return path_img
