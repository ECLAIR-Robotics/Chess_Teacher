from tracemalloc import start
import cv2 as cv2
import numpy as np
vs = cv2.VideoCapture(1)


def draw_crosshairs(img, offset, color):
    height = img.shape[0]
    width = img.shape[1]
    center_x = int(width/2)
    center_y = int(height/2)

    copy = img.copy()
    #                     x       y
    cv2.drawMarker(copy, (center_x, center_y), color,
                   markerType=cv2.MARKER_CROSS, thickness=2)
    cv2.drawMarker(copy, (center_x-offset, center_y-offset),
                   color, markerType=cv2.MARKER_CROSS, thickness=2)
    cv2.drawMarker(copy, (center_x+offset, center_y-offset),
                   color, markerType=cv2.MARKER_CROSS, thickness=2)
    cv2.drawMarker(copy, (center_x+offset, center_y+offset),
                   color, markerType=cv2.MARKER_CROSS, thickness=2)
    cv2.drawMarker(copy, (center_x-offset, center_y+offset),
                   color, markerType=cv2.MARKER_CROSS, thickness=2)

    cv2.imshow('ch', copy)


def get_image():
    ret, frame = vs.read()
    # frame = cv2.resize(frame, (640, 480), interpolation = cv2.INTER_AREA)
    if not ret:
        return None
    return frame



def calibrate():
    while True:
        
        frame = get_image()
        height = frame.shape[0]
        width = frame.shape[1]
        center_x = int(width/2)
        center_y = int(height/2)
        frame = frame[center_x - 150:center_x + 150, center_y - 50:center_y + 200]
        draw_crosshairs(frame, 100, (0, 0, 255))
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        green = np.uint8([[[0, 255, 0]]])
        hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)

        # define kernel size
        kernel = np.ones((7, 7), np.uint8)
        # Remove unnecessary noise from mask
        # mask basically gets a black and white image of the decided color
            # bitwise_and adds it to the original image
        mask = cv2.blur(frame, (20, 25))
        mask = cv2.GaussianBlur(mask, (5, 5), 0)
        
        # for green color in gimp hsv the range is 70 -  140 | for opencv it is 30 - 60
        mask = cv2.inRange(hsv, (0, 0, 180), (180, 30, 220))

        # mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        # mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        # res = cv2.bitwise_or(frame, frame, mask=mask)
        cv2.imshow('frame', mask)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

if __name__ == "__main__":

    calibrate()

    # frame = get_image()
    # draw_crosshairs(frame, 100, (0, 0, 255))
    # cv2.imshow('frame', frame)
    # key = cv2.waitKey(1) & 0xFF

    # # Write Filter
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # green = np.uint8([[[0, 255, 0]]])
    # hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)

    # # define kernel size
    # kernel = np.ones((7, 7), np.uint8)
    # # Remove unnecessary noise from mask
    # # mask basically gets a black and white image of the decided color
    #     # bitwise_and adds it to the original image
    # mask = cv2.blur(frame, (20, 25))
    # mask = cv2.GaussianBlur(mask, (5, 5), 0)

    #    # for green color in gimp hsv the range is 70 -  140 | for opencv it is 30 - 60
    # mask = cv2.inRange(hsv, (150, 0, 70), (170, 10, 70))

    # mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    # mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # res = cv2.bitwise_or(frame, frame, mask=mask)

    #     # res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    # params = cv2.SimpleBlobDetector_Params()

    # params.filterByCircularity = True
    # params.minCircularity = 0.5

    # detector = cv2.SimpleBlobDetector_create(params)
    # keypoints = detector.detect(mask)

    # blank = np.zeros((1, 1))
    # blobs = cv2.drawKeypoints(mask, keypoints, blank, (0, 0, 255),
    #                                 cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # contours, _ = cv2.findContours(
    #     mask.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # if (len(contours) > 0):
    #     c = max(contours, key=cv2.contourArea)
    #         # Set Bounding Box
    #     x, y, w, h = cv2.boundingRect(c)
    #     startpt = (x, y)
    #     endpt = (x+w, y+h)
    #     frame = cv2.rectangle(frame, startpt, endpt, (255, 255, 0), 1)

    #     # contours = sorted(contours, key=cv2.contourArea, reverse=True)
    #     if( len(contours) > 0):
    #         c = max(contours, key=cv2.contourArea)
    #         #Set Bounding Box
    #         x,y,w,h = cv2.boundingRect(c)
    #         startpt = (x, y)
    #         endpt = (x+w, y+h)
    #         frame = cv2.rectangle(frame, startpt, endpt, (255, 255, 0), 1)

        #uncomment this to box all the contours

        
        
        
        # #Display Code
        # cv2.imshow("Masked", mask)
        # cv2.imshow("Original", frame)
        # cv2.imshow("Result", res)

        # # you can comment this out if you don't want to see the blobs
        # cv2.imshow("Blobs", blobs)



    cv2.destroyAllWindows()
