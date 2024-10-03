#!/usr/bin/env python
# coding: utf-8

# In[1]:Write your code to find the histogram of gray scale image and color image channels


import cv2
import matplotlib.pyplot as plt
gray_image = cv2.imread("gray image of flower.jpg")
color_image = cv2.imread()
cv2.imshow("Gray Image",gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[2]:Display the histogram of gray scale image and any one channel histogram from color image


import matplotlib.pyplot as plt 
grayscale_image=cv2.imread("gray image of flower.jpg")
colourscale_image=cv2.imread("color image of flower.jpg")
hist=cv2.calcHist(grayscale_image,[0],None,[255],[0,255])
hist1=cv2.calcHist()
plt.figure()
plt.title("Histogram")
plt.xlabel("")
plt.ylabel("pixel count")
plt.stem()
plt.show()



# In[3]:Write the code to perform histogram equalization of the image. 



import cv2
import matplotlib.pyplot as plt 
gi=cv2.imread("gray image of flower.jpg",0)
colorscale=cv2.imread("color image of flower.jpg")
g=cv2.resize(gi,(500,400))
equ=cv2.equalizeHist(gi)

import cv2
import matplotlib.pyplot as plt
gray_image = cv2.imread(r"C:\Users\admin\Downloads\gray--gray.jpg", cv2.IMREAD_GRAYSCALE)  
color_image = cv2.imread(r"C:\Users\admin\Downloads\gray .jpg") 
cv2.imshow("Gray Image",gray_image)
cv2.imshow("Color Image",color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import matplotlib.pyplot as plt

gray_image = cv2.imread(r"C:\Users\admin\Downloads\gray--gray.jpg", cv2.IMREAD_GRAYSCALE)  
color_image = cv2.imread(r"C:\Users\admin\Downloads\gray .jpg") 

gray_hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
color_hist = cv2.calcHist([color_image], [0], None, [256], [0, 256])

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.plot(gray_hist, color='black')

plt.subplot(1, 2, 2)
plt.title("Color Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.plot(color_hist, color='blue')

plt.tight_layout()
plt.show()

import cv2
import matplotlib.pyplot as plt
gray_image = cv2.imread(r"C:\Users\admin\Downloads\gray--gray.jpg", cv2.IMREAD_GRAYSCALE)
color_image = cv2.imread(r"C:\Users\admin\Downloads\gray .jpg")
resized_gray_image = cv2.resize(gray_image, (500, 400))
equalized_image = cv2.equalizeHist(gray_image)
cv2.imshow("Original Grayscale Image", gray_image)
cv2.waitKey(0)

cv2.imshow("Resized Grayscale Image", resized_gray_image)
cv2.waitKey(0)
cv2.imshow("Equalized Grayscale Image", equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.figure()

plt.subplot(1, 2, 1)
plt.title("Original Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
gray_hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
plt.plot(gray_hist)

plt.subplot(1, 2, 2)
plt.title("Equalized Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
equalized_hist = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])
plt.plot(equalized_hist)

plt.tight_layout()
plt.show()









