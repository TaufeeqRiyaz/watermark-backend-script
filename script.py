import cv2

logo = cv2.imread('watermark.png')
H_logo, W_logo,_ = logo.shape

img = cv2.imread('picture.png')
H_img, W_img,_ = img.shape

cx_img = int(W_img /2)
cy_img = int(H_img /2)

top_y = cy_img - int(H_logo/ 2)
left_x = cx_img - int(W_logo/ 2)

bottom_y = top_y + H_logo
right_x = left_x + W_logo

roi = img[top_y:bottom_y, left_x:right_x]

result = cv2.addWeighted(roi, 1, logo, 0.3, 1)

img[top_y:bottom_y, left_x:right_x] = result

cv2.imshow('Logo', logo)
cv2.imshow('Image', img)
cv2.imwrite('Output.png', img)

cv2.waitKey(0)


