import os
import sys
import fnmatch
import shutil
from shutil import copyfile

#folderi u koji se fileovi kopiraju
fo20 = r'C:\Users\Luka\Desktop\Kopiranje\kopiranje\2020'
os.listdir(fo20)
fo50 = r'C:\Users\Luka\Desktop\Kopiranje\kopiranje\5020'
os.listdir(fo50)


def find_files(search_path):

   for root, dir, files in os.walk(search_path):
        for file in files:
            if fnmatch.fnmatch(file, '*_5020*'):
##                print(root + '\\' +file)
                if file not in os.listdir(fo50):
                    shutil.copy(root + '\\' + file, fo50)
            elif fnmatch.fnmatch(file, '*_2020*'):
##                print(root + '\\' + file)
                if file not in os.listdir(fo20):
                    shutil.copy(root + '\\' + file, fo20)

##search path je path direktorija za pretragu
find_files(r'C:\Users\Luka\Desktop\Kopiranje\Podaci')

#fixanje crasha exea
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__) 
