import cv2
import numpy as np
import math
import time

def show(img,name):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# save image
#cv2.imwrite('image-name.jpg',img)

''' Load images '''
img1 = cv2.imread('image1.jpeg',0)
img2 = cv2.imread('image2.jpg',0)
img3 = cv2.imread('image3.jpg',0)
img4 = cv2.imread('image4.jpg',0)
img5 = cv2.imread('image5.jpg',0)
img_color_1 = cv2.imread('image1.jpeg',1)
img_color_2 = cv2.imread('image2.jpg',1)
img_color_3 = cv2.imread('image3.jpg',1)
img_color_4 = cv2.imread('image4.jpg',1)
img_color_5 = cv2.imread('image5.jpg',1)
print('image size =',img1.shape)

''' Resize images '''
img1 = cv2.resize(img1, (960,720)) 
img2 = cv2.resize(img2, (960,720)) 
img3 = cv2.resize(img3, (960,720)) 
img4 = cv2.resize(img4, (960,720)) 
img5 = cv2.resize(img5, (960,720)) 
img_color_1 = cv2.resize(img_color_1, (960,720)) 
img_color_2 = cv2.resize(img_color_2, (960,720)) 
img_color_3 = cv2.resize(img_color_3, (960,720)) 
img_color_4 = cv2.resize(img_color_4, (960,720)) 
img_color_5 = cv2.resize(img_color_5, (960,720)) 

''' Put images into list '''
images = [img1,img2,img3,img4,img5]
color_images = [img_color_1,img_color_2,img_color_3,img_color_4,img_color_5]
transformed_images = []

''' Display images '''
for image in images:
    #show(image,'image')
    pass

''' Display images after transformation '''
img_num = 0
for image in images:
    image = cv2.GaussianBlur(image,(15,15),0)
    show(image,"image")
    image = cv2.GaussianBlur(image,(15,15),0)
    show(image,"image")
    image = cv2.GaussianBlur(image,(15,15),0)
    show(image,"image")
    image = cv2.GaussianBlur(image,(15,15),0)
    show(image,"image")
    image = cv2.GaussianBlur(image,(15,15),0)
    show(image,"image")

    sobely = cv2.Sobel(image,cv2.CV_8U,0,1,ksize=5)
    name = 'draw'+str(img_num)+'.jpg'
    show(sobely,name)
    img_num += 1
    transformed_images.append(sobely)
