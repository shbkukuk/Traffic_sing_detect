import cv2 as cv
from matplotlib import  pyplot as plt

img1 = cv.imread("images/4.jpg")
girilmez_data = cv.CascadeClassifier('data/girilmezlevha/classifier/cascade.xml')
hizsiniri_data = cv.CascadeClassifier('data/hizsiniri/classifier/cascade.xml')
ilerisag_data = cv.CascadeClassifier('data/sagamecburiyon/classifier/cascade.xml')
ilerimecburi_data = cv.CascadeClassifier('data/ilerimecburiyon/classifier/cascade.xml')
img1_gray = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
img1_rgb = cv.cvtColor(img1, cv.COLOR_BGR2RGB)

girilmez =girilmez_data.detectMultiScale(img1_gray,minSize=(20,20))
ilerisag= ilerisag_data.detectMultiScale(img1_gray,minSize =(20, 20))
hizsiniri = hizsiniri_data.detectMultiScale(img1_gray,minSize=(20,20))
ilerimecburi = ilerimecburi_data.detectMultiScale(img1_gray,minSize=(20,20))


if len(ilerisag) != 0:
    for (x, y, width, height) in ilerisag:
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img1_rgb,'Mecburi Saga Yon',(300,690),
                   font,0.75,(0,255,255),2,cv.LINE_AA)
elif len(girilmez) !=0:
    for (x, y, width, height) in girilmez:
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img1_rgb, 'Girilmez', (x, y + height),
                   font, 0.75, (0, 255, 0), 2, cv.LINE_AA)

elif len(hizsiniri) != 0:
    for (x, y, width, height) in hizsiniri:
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img1_rgb, 'Hiz Siniri', (x, y + height),
                       font, 0.75, (0, 255, 0), 2, cv.LINE_AA)
elif len(ilerimecburi) != 0:
    for (x, y, width, height) in hizsiniri:
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img1_rgb, 'Mecburi ileri Yon', (x, y + height),
                       font, 0.75, (0, 255, 0), 2, cv.LINE_AA)

else:
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img1_rgb, 'Yol Yok', (195,260),
               font, 0.75, (0, 255, 0), 2, cv.LINE_AA)



plt.subplot(1, 1, 1)
plt.imshow(img1_rgb)
plt.show()