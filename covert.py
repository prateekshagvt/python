
import cv2
image=cv2.imread("rose.png")
grey_filter = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imwrite("output2.png",grey_filter)



