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
        file.write(name+'\n')
    file.close()

def create_checks(data):
    for k,raw in enumerate(data):
        checks.append(Checkbutton(Dchks,text=raw,variable=checks_var[k]))

def write_data():
    for k,elem in enumerate(raw_data):
        if checks_var[k].get() == 0:
            raw_data.remove(elem)
    create_data_file(plugin_folder,raw_data)
    tk.destroy()
            
        
if __name__ == '__main__':
    tk = Tk()
    Dchks = Frame(tk)
    Dchks.pack(side=TOP)

    options = {}
    options['initialdir'] = os.getcwd()
    options['title'] = "Select your data folder"
    options['mustexist'] = False
    
    data_folder = filedialog.askdirectory(**options)
    options['title'] = "Select your plugin folder"
    plugin_folder = filedialog.askdirectory(**options)

    raw_data = find_data_files(data_folder)

    checks_var = [IntVar() for i in range(len(raw_data))]
    checks = []
    create_checks(raw_data)
    for elem in checks:
        elem.pack(side=TOP)
    Write_button = Button(Dchks,text="Done",command=write_data)
    Write_button.pack()

#can = Canvas(width=800,height=600)
#can.pack()

#tk.mainloop()
