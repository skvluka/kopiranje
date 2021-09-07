import os
import fnmatch
from shutil import copyfile
import shutil

fo20 = '/home/korisnik/Desktop/Projekti/Kopiranje/Podaci/2020'
os.listdir(fo20)
fo50 = '/home/korisnik/Desktop/Projekti/Kopiranje/Podaci/5020'
os.listdir(fo50)

for file20 in os.listdir('.'):
    if fnmatch.fnmatch(file20, '*_2020'):
        #print(file20)
        shutil.copy(file20,fo20)

for file50 in os.listdir('.'):
    if fnmatch.fnmatch(file50, '*_5020'):
        #print(file50)
        shutil.copy(file50,fo50)