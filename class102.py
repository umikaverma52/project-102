import cv2
import time
import random
start_time=time.time()
def takeSnapShot():
    number = str(random.randint(0,100))

    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+number+".jpg"
        cv2.imwrite(img_name, frame)
        result=False
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def main():
    global start_time
    while(True):
        if ((time.time() - start_time) >= 10):
            takeSnapShot()
            start_time = time.time()

            
main()



    