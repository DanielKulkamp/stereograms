import cv2 as cv
import sys
import numpy as np
import random


def main(argv):
    if len(argv) < 3:
        print("Usage: stereogram <inputfile> <depthmap> <outputfile> [-f=<forceshiftvalue>] [-r=<S>]")

    fore = cv.imread(argv[0])
    if fore is None:
        sys.exit("Could not read the image.")

    depthmap = cv.imread(argv[1], cv.IMREAD_GRAYSCALE)
    if depthmap is None:
        sys.exit("Could not read the depthmap image.")
    
    final = cv.imread(argv[0])


    force = None #anti pattern?
    for arg in argv[3:]:
        if arg[:3] == '-f=':
            try:
                force = int(arg[3:])
            except ValueError as e:
                print(f"{e}")
                sys.exit("invalid force shift input")
            except:
                sys.exit("An exception occurred")

        if arg[:3] == '-r=':
            try:
                width = int(arg[3:])
            except ValueError as e:
                print(f"{e}")
                sys.exit("invalid force shift input")
            except:
                sys.exit("An exception occurred")
            print(f"fore.shape={fore.shape}, fore.dtype{fore.dtype}")
            pattern = np.zeros([width, width, 3], np.uint8)
            for (i, row) in enumerate(pattern):
                for( j, col ) in enumerate(row):
                    pattern[i][j] = [ random.randrange(255), random.randrange(255), random.randrange(255)]
            for (i, row) in enumerate(fore):
                for (j, col) in enumerate(row):
                    fore[i][j] = pattern[i%width][j%width]
                    final[i][j] = fore[i][j]


    for (i, row) in enumerate(depthmap):
        for (j, pixel) in enumerate(row):
            if pixel != 0:
                if force is None:
                    final[i][j] = fore[i][j-depthmap[i][j]]
                else:
                    final[i][j] = fore[i][j-force]

            
    cv.imshow("Foreground", fore)
    cv.imshow("Final", final)

    k = cv.waitKey(0)
    if k == ord("s"):
        cv.imwrite(argv[2], final)
        print(f"saving {argv[2]}")

if __name__ == '__main__':
    print(sys.argv)
    main(sys.argv[1:])
