# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 13:45:56 2018

@author: gd
"""
from PIL import Image, ImageStat

im_file="2.jpg"
im2 = Image.open(im_file)
im2 = im2.resize((500, 500), Image.ANTIALIAS)

greyscale_image = im2.convert('L')

#plt.imshow(greyscale_image)
pix = greyscale_image.load()


print(pix[0,0])
print(pix[499,499])
print(type(pix))
print(greyscale_image)
width, height = greyscale_image.size
print(width,height)


#average (arithmetic mean) pixel level for each band in the image.
def brightness( im_file ):  
   stat = ImageStat.Stat(im2)
   return stat.mean[0]

#RMS (root-mean-square) for each band in the image.
def contrast( im_file ):  
   stat = ImageStat.Stat(im2)
   return stat.rms[0]


b=int(brightness(greyscale_image))
c=int(contrast(greyscale_image))
alfa=.5
pi = list(greyscale_image.getdata())


def modify_image(img):
    pixdata = img.load()
    
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if abs(pixdata[i, j] - b )> alfa*c:
                pixdata[i, j] = 255
            else:
                pixdata[i, j] = 0
    return img


print(range(greyscale_image.size[0]))


g=modify_image(greyscale_image)


print(g)


g.show()











