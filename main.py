import tkinter as tk
from tkinter import filedialog as fd
from tkinter import *
print(f'\n This is Taés File Management Automaiton\n ')


starterFile = fd.askopenfilename()#file/folder you want to change

#print/read the contents of a file
fileRead = open(starterFile, 'r')

print(f'\n {fileRead.read()} \n')
