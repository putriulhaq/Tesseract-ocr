from PIL import Image
import pytesseract
from pytesseract import Output
import cv2
from matplotlib import pyplot as plt

# print(pytesseract.image_to_string(Image.open('testocr.png')))


# img=cv2.imread('testocr.png')
img=cv2.imread('ipb.jpg')
print(img)
custom_config = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(img, config=custom_config))

print(img.shape)
h,w,c = img.shape

# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
boxes = pytesseract.image_to_boxes(img)
print(boxes.splitlines())
for b in boxes.splitlines():
    b = b.split(' ')
    img_new = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
# cv2.imshow('img', img)
plt.imshow(img_new)
plt.axis('off')  # Turn off axis
plt.show()
