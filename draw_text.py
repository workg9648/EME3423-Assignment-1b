import cv2
import numpy as np

capture = cv2.VideoCapture(0 , cv2.CAP_DSHOW)
capture.set(3 , 240) # 3 = width
capture.set(4 , 320) # 4 = height

while True:
    _ , img1 = capture.read()

    img2 = cv2.flip(img1 , 0)
    img3 = cv2.flip(img1 , 1)
    img4 = cv2.flip(img1 , -1)

    Hori1 = np.concatenate((img1 , img3) , axis = 1)
    Hori2 = np.concatenate((img2, img4), axis=1)
    Verti = np.concatenate((Hori1, Hori2), axis=0)

    cv2.imshow("frama" , Verti)


    if cv2.waitKey(20) & 0xff == ord('g'):
        break


# ////////////////////////////////////////////////////////////////////////////////
# import  cv2

# capture = cv2.VideoCapture('Resources/dog.mp4')

# while True:
#    success , img = capture.read()

#    img2 = cv2.resize(img, (int(img.shape[1] / 1.5), int(img.shape[0] / 1.5)))
#    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#    cv2.putText(img, 'i am dog', (10, 300), cv2.FONT_HERSHEY_PLAIN, 2, (0 , 0, 0), 2)

#    cv2.imshow("Frame" , img)

#   if cv2.waitKey(20) & 0xff == ord('g'):
#        break

# capture.release()
# cv2.destroyAllWindows()
# ////////////////////////////////////////////////////////////////////////////////////

# /////////////////////////////////////////////////////////////////////////////////////
# img = cv2.imread('Resources / lena.png')

# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img , 'i am Lena' , (10 , 300) , font , 2 , (255 , 255 , 255) ,2)
# ///////////////////////////////////////////////////////////////////////////////////

# //////////////////////////////////////////////////////////////////////////////////
# img = np.zeros((255 , 255 , 3) , np.uint8)
# img = cv2.line(img , (0 , 0) , (255 , 255) , (255 , 255 , 255) , 5)
# img = cv2.circle(img , (200 , 100) , 50 , (255 , 255 , 0) , 9)
# img = cv2.rectangle(img , (155 , 0) , (255 , 100) , (0 , 0 , 255) , 8)

# pts = np.array([[50 , 60] , [90 , 80] , [22 , 33] , [44 , 66] , [73 , 11]] , np.int32)
# img = cv2.polylines(img , [pts] , True , (0 , 155 , 155))


# print(img.shape)
# print(img)

# ///////////////////////////////////////////////////////////////////////////////////

cv2.imshow("img" , img)

cv2.waitKey(0)








