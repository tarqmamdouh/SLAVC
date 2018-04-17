import numpy as np
import  Eyes
import cv2
import time
from Dinput import PressKey, ReleaseKey, W, A, S, D
from alexnet import alexnet
from Register import key_check

import random

WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCHS = 400
MODEL_NAME = 'CarNaiveDrive-{}-{}-{}-epochs-100K-data.model'.format(LR, 'SV',EPOCHS)

t_time = 0.09


def straight():
    ##    if random.randrange(4) == 2:
    ##        ReleaseKey(W)
    ##    else:
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
    print("Driver is Moving Stright")


def left():
    PressKey(W)
    PressKey(A)
    # ReleaseKey(W)
    ReleaseKey(D)
    # ReleaseKey(A)
    time.sleep(t_time)
    ReleaseKey(A)
    print("Driver is Moving left")


def right():
    PressKey(W)
    PressKey(D)
    ReleaseKey(A)
    # ReleaseKey(W)
    # ReleaseKey(D)
    time.sleep(t_time)
    ReleaseKey(D)
    print("Driver is Moving right")


model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)


def main():
    last_time = time.time()
    for i in list(range(5))[::-1]:
        print("Your Testing Neural Network will start in : " + str(i + 1))
        time.sleep(1)

    paused = False
    while (True):

        if not paused:
            # 800x600 windowed mode
            # screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
            screen = Eyes.FrontFrameCapture()
            # print('loop took {} seconds'.format(time.time() - last_time))
            # last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (160, 120))

            prediction = model.predict([screen.reshape(160, 120, 1)])[0]
            print(prediction)

            turn_thresh = .90
            fwd_thresh = 0.40

            if prediction[1] > fwd_thresh:
                straight()
            elif prediction[0] > turn_thresh:
                left()
            elif prediction[2] > turn_thresh:
                right()
            else:
                straight()

        keys = key_check()

        # p pauses game and can get annoying.
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(A)
                ReleaseKey(W)
                ReleaseKey(D)
                time.sleep(1)


main()