import cv2

img = cv2.imread('111.png')
resize_frame = cv2.resize(img, (980, 2122), interpolation=cv2.INTER_AREA)
cv2.imwrite('E:/python_script/112.png', resize_frame)
# cv2.imshow(resize_frame)
# cv2.waitKey()