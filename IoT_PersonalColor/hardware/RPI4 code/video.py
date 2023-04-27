import cv2
import cvlib as cv
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from threading import Thread
import time


#import os
#os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH")

class video(QObject):
    sendImage = pyqtSignal(QImage)

    def __init__(self, widget, size):
        super().__init__()
        self.widget = widget
        self.size = size
        self.sendImage.connect(self.widget.recvImage)

        files = ['haarcascade_fullbody.xml',
                 'haarcascade_upperbody.xml',
                 'haarcascade_lowerbody.xml',
                 'haarcascade_frontalface_default.xml',
                 'haarcascade_eye.xml',
                 'haarcascade_eye_tree_eyeglasses.xml',
                 'haarcascade_smile.xml']

        self.filters = []
        for i in range(len(files)):
            filter = cv2.CascadeClassifier(files[i])
            self.filters.append(filter)

        self.option = [False for i in range(len(files))]
        self.color = [QColor(255, 0, 0), QColor(255, 128, 0), QColor(255, 255, 0), QColor(0, 255, 0), QColor(0, 0, 255),
                      QColor(0, 0, 128), QColor(128, 0, 128)]

    def setOption(self, option):
        self.option = option

    def startCam(self):
        try:
            self.cap = cv2.VideoCapture(0)
        except Exception as e:
            print('Cam Error : ', e)
        else:
            self.bThread = True
            self.thread = Thread(target=self.threadFunc)
            self.thread.start()

    def stopCam(self):
        self.bThread = False
        bopen = False
        try:
            bopen = self.cap.isOpened()
        except Exception as e:
            print('Error cam not opened')
        else:
            self.cap.release()


    def threadFunc(self):
        while self.bThread:
            ok, frame = self.cap.read()
            if ok:

                cv2.imwrite('photo.jpg', frame)
                imgs = cv2.imread('photo.jpg')
                faces, confidences = cv.detect_face(imgs)
                img2 = imgs

                dst = cv2.transpose(frame)
                dst = cv2.flip(dst,1)
                frame = dst
                cv2.imwrite('photo.jpg',frame)
                imgs = cv2.imread('photo.jpg')

                gray = cv2.cvtColor(imgs, cv2.COLOR_BGR2GRAY)

                criterion = 0.9999

                if confidences :

                    _conf_ = confidences.pop()
                    if _conf_ > criterion :
                        print('capture')
                        cv2.imwrite('photo.jpg',img2)
                        import os
                        os.system('python3 /home/pi/pythonProject/pytorchtest1.py')
                        self.stopCam()
                        self.widget.hide()

                        break
                    else:
                        pass




                # detect image
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                for i in range(len(self.filters)):
                    self.option[3]=True
                    self.option[4]=True
                    if self.option[i]:
                        detects = self.filters[i].detectMultiScale(gray, 1.1, 5)
                        for (x, y, w, h) in detects:
                            r = self.color[i].red()
                            g = self.color[i].green()
                            b = self.color[i].blue()
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (b, g, r), 2)

                            # create image
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb.shape
                bytesPerLine = ch * w
                img = QImage(rgb.data, w, h, bytesPerLine, QImage.Format_RGB888)
                resizedImg = img.scaled(self.size.width(), self.size.height(), Qt.KeepAspectRatio)
                #resizedImg = resizedImg2.rotate(90)
                self.sendImage.emit(resizedImg)
            else:
                pass
               # print('cam read error')

            time.sleep(0.01)

        print('thread finished')
