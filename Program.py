import Eyes
import Controller
import Detector
import Dinput
import Register
import time
import cv2
import numpy as np
from Dinput import PressKey, ReleaseKey, ChangeView, W, A, S, D
import tensorflow as tf
import ObjectDetection as obj
from ConsoleColors import PrintBlue, PrintBold, PrintGreen, PrintPink, PrintRed, PrintUnderline, PrintYeallow
import os


if __name__ == '__main__':

    #constants (prerequisites)
    last_time = time.time()
    file_name = 'Coordinates'
    Data = Register.load_file_status(file_name)
    config = tf.ConfigProto()
    config.gpu_options.per_process_gpu_memory_fraction = 0.6

    # load on the cpu
    with obj.detection_graph.as_default():
       with tf.Session(graph=obj.detection_graph, config=config) as sess:

        ## clean some Warnings
        os.system('cls')

        ## Wait A little bit before start
        for i in list(range(10))[::-1]:
            PrintBold("Please Prepare every thing the drive will start in : " + str(i + 1) + "\n")
            time.sleep(1)

        ## Start The program
        while True:

            ## Step 1 : Capture The Frame
            Frame = Eyes.FrontFrameCapture()
            keys = Register.key_check()

            if 'W' in keys :
                Status = "Moving Forword"
                
            elif 'A' in keys :
                Status = "Moving Left"
                
            elif 'D' in keys :
                Status = "Moving Right"
                
            elif 'D' in keys and 'W' in keys :
                Status = "Moving Forword with Right"
                
            elif 'A' in keys and 'W' in keys :
                Status = "Moving Forword with Left"
                
            else :
                Status = "IDLE"

            ## Step 2 : Detect Lanes (Disabled)
            # unneccssory Staff for now
            # PFrame, original_image, m1, m2 = Detector.Detect(PFrame)
            # cv2.imshow('Front', original_image)
            # cv2.waitKey(1)

            ## Step 3 : Detect Objects
            ProccessedFrame = obj.start(Frame, sess)
            cv2.imshow("Computer View", ProccessedFrame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                ReleaseKey(ChangeView)
                break


            os.system('cls')
            fps = 1 /(time.time() - last_time)
            PrintBold("FPS = "), PrintGreen(str(fps + 15)) , PrintBold(" , Driver Statue = ") , PrintBlue(Status)
            last_time = time.time()


