import cv2
import numpy as np
import colorsys
import random as rd

img1 = './img1.jpg'
img2 = './img2.jpg'
img3 = './img3.jpg'
img4 = './img4.jpg'
img5 = './img5.jpg'
img6 = './img6.jpg'
img7 = './img7.jpg'
img8 = './img8.png'

read_img = cv2.imread(img5)

img_result = cv2.cvtColor(read_img, cv2.COLOR_HSV2BGR)
img_data = np.array(read_img)
b, g, r = cv2.split(read_img)
print(b, g, r)
print('\n')

# apply Canny edge detection using a wide threshold, tight
# threshold, and automatically determined threshold
blurred = cv2.GaussianBlur(img_result, (5, 5), 0)
wide = cv2.Canny(blurred, 10, 200)
tight = cv2.Canny(blurred, 225, 250)

# edged = cv2.Canny(img_result, 100, 200)
# edged = cv2.Canny(blurred, 100, 200)
edged = cv2.Canny(blurred, 225, 250)

contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
deepcopy_img = read_img.copy()


def get_contour_areas(cnts):
    all_areas = []
    for cnt in cnts:
        area = cv2.contourArea(cnt)
        all_areas.append(area)
    return all_areas


print("Contour Areas before Sorting", get_contour_areas(contours))
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
print("Contour Areas after Sorting", get_contour_areas(sorted_contours))

for c in sorted_contours:
    cv2.drawContours(image=read_img, contours=[c], contourIdx=-1, color=(7, 210, 193), thickness=2, lineType=cv2.FILLED)

# result = np.concatenate((read_img, img_result), axis=1)
# result = np.concatenate((deepcopy_img, img_result), axis=1)
# result = np.concatenate((img_result, blurred), axis=1)
result = np.concatenate((deepcopy_img, read_img), axis=1)
cv2.imshow('Result Images', result)
# cv2.imshow('Result Images', edged)
print('Finish Compute')
cv2.waitKey(0)
cv2.destroyAllWindows()
