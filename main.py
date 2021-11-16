import cv2 as cv
from matplotlib import  pyplot as plt

img1 = cv.imread("Hiz_siniri.jpg")
Hiz_data = cv.CascadeClassifier('stop_data.xml')
img1_gray = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
img1_rgb = cv.cvtColor(img1, cv.COLOR_BGR2RGB)

"""plt.subplot(1, 1, 1)
plt.imshow(img1_rgb)
plt.show()
"""
found = Hiz_data.detectMultiScale(img1_gray,
                                   minSize =(20, 20))
amount_found = len(found)

if amount_found != 0:


    for (x, y, width, height) in found:

        cv.rectangle(img1_rgb, (x, y),
                      (x + height, y + width),
                      (0, 255, 0), 5)


plt.subplot(1, 1, 1)
plt.imshow(img1_rgb)
plt.show()