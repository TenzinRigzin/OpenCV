import cv2

#input
img_path = r"C:/Users/trigz/OneDrive/Desktop/CV2/bird1.jpg"
img = cv2.imread(img_path)

#resize
resized_img = cv2.resize(img,(1000,240))

#print
cv2.imshow('original_img',img)
cv2.waitKey(0)
print(img.shape)

#resized output
cv2.imshow('resized_img',resized_img)
cv2.waitKey(0)
print(resized_img.shape)

#cropped
cropped_img = img[30:150,220:380]
cv2.imshow("cropped_image",cropped_img)
cv2.waitKey(0)
print(cropped_img.shape)

cv2.destroyAllWindows()