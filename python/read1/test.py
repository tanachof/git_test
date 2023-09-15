
import os
import glob
import read2.printsum as read


print("1")
print("2")


exe_file_path = __file__
dirname = os.path.dirname(exe_file_path)

img = glob.glob(dirname + "/*/*.py" )

print(dirname)
print(img)

read.printsum()