import cv2
import numpy as np

'''
def show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

images = []

for i in range(5):
    name = "~/Documents/Projects/Detect-floor-OpenCV/resized_color_img_"+str(i)+".jpg"
    temp = cv2.imread(name,0)
    images.append(temp)
    #show("img",temp)

a = images[0]
show("a",a)
for i in range(10):
    a = cv2.GaussianBlur(a,(15,15),0)
    show("a",a)

'''

#import cv2
import matplotlib.pyplot as plt
image = cv2.imread("image2.jpg",0)
print(type(image))
print("\n\n\n")
plt.imshow(image)
plt.show()
