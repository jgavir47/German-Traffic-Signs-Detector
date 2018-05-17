from sklearn import linear_model
import numpy as np
import cv2

for i in range (43):
    if (i < 10):
        imagen= cv2.imread("/home/nasa1/RETO_KIWI/German-Traffic-Signs-Detector/images/test/FullIJCNN2013/0"+str(i)+"/00000.ppm")
    else:
        imagen = cv2.imread("/home/nasa1/RETO_KIWI/German-Traffic-Signs-Detector/images/test/FullIJCNN2013/"+str(i)+"/00000.ppm")
        cv2.imshow("image", imagen)
        cv2.waitKey()
        cv2.destroyAllWindows()
