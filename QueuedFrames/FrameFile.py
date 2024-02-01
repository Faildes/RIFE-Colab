import cv2
import numpy
import os

class FrameFile:
    filePath: str = None
    imageData = None

    def __init__(self, filePath: str):
        self.filePath = filePath

    def __str__(self):
        return self.filePath

    def swapfilePath(self, newPath: str):
        self.filePath = newPath

    def setImageData(self, imageData):
        self.imageData = imageData

    def getImageData(self):
        return self.imageData

    def saveImageData(self):
        if not os.path.exists(self.filePath):
            cv2.imwrite(self.filePath, self.imageData)

    def loadImageData(self):
        self.imageData = cv2.imread(self.filePath,cv2.IMREAD_UNCHANGED)

