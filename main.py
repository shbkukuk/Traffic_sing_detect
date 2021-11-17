import cv2 as cv
from matplotlib import  pyplot as plt

img1 = cv.imread("images/4.jpg")
girilmez_data = cv.CascadeClassifier('data/girilmezlevha/classifier/cascade.xml')
img1_gray = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
img1_rgb = cv.cvtColor(img1, cv.COLOR_BGR2RGB)


found = girilmez_data.detectMultiScale(img1_gray,minSize =(20, 20))
amount_found = len(found)
if amount_found != 0:
    for (x, y, width, height) in found:
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img1_rgb,'Girilmez Trafik Levhasi',(x,y+height),
                   font,0.75,(0,255,255),2,cv.LINE_AA)
        #cv.rectangle(img1_rgb, (x, y),
                      #(x + height, y + width),
                      #(0, 255, 0), 5)


plt.subplot(1, 1, 1)
plt.imshow(img1_rgb)
plt.show()