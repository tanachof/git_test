
import os
import glob
import read2.printsum as read
import numpy as np
import csv
import time
import cfg
import sys
import ctypes

camdll = ctypes.cdll.LoadLibrary(r"C:\Users\t36co\Documents\git_test\python\get_cam")
addi = camdll.add_int
addi.argtypes=(ctypes.c_int,ctypes.c_int)
addi.restype = ctypes.c_int
print(addi(50,5))

class caminfo(ctypes.Structure):
    _fields_ = [("cam1",ctypes.c_int),("cam2",ctypes.c_int),("cam3",ctypes.c_int),("cam4",ctypes.c_int)]


cam_num = camdll.cam_number
cam_num.argtypes=(ctypes.POINTER(ctypes.c_char_p),ctypes.c_int)
cam_num.restype = caminfo

def get_cam(strings):
    string_array = (ctypes.c_char_p * len(strings))(*strings)
    
    # C関数を呼び出し
    cam_numbers =cam_num(string_array, len(strings))
    return cam_numbers

camlist = [b"svm1",b"svm2",b"svm3",b"svm4"]

vector_c = get_cam(camlist)
print('x={},y={},z={},w ={}'.format(vector_c.cam1,vector_c.cam2,vector_c.cam3,vector_c.cam4))

print("1")
print("2")


exe_file_path = __file__
dirname = os.path.dirname(exe_file_path)

img = glob.glob(dirname + "/*/*.py" )

print(dirname)
print(img)


read.printsum()

os.makedirs(r"C:\Users\t36co\Documents\test99",exist_ok=True)
