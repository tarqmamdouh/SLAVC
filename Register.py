import win32api as wapi
import os
import numpy as np

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys

def key_to_output(keys):
    #        [A,W,D]
    output = [0,0,0]
    if 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    else :
        output[1] = 1

    return output

def load_file_status(file_name):
    if os.path.isfile(file_name):
        print('File exists, The driver continues')
        Data = list(np.load(file_name))
    else :
        print ('File does not exist, the driver will start normally')
        Data = []
    return  Data

