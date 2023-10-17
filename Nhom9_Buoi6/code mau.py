import cv2
import numpy as np
import matplotlitb.puplot as plt
img = cv2.imread('pic1.png',cv2.IMREAD_GRAYSCALE)
half = vc2.resize(img, (0, 0), fx = 0.1, fy = 0.1)
bigger = vc2.resize(img, (1050, 1610))
atretch_near = cv2.resize(img, (780, 540), interpolation = cv2.INTER_LINEAR)
Titles = ["Original", "Half", "Bigger", "interpolation Nearest"]
images = [img, half, bigger, stretch_near]
count = 4
for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])
plt.show()
