import cv2
import numpy as np

def show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

''' load images '''
images = []
bw_images = []

for i in range(1,6):
    name = "test"+str(i)+".jpg"
    temp = cv2.imread(name)
    temp = cv2.resize(temp,(960,720))
    images.append(temp)
    show("img",temp)
    
    temp2 = cv2.imread(name,0)
    temp2 = cv2.resize(temp2,(960,720))
    for i in range(3):
        temp2 = cv2.GaussianBlur(temp2,(15,15),0)
    temp2 = cv2.Sobel(temp2,cv2.CV_8U,0,1,ksize=5)
    for i in range(3):
        temp2 = cv2.GaussianBlur(temp2,(15,15),0)
    bw_images.append(temp2)
    show("img",temp2)

''' model '''
import pickle
with open("model_pickle","rb") as f:
    model = pickle.load(f)

#model.predict(X_test)

''' detect '''
for img,bw_img in zip(images,bw_images):
    for x in range(960):
        for y in range(200,720):
            try:
                a = bw_img[y-2,x-2]+bw_img[y-2,x-1]+bw_img[y-2,x]+bw_img[y-2,x+1]
                b = bw_img[y-2,x+2]+bw_img[y-1,x-2]+bw_img[y-1,x-1]+bw_img[y-1,x]
                c = bw_img[y-1,x+1]+bw_img[y-1,x+2]+bw_img[y,x-2]+bw_img[y,x-1]
                d = bw_img[y,x]+bw_img[y,x+1]+bw_img[y,x+2]+bw_img[y+1,x-2]
                e = bw_img[y+1,x-1]+bw_img[y+1,x]+bw_img[y+1,x+1]+bw_img[y+1,x+2]
                f = bw_img[y+2,x-2]+bw_img[y+2,x-1]+bw_img[y+2,x]+bw_img[y+2,x+1]+bw_img[y+2,x+2]
                v = a+b+c+d+e+f
            except:
                v = 0
            pred = model.predict([[x,y,v]])

            if pred==1:
                img = cv2.line(img,(x,y),(x,719),(255,255,0),1)
                pass

    show("img",img)
