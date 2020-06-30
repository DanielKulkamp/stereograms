import cv2 as cv
import sys
import numpy as np
import random
fore = cv.imread("./fore2.png")

if fore is None:
    sys.exit("Could not read the image.")

depthmap = cv.imread("./cafe.png", cv.IMREAD_GRAYSCALE)

final = cv.imread("./fore2.png")

for (i, row) in enumerate(depthmap):
    for (j, pixel) in enumerate(row):
        if pixel != 0:
            #print (f"i={i}, j={j}, pixel={pixel}" )
            final[i][j] = fore[i][j+30]
            


cv.imshow("Foreground", fore)

cv.imshow("Final", final)

k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("./final2.png", final)
    print(f"saving")
