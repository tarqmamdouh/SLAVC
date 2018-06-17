import Eyes
import Controller
import Detector
import Dinput
import Register
import time
import cv2
import numpy as np
from Dinput import PressKey, ReleaseKey, ChangeView, W, A, S, D

starting_value = 1

if __name__ == '__main__':

    #constants (prerequisites)
    last_time = time.time()
    starting_value = starting_value
    file_name = 'Coordinates'
    Data = Register.load_file_status(file_name)
    paused = False

    ## Wait A little bit before start
    for i in list(range(10))[::-1]:
        print("Please Prepare every thing the drive will start in : " + str(i + 1))
        time.sleep(1)



    i = 0
    ## Start The program
    while True:

        if paused :
            continue

        PFrame = Eyes.FrontFrameCapture()
        PFrame = cv2.cvtColor(PFrame,cv2.COLOR_BGR2GRAY)
        PFrame = cv2.resize(PFrame,(480,270))
        keys = Register.key_check()
        output = Register.key_to_output(keys)
        Data.append([PFrame,output])

        # Save Bulk
        if len(Data) % 1000 == 0:
            print("################### Saving Bulk Number : " + str(i + 1) + "###################")
            np.save('Naive-Data\\' + file_name + '-' + str(i+1) + '.npy', Data)
            i = i +1
            Data.clear()


        # print('Loop took {} Seconds'.format(time.time() - last_time))
        # last_time = time.time()

        if 0xFF == ord('q'):
            cv2.destroyAllWindows()
            ReleaseKey(ChangeView)
            break



        # unneccssory Staff for now
        # PFrame, original_image, m1, m2 = Detector.Detect(PFrame)
        # cv2.imshow('Front', original_image)
        # cv2.waitKey(1)

