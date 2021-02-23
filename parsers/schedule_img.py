import os
import random
name_image = 'media_studio.jpg'


def schedule_open_img(name_image):
    directory = '/home/maxim/PycharmProjects/telebot/static/img'
    files = os.listdir(directory)
    if name_image in files:
        path_img = directory + '/' + name_image
        return path_img


# img = schedule_open_img(name_image)
# print(img)




# def media_class_open_img(name_image):
#     directory = 'static/img'
#     import_img_path = directory + '/' + name_image
#     files = os.listdir(directory)
#     for file in files:
#         if file == name_image:
#             path = directory + '/' + file
#             return path