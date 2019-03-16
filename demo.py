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
'''
cv2.imwrite('resized_img_1.jpg',img0)
cv2.imwrite('resized_img_2.jpg',img1)
cv2.imwrite('resized_img_3.jpg',img2)
cv2.imwrite('resized_img_4.jpg',img3)
cv2.imwrite('resized_img_5.jpg',img4)
cv2.imwrite('resized_color_img_1.jpg',img_color_0)
cv2.imwrite('resized_color_img_2.jpg',img_color_1)
cv2.imwrite('resized_color_img_3.jpg',img_color_2)
cv2.imwrite('resized_color_img_4.jpg',img_color_3)
cv2.imwrite('resized_color_img_5.jpg',img_color_4)
'''

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
    show(sobely,name)
    img_num += 1
    transformed_images.append(sobely)

show(transformed_images[0],"img")
target_img = transformed_images[0]
target_col_img = img_color_1

print(target_img[2,0])
# index[y,x]
# dimension = x,y = 960,720
vertical   = [[-1, 0, 1],
              [-2, 0, 2],
              [-1, 0, 1]]

horizontal = [[-1,-2,-1],
              [ 0, 0, 0],
              [ 1, 2, 1]]

def check(target_img,target_col_img):
    x = 960
    y = 720
    for col in range(0,x,20):
        for row in range(y,int(y/2),-20):
            try:
                a = 0
                l = 20
                for i in range(l):
                    a += target_img[row+i,col]
                for i in range(l):
                    a += target_img[row,col+i]
                if a == 0:
                    target_col_img = cv2.line(target_col_img,(col,row),(col,row+20),(255,255,0),1) 
                    target_col_img = cv2.line(target_col_img,(col,row),(col+20,row),(255,255,0),1) 
                    break
            except:
                continue
    
    show(target_col_img,"result")


for i,j in zip(transformed_images,color_images):
    check(i,j)













'''
points_each_img = []
for img in range(img_num):
    #name = 'resized_img_'+str(img)+'.jpg'
    #name = 'draw'+str(img)+'.jpg'
    name = 'resized_color_img_'+str(img)+'.jpg'
    new_draw = cv2.imread(name,1)
    points = []
    # col,x
    for j in range(0,960,1):
        # row,y
        for i in range(719,200,-10):
            if images[img][i][j]==0:
                s = 0
                for x in range(1,25):
                    s += images[img][i-x][j]
    
                if s == 0:
                    current_point = [i,j]
                    points.append(current_point)
                    new_draw = cv2.line(new_draw,(j,719),(j,i),(0,255,0),10)
                    name = 'final_'+str(img)+'.jpg'
                    cv2.imwrite(name,new_draw)
                    
                    break
    points_each_img.append(points)
    
        #print()
    show(new_draw,name)
#cv2.imwrite('green.jpg',new_draw)
'''

