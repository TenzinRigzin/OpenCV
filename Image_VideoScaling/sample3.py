#modules
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np

def thresholding():
    root = os.getcwd()
    imagePath = os.path.join(root,"bird1.jpg")

    #reading the image
    image = plt.imread(imagePath)
    cvImage = cv2.imread(imagePath)
    grayImg = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    cvGrayImg = cv2.cvtColor(cvImage,cv2.COLOR_BGR2GRAY)

    #histogram plotting /window1
    hist = cv2.calcHist(grayImg,[0],None,[256],[0,256])

    plt.figure()
    plt.plot(hist)
    plt.xlabel("Binary value")
    plt.ylabel("No. of pixel")
    plt.show()

    #GrayScaleShow /window2
    cv2.imshow("GrayScaled",cvGrayImg)
    cv2.waitKey()
    cv2.destroyAllWindows()


    #threshold types
    option = [
        cv2.THRESH_BINARY,
        cv2.THRESH_BINARY_INV,
        cv2.THRESH_TOZERO,
        cv2.THRESH_TOZERO_INV,
        cv2.THRESH_TRUNC,
        
    ]
    threshold = ["binary", "binaryInv","toZero","toZeroInv","trunc"]

    #Grayscale Plotting /window3
    plt.figure()
    plt.subplot(231)
    plt.imshow(grayImg, cmap='gray')

    plt.show()

    
    #All threshold at once /window4
    plt.figure()
    for i in range(len(option)):
        plt.subplot(2,3,i+1)
        _,imgThres = cv2.threshold(grayImg, 70,255,option[i])
        plt.imshow(imgThres, cmap='gray')
        plt.title(threshold[i])
        
    plt.show()


if __name__ == '__main__':
    thresholding()
