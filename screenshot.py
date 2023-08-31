import cv2
def ss():
    # Opens the inbuilt camera of laptop to capture video.
    webCam = cv2.VideoCapture("f1.mp4")
    currentframe = 0

    while (True):
        success, frame = webCam.read()


        cv2.imshow("Output", frame)
        cv2.imwrite('static/'+'Frame' + str(currentframe) + '.jpg', frame)
        currentframe += 1
        if cv2.waitKey(1) & currentframe == 1:
             break

    webCam.release()

    webCam1 = cv2.VideoCapture("f2.mp4")
    #webCam1 = cv2.VideoCapture("http://192.168.140.173:8080/video")
    currentframe1 = 1

    while (True):
        success, frame1 = webCam1.read()


        cv2.imshow("Output1", frame1)
        cv2.imwrite('static/'+'Frame' + str(currentframe1) + '.jpg', frame1)
        currentframe1 += 1

        if cv2.waitKey(1) & currentframe1 == 2:
            break

    webCam1.release()

    webCam2 = cv2.VideoCapture("f3.mp4")
    #webCam2 = cv2.VideoCapture("http://192.168.140.176:8080/video")
    currentframe2 = 2

    while (True):
        success, frame2 = webCam2.read()


        cv2.imshow("Output1", frame2)
        cv2.imwrite('static/'+'Frame' + str(currentframe2) + '.jpg', frame2)
        currentframe2 += 1

        if cv2.waitKey(1) & currentframe2 == 3:
            break

    webCam2.release()

    webCam3 = cv2.VideoCapture("f4.mp4")
    currentframe3 = 3

    while (True):
        success, frame3 = webCam3.read()


        cv2.imshow("Output1", frame3)
        cv2.imwrite('static/'+'Frame' + str(currentframe3) + '.jpg', frame3)
        currentframe3 += 1

        if cv2.waitKey(1) & currentframe3 == 4:
            break

    webCam3.release()



cv2.destroyAllWindows()