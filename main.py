
import sys

import numpy as np
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QFormLayout, QPushButton
from cv2 import *


class Window(QWidget):

    def getNewNum(self):
        image = getImage()
        self.imageCaptureLabel2.setText("successful")
        print(image.shape[0])

        strFromImg = imageToString(image)

        print("Str from image: \n" + strFromImg)

        randomNumber = getRand(strFromImg)

        print("random num: ")
        print(randomNumber)

        self.randNumLabel2.setText(str(randomNumber))

        print("done1")

        self.pixmap = QPixmap("images/filename.jpg")
        self.pictureLabel.setPixmap(self.pixmap)

        print("done2")

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Number generator")
        self.setGeometry(100, 100, 400, 100)
        self.move(400, 200)
        # Create a QFormLayout instance
        layout = QFormLayout()
        # Add widgets to the layout

        self.imageCaptureLabel1 = QLabel("Image capture:")
        self.imageCaptureLabel2 = QLabel("none")
        self.imageCaptureLabel1.setFont(QFont('Arial', 10))
        self.imageCaptureLabel2.setFont(QFont('Arial', 10))
        layout.addRow(self.imageCaptureLabel1, self.imageCaptureLabel2)


        self.randNumLabel1 = QLabel("Random Number:")
        self.randNumLabel2 = QLabel("?")
        self.randNumLabel2.setFont(QFont('Arial', 10))
        self.randNumLabel1.setFont(QFont('Arial', 10))
        # self.nameLabel2.setWordWrap(True)
        layout.addRow(self.randNumLabel1, self.randNumLabel2)

        self.pictureLabel = QLabel()
        self.pixmap = QPixmap("images/placeholder.jpg")
        self.pictureLabel.setPixmap(self.pixmap)
        self.pictureLabel.setScaledContents(True)
        # self.pictureLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        layout.addRow(self.pictureLabel)


        button = QPushButton('Get random number')
        button.setToolTip('Click for a random number')
        button.move(100, 70)
        button.clicked.connect(self.getNewNum)
        layout.addRow(button)

        # Set the layout on the application's window
        self.setLayout(layout)



def getImage():
    # initialize the camera
    cam = VideoCapture(0)  # 0 -> index of camera

    img = np.zeros((100, 100, 3), np.uint8)
    s, img = cam.read()
    if s:  # frame captured without any errors
        # namedWindow("Image capture sample")
        # imshow("Image capture sample", img)
        # waitKey(0)
        # destroyWindow("Image capture sample")
        imwrite("images/filename.jpg", img)  # save image

    return img

def imageToString(img):
    img_2 = img/255*100

    # converted_string = img.tostring()
    # converted_string = base64.b64encode(img)
    converted_string = np.array2string(img_2, separator='',
                      suppress_small=True)

    final_str = converted_string.replace('[','').replace(']','').replace('\n','').replace(' ','').replace('.','')
    return final_str

# def getHash(imgStr):
#     result = hashlib.sha1(imgStr.encode())
#     return result

def getRand(numString):
    length = len(numString)

    print(type(numString))
    start = int(length/2)

    end = start + 10

    # slice to get a section of the string
    cut_str = numString[start:end]

    # convert to a number
    return int(cut_str) / 10000000000





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())




