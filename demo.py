import cv2
import numpy as np
import math

def show(img,name):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# save image
#cv2.imwrite('image-name.jpg',img)

''' Load images '''
img = cv2.imread('image.jpeg',0)
img2 = cv2.imread('image2.jpg',0)
img3 = cv2.imread('image3.jpg',0)
img4 = cv2.imread('image4.jpg',0)
img5 = cv2.imread('image5.jpg',0)
img_color_0 = cv2.imread('image.jpeg',1)
img_color_1 = cv2.imread('image2.jpg',1)
img_color_2 = cv2.imread('image3.jpg',1)
img_color_3 = cv2.imread('image4.jpg',1)
img_color_4 = cv2.imread('image5.jpg',1)
print('image size =',img.shape)

''' Resize images '''
img0 = cv2.resize(img, (960,720)) 
img1 = cv2.resize(img2, (960,720)) 
img2 = cv2.resize(img3, (960,720)) 
img3 = cv2.resize(img4, (960,720)) 
img4 = cv2.resize(img5, (960,720)) 
img_color_0 = cv2.resize(img_color_0, (960,720)) 
img_color_1 = cv2.resize(img_color_1, (960,720)) 
img_color_2 = cv2.resize(img_color_2, (960,720)) 
img_color_3 = cv2.resize(img_color_3, (960,720)) 
img_color_4 = cv2.resize(img_color_4, (960,720)) 
cv2.imwrite('resized_img_0.jpg',img0)
cv2.imwrite('resized_img_1.jpg',img1)
cv2.imwrite('resized_img_2.jpg',img2)
cv2.imwrite('resized_img_3.jpg',img3)
cv2.imwrite('resized_img_4.jpg',img4)
cv2.imwrite('resized_color_img_0.jpg',img_color_0)
cv2.imwrite('resized_color_img_1.jpg',img_color_1)
cv2.imwrite('resized_color_img_2.jpg',img_color_2)
cv2.imwrite('resized_color_img_3.jpg',img_color_3)
cv2.imwrite('resized_color_img_4.jpg',img_color_4)

''' Put images into list '''
images = [img0,img1,img2,img3,img4]

''' Display images '''
for image in images:
    #show(image,'image')
    pass

''' Display images after transformation '''
img_num = 0
for image in images:
    image = cv2.GaussianBlur(image,(15,15),0)
    sobely = cv2.Sobel(image,cv2.CV_8U,0,1,ksize=5)
    images[img_num] = sobely
    name = 'draw'+str(img_num)+'.jpg'
    cv2.imwrite(name,sobely)
    img_num += 1

new_img = []

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
                    
                    '''
                    try:
                        previous0 = points[-2][0]
                        previous1 = points[-3][0]
                    except:
                        previous0 = points[-1][0]
                        previous1 = previous0

                    diff01 = math.sqrt((previous0-previous1)**2)
                    diffc0 = math.sqrt((i-previous0)**2)
                    total_diff = math.sqrt((diffc0-diff01)**2)

                    print('previous0 ',previous0)
                    print('previous1 ',previous1)
                    print('diffc0',diffc0)
                    print('diff01',diff01)
                    print('total_diff',total_diff)
                    print()

                    if total_diff < 20:
                        break

                    '''
                    break
    points_each_img.append(points)
    
        #print()
    show(new_draw,name)
#cv2.imwrite('green.jpg',new_draw)

