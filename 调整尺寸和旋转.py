#coding=utf-8
from PIL import Image

'''
    resize()    该方法的参数是一个元组，用来指定新图像的大小
    rotate()    逆时针方式表示旋转角度
    convert('L')    将其转换成灰度图像
'''

img = Image.open("./img/test.jpg")

out_img = img.resize((128, 128))

ro_img = img.rotate(45)

ro_img.show()

ro_img.convert("L").show()
