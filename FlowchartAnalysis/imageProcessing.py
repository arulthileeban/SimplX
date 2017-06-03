import numpy as np
from matplotlib import pyplot as plt
import cv2
import ocr
import erc
import beautifier as bf

def get(str):
    str = "TestImages/" + str
    t = cv2.imread(str, 1)
    t2 = cv2.cvtColor(t, cv2.COLOR_BGR2GRAY)
    return t.copy(), t2.copy()

if __name__ == '__main__':
    getFinal("flow.jpg")
    getFinal("flow2.jpg")
    getFinal("flow3.jpg")
