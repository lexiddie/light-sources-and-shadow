import cv2
import numpy as np

img1 = './img1.jpg'
img2 = './img2.jpg'

read_img = cv2.imread(img2)
img_result = cv2.cvtColor(read_img, cv2.COLOR_HSV2BGR)

# apply Canny edge detection using a tight threshold
blurred = cv2.GaussianBlur(img_result, (5, 5), 0)
tight = cv2.Canny(blurred, 225, 250)
contours, hierarchy = cv2.findContours(tight.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
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

result = np.concatenate((deepcopy_img, read_img), axis=1)
cv2.imshow('Result Images', result)
cv2.imwrite('save_result.png', result)
print('Finish Compute')
cv2.waitKey(0)
cv2.destroyAllWindows()
