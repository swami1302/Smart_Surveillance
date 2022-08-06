import cv2
import imutils
from main import Detector

img = cv2.imread('D:\python\people_detection\\1.jpg')
img = imutils.resize(img,700)
img = Detector(img)
cv2.waitKey(0)
cv2.destroyAllWindows()