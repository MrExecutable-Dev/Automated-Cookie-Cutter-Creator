import cv2
import numpy as np

x = 0
y = 0
K = 4

def onXchange(value):
    edges = cv2.Canny(img, value, 400)
    cv2.imshow("canny-edges", edges)
    global x
    x = value
    print("x: {} | y: {}".format(x, y))


def onYchange(value):
    edges = cv2.Canny(img, x, value)
    cv2.imshow("canny-edges", edges)
    global y
    y = value
    print("x: {} | y: {}".format(x, y))

def onKchange(value):
    global K
    K = value
    ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    cv2.imshow("k-means edges", res2)

colors = []

def onChange(value):
    all_colors = np.unique(res2, axis=0, return_counts=True)
    all_colors_array = np.asarray(all_colors[0])

    for x in range(len(all_colors_array[0])):
        to_add = all_colors_array[0][x]   

        color = [to_add[0], to_add[1], to_add[2]]
        if color not in colors:
            colors.append(color)


img = cv2.imread('./test_data/face-2-bg-removed.png')
edges = cv2.Canny(img, x, y)

Z = img.reshape((-1, 3))
Z = np.float32(Z)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))


cv2.imshow("k-means edges", res2)
cv2.imshow("canny-edges", edges)


cv2.createTrackbar('slider-1', "canny-edges", 0, 400, onXchange)
cv2.createTrackbar('slider-2', "canny-edges", 0, 400, onYchange)

cv2.createTrackbar('k-slider', "k-means edges", 0, 10, onKchange)

cv2.createTrackbar('button slider', "k-means edges", 0, 1, onChange)


cv2.waitKey(0)
cv2.destroyAllWindows()

file = open("./output/cutter.obj", "w")
file.write("o Cutter\n")

height = 0

for i in range(len(colors)):

    indices = np.where(img == colors[i])
    coordinates = zip(indices[0], indices[1])

    unique_coordinates = list(set(list(coordinates)))

    for x in range(len(unique_coordinates)):
        file.write("v {} {} {}\n".format(unique_coordinates[x][0]/10, unique_coordinates[x][1]/10, height))

    height = height + 5


file.close()
