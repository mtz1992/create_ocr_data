# -*- coding: utf-8 -*-
import os
import random

# root_path = "/home/mtz/workspace/test/ocrtest"

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

wh_list_5_50 = [250,65]
wh_list_10_50 = [500,65]
wh_list_5_100 = [500,130]
wh_list_10_100 = [1000,130]
wh_list_2_50 = [100,65]
wh_list_2_100 = [200,130]
wh_list_2_60 = [150,65]
wh_list_5_60 = [300,65]
wh_list_10_60 = [600,65]
wh_list_2_70 = [150,80]
wh_list_5_70 = [350,80]
wh_list_10_70 = [700,80]

def count_size_wh(count,size):
    if (count == 5) and (size == 50):
        return wh_list_5_50
    if (count == 10) and (size == 50):
        return wh_list_10_50
    if (count == 5) and (size == 100):
        return wh_list_5_100
    if (count == 10) and (size == 100):
        return wh_list_10_100
    if (count == 2) and (size == 50):
        return wh_list_2_50
    if (count == 2) and (size == 100):
        return wh_list_2_100
    if (count == 2) and (size == 60):
        return wh_list_2_60
    if (count == 5) and (size == 60):
        return wh_list_5_60
    if (count == 10) and (size == 60):
        return wh_list_10_60
    if (count == 2) and (size == 70):
        return wh_list_2_70
    if (count == 5) and (size == 70):
        return wh_list_5_70
    if (count == 10) and (size == 70):
        return wh_list_10_70

# 读取字典
text_list = []
with open('dictionaries.txt', 'r') as f1:
    for text in f1.readlines():
        if text != None:
            # 从文件中读取行数据时，会带换行符，使用strip函数去掉 换行符后存入列表
            text_list.append(text.strip("\n"))

file_txt = open("train.txt", 'w')
# 读取图片
image_path = "image"

def create_iamge(x,y,i):
    for root, dirs, files in os.walk(image_path):
        j = 0
        for file in files:
            image = image_path + "/" + file

            # 设置字体大小，如果没有，也可以不设置
            font_list = ['Fonts/msjhbd.ttc', 'Fonts/msyh.ttc', 'Fonts/simsun.ttc', 'Fonts/msyhl.ttc', 'Fonts/msjhl.ttc', 'Fonts/msjh.ttc', 'Fonts/msyhbd.ttc']
            font_name = random.choice(font_list)
            size_list = [50, 60, 70, 100]
            size = random.choice(size_list)
            font = ImageFont.truetype(font_name, size)
            # 设置文字个数
            count_list = [2, 5, 10]
            count = random.choice(count_list)
            text_list_new = random.sample(text_list, count)
            text_new = ''.join(text_list_new)

            # 打开底版图片
            im1 = Image.open(image)
            # 在图片上添加文字 1
            draw = ImageDraw.Draw(im1)
            # draw.text((100, 100),u'庆庆 祝河南理工大学建校110周年',(255,255,0),font=font)
            color1 = random.randint(0,255)
            color2 = random.randint(0,255)
            color3 = random.randint(0,255)
            draw.text((x, y), text_new, (color1, color2, color3), font=font)
            draw = ImageDraw.Draw(im1)

            # 根据文字个数和字体大小据定裁图大小
            w, h = count_size_wh(count, size)

            region = im1.crop((x, y, x + w, y + h))
            save_image_path = "train/create_" + str(i) + "_" + str(j) + ".jpg"
            region.save(save_image_path)
            # label
            col = save_image_path + "\t" + text_new + "\n"
            # print(col)
            file_txt.write(col)
            j = j + 1

xy_list = [[50,100],[0,200],[50,300],[50,200],[0,150]]

for i in range(len(xy_list)):
    x, y = xy_list[i]
    create_iamge(x,y,i)
    print("x:" + str(x) + ",y:" + str(y))
    print("deno")


# for x,y in xy_list:
#     i = 0
#     create_iamge(x,y,i)
#     print("x:" + str(x) + ",y:" + str(y))
#     print("deno")

# x = 100
# y = 100

# text_list_new = random.sample(text_list,10)
# text_new = ''.join(text_list_new)
# print(text_new)

# font = ImageFont.truetype(font_name, 70)
# image = "0.jpg"
# im1 = Image.open(image)
# # 在图片上添加文字 1
# draw = ImageDraw.Draw(im1)
# # draw.text((100, 100),u'庆庆 祝河南理工大学建校110周年',(255,255,0),font=font)
# color1 = random.randint(0,255)
# color2 = random.randint(0,255)
# color3 = random.randint(0,255)
# draw.text((x, y), text_new, (color1, color2, color3), font=font)
# draw = ImageDraw.Draw(im1)
#
# # 根据文字个数和字体大小据定裁图大小
# w, h = wh_list_10_70
#
# region = im1.crop((x, y, x+w, y+h))
# region.save("./crop_test2.jpg")

