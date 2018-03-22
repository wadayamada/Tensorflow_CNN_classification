from PIL import Image
import os

#png_2_jpg.py

#pngの画像の枚数
png_gazou=82

#pngをjpgに変換する

def png_2_jpg(png_gazou,name):

    for a in range(png_gazou):
        b=str(a+1)
        #パスを指定して画像読み込み
        img=Image.open("./data_keep/other/"+name+" ("+b+").png")
        width,height=img.size
        canvas=Image.new("RGB",(width,height),(255,255,255))
        canvas.paste(img,(0,0))
        #jpgとして保存
        canvas.save("./data_keep/other/"+name+"("+b+").jpg","JPEG",quality=100,optimizer=True)
 