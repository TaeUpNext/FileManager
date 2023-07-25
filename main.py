#Imports requtired librareis 
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import *
from zipfile import ZipFile as zf

print(f'\n This is Taés File Management Automaiton\n ')

#reads and prints the content of the file 
def READFILE(): 
  starterFile = fd.askopenfilename()#file/folder you want to change  
  fileRead = open(starterFile, 'r')
  print(f'\n {fileRead.read()} \n')

#unzips file
def EXTRACTZIP():
  fileOrDirectory = int(input("Do you want to extract a zip file or folder? \n1. File: \n2. Folder: \n\nYour Choice: "))
  if fileOrDirectory == 1:
    starterFile = fd.askopenfilename() #file/folder you want to extract
    zip.extract(starterFile)
  
  elif fileOrDirectory ==2:
    starterFolder = fd.askdirectory()


managerChoice = int(input('What would you like to do today? \n\n1. Read Contents of File: \n2. Extract Zi File \n\nYour Choice:  '))
if managerChoice == 1:
  READFILE()

elif managerChoice ==2:
  EXTRACTZIP()
