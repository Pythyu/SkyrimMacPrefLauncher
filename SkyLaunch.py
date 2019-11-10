from tkinter import *
from tkinter import filedialog
import os
from os import listdir
from os.path import isfile, join

formats = [".esb",".bsa",".py"]
def find_data_files(path):
    data_files_path = []
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    for file in onlyfiles:
        name, ext = os.path.splitext(path+"/"+file)
        if ext in formats:
            data_files_path.append(path+"/"+file)
    return data_files_path

def parse_data(data):
    for k,elem in enumerate(data):
        name = elem.split('/')[-1]
        data[k] = name
    for k in range(len(data)):
        if data[k][-3:] == "bsa" and data[k+1][-3:] == "esb":
            data[k], data[k+1] = data[k+1], data[k]

def create_data_file(path,data):
    parse_data(data)
    file = open(path+'/plugins.txt','w')
    for name in data:
        file.writeline(name)
    file.close()
            
        

#tk = Tk()

#can = Canvas(width=800,height=600)
#can.pack()

#tk.mainloop()
