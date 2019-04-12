import cv2
import numpy as np
import pandas as pd

def show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img0 = cv2.imread("resized_labeled_color_img_0.jpg")
images = []
bw_images = []

for i in range(5):
    name = "resized_labeled_color_img_"+str(i)+".jpg"
    temp = cv2.imread(name)
    temp = cv2.resize(temp,(960,720))
    images.append(temp)

    name = "resized_color_img_"+str(i)+".jpg"
    temp = cv2.imread(name,0)
    #show("img",temp)
    for i in range(3):
        temp = cv2.GaussianBlur(temp,(15,15),0)
    temp = cv2.Sobel(temp,cv2.CV_8U,0,1,ksize=5)
    for i in range(3):
        temp = cv2.GaussianBlur(temp,(15,15),0)
    bw_images.append(temp)
    show("img",temp)


img = images[0]
img = cv2.rectangle(img,(100,100),(100,106),(255,255,255),1)
show("img",img)
print("len=",len(images))


def detect_line(images,bw_images,pX,pY,s,edge):
    count = 1
    for img,bw_img in zip(images,bw_images):
        for y in range(720):
            for x in range(960):
                pX.append(x)
                pY.append(y)
                #v = bw_img[y-2,x-2]+bw_img[y-2,x-1]+bw_img[y-2,x]+bw_img[y-2,x+1]+bw_img[y-2,x+2]+                        bw_img[y-1,x-2]+bw_img[y-1,x-1]+bw_img[y-1,x]+bw_img[y-1,x+1]+bw_img[y-1,x+2]+bw_img[y,x-2]+bw_img[y,x-1]+bw_img[y,x]+bw_img[y,x+1]+bw_img[y,x+2]+bw_img[y+1,x-2]+bw_img[y+1,x-1]+bw_img[y+1,x]+bw_img[y+1,x+1]+bw_img[y+1,x+2]+bw_img[y+2,x-2]+bw_img[y+2,x-1]+bw_img[y+2,x]+bw_img[y+2,x+1]+bw_img[y+2,x+2]
                try:
                    v = (bw_img[y-2,x-2]+bw_img[y-2,x-1]+bw_img[y-2,x]+bw_img[y-2,x+1]+bw_img[y-2,x+2]+
                        bw_img[y-1,x-2]+bw_img[y-1,x-1]+bw_img[y-1,x]+bw_img[y-1,x+1]+bw_img[y-1,x+2]+
                        bw_img[y,x-2]+bw_img[y,x-1]+bw_img[y,x]+bw_img[y,x+1]+bw_img[y,x+2]+
                        bw_img[y+1,x-2]+bw_img[y+1,x-1]+bw_img[y+1,x]+bw_img[y+1,x+1]+bw_img[y+1,x+2]+
                        bw_img[y+2,x-2]+bw_img[y+2,x-1]+bw_img[y+2,x]+bw_img[y+2,x+1]+bw_img[y+2,x+2])
                    s.append(v)
                except:
                    s.append(0)
                r = 200
                g = 50
                b = 50
                rr = img[y,x][2]
                gg = img[y,x][1]
                bb = img[y,x][0]
                if r<rr and g>gg and b>bb:
                    bw_img = cv2.line(bw_img,(x,y),(x,y),(255,255,255),2)
                    edge.append(1)
                else:
                    edge.append(0)

        show("img",bw_img)
        print("image"+str(count)+": done")
        count += 1

#detect_line(images)

''' Create dictionary '''
''' x[pixelX,pixelY,sum25]'''
pX = []
pY = []
sum_of_filter=  []
edge = []

print("\n\nStart")
detect_line(images,bw_images,pX,pY,sum_of_filter,edge)
df = pd.DataFrame({"pixel_Y":pY, "pixel_X":pX, "sum_of_filter":sum_of_filter,"edge":edge})
print(df.describe())

#print(df[df["edge"]==1])
export = df.to_csv("data.csv", index=None, header=True)
