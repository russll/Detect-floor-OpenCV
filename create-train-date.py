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
    image = cv2.GaussianBlur(image,(15,15),0)
    image = cv2.GaussianBlur(image,(15,15),0)
    #show(image,"image")

    sobely = cv2.Sobel(image,cv2.CV_8U,0,1,ksize=5)
    name = 'draw'+str(img_num)+'.jpg'
    #show(sobely,name)
    img_num += 1
    transformed_images.append(sobely)

#show(transformed_images[0],"img")
target_img = transformed_images[0]
target_col_img = img_color_1

print(target_img[2,0])


# image 1 - [0,600],[357,498],[959,566]
img_color_1 = cv2.line(img_color_1,(0,600),(357,498),(255,255,0),1) 
img_color_1 = cv2.line(img_color_1,(357,498),(959,566),(255,255,0),1) 
#show(img_color_1,"1")

# image 2 - [0,564],[129,510],[835,510],[959,564]

img_color_2 = cv2.line(img_color_2,(0,564),(129,510),(255,255,0),1) 
img_color_2 = cv2.line(img_color_2,(129,510),(835,510),(255,255,0),1) 
img_color_2 = cv2.line(img_color_2,(835,510),(959,564),(255,255,0),1) 
#show(img_color_2,"2")

# image 3 - [0,690],[210,560],[835,564],[959,640]
transformed_images[2] = cv2.line(transformed_images[2],(0,690),(0,690),(255,255,0),5) 
transformed_images[2] = cv2.line(transformed_images[2],(210,560),(210,560),(255,255,0),5) 
transformed_images[2] = cv2.line(transformed_images[2],(835,564),(835,564),(255,255,0),5) 
transformed_images[2] = cv2.line(transformed_images[2],(959,640),(959,640),(255,255,0),5) 
show(transformed_images[2],"3")

# image 4
'''
for i in range(0,960,10):
    img_color_2 = cv2.line(img_color_2,(i,0),(i,719),(0,0,0),1) 
    pass
for i in range(0,720,10):
    img_color_2 = cv2.line(img_color_2,(0,i),(959,i),(0,0,0),1) 
    pass
'''
# image 5
'''
for i in range(0,960,10):
    img_color_2 = cv2.line(img_color_2,(i,0),(i,719),(0,0,0),1) 
    pass
for i in range(0,720,10):
    img_color_2 = cv2.line(img_color_2,(0,i),(959,i),(0,0,0),1) 
    pass
'''

# index[y,x]
# dimension = x,y = 960,720

'''
for i,j in zip(transformed_images,color_images):
    show(i,j)
'''
