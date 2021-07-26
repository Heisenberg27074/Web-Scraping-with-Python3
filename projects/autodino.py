import pyautogui
from PIL import Image,ImageGrab
from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
        #draw rectangle for birds
    for i in range(680,720):
        for j in range(220,280):
            if data[i,j]<100:
                hit('down')
                return

#for cactus
    for i in range(765,800):
        for j in range(285,330):
            if data[i,j]<100:
                hit('up')
                return
    return
if __name__ == '__main__':
    print("Hey..dino game is about to start in 3 seconds")

    time.sleep(3)

    while True:
        image=ImageGrab.grab().convert('L')
        data=image.load()
        #print(asarray(image))
        isCollide(data)

         #draw rectangle for cactus
    '''    for i in range(745,785):
            for j in range(282,330):
                hit('up')

                data[i,j]=0

            #draw rectangle for birds
        for i in range(680,710):
            for j in range(220,280):
                data[i,j]=71
        image.show()
        break'''
