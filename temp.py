import cv2

def show(img,name):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('image.jpeg')
img = cv2.line(img,(500,500),(500,520),(0,255,0),1)
show(img,'img')


