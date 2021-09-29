import numpy as np
import cv2
from skimage.morphology import remove_small_objects

img1 = cv2.imread('shadow1.jpg')
img2 = cv2.imread('shadow2.jpg')
img3 = cv2.imread('shadow3.jpg')
img4 = cv2.imread('shadow4.jpg')
img5 = cv2.imread('shadow5.jpg')
img6 = cv2.imread('shadow5.jpg')

# Change image input from this variable
main_img = img3

cv2.imshow('origin', main_img)
gray = cv2.cvtColor(main_img, cv2.COLOR_RGB2GRAY)

b, g, r = np.double(cv2.split(main_img))
im1 = cv2.cvtColor(main_img, cv2.COLOR_RGB2GRAY)

shadow_ratio = (4 / np.pi) * np.arctan2((b - g), (b + g))
cv2.imshow('shadow ratio', shadow_ratio)

shadow_mask = shadow_ratio > np.mean(shadow_ratio)
cv2.imshow("shadow_mask", np.uint8(shadow_mask * 255))
shadow_mask[-5:5, -5:5] = 0

cv2.imshow("shadow_mask1", np.uint8(shadow_mask * 255))
shadow_mask = remove_small_objects(shadow_mask, min_size=80, connectivity=3)
cv2.imwrite('shadow_mask1.png', np.uint8(shadow_mask * 255))

cv2.imshow("shadow_mask1", np.uint8(shadow_mask * 255))
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
kernel[1, 0] = 0
kernel[3, 0] = 0
kernel[1, 4] = 0
kernel[3, 4] = 0
shadow_mask1 = np.uint8(shadow_mask * 1)
mask = cv2.dilate(shadow_mask1, kernel) - shadow_mask1

cv2.imshow("boundary", np.uint8(mask * 255))
[row, col] = np.where(mask == 1)
for i in range(len(row) - 1):
    cv2.line(im1, (col[i], row[i]), (col[i + 1], row[i + 1]), (0, 0, 255), 1)
cv2.imshow("original-shadow", main_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
