import numpy as np
import cv2
import os

# Hier fängt das ganze mit allen Dateien an
list = os.listdir('../testdata')
number_files = len(list) #Anzahl der Dateien in /testdata

# K means image filter
kmeans_img_array = []
for x in range(1, number_files+1):
    img = cv2.imread('../testdata/person-{}.jpg'.format(x))
    Z = img.reshape((-1, 3))

    Z = np.float32(Z)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1-0)
    K = 5
    ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))

    kmeans_img_array.append(res2)

# Canny edge detection


for i in range(0, len(kmeans_img_array)):
    cv2.imshow('img-{}'.format(i+1), kmeans_img_array[i])


while True:
    cv2.waitKey(0)
    if cv2.waitKeyEx() == 2490368:
        print("test")
    elif cv2.waitKeyEx() == 27:
        cv2.destroyAllWindows()
