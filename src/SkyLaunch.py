from tkinter import *
from tkinter import filedialog
from pref_merger import merge
import os
from os import listdir
from os.path import isfile, join

formats = [".bsa",".esm",".esp"]
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
        if name[-3:] == "esm":
            data.remove(name)
            data.insert(0,name)
            
    for k in range(len(data)-1):
        if data[k][:-3] == data[k+1][:-3]:
            if data[k][-3:] == "bsa" and data[k+1][-3:] == "esp":
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
    final = []
    for k,elem in enumerate(raw_data):
        if checks_var[k].get() == 1:
            final.append(elem)
    create_data_file(plugin_folder,final)

def get_dir(msg):
    options = {}
    options['initialdir'] = os.getcwd()
    options['title'] = msg
    options['mustexist'] = False
    print(msg)
    path = filedialog.askdirectory(**options)
    return path
    
            
        
if __name__ == '__main__':
    tk = Tk()
    
    print("Plugin file creation or Edit Parameters ? (o/x)")
    inp = input(">>> ")
    if inp == "o":
        Dchks = Frame(tk)
        Dchks.pack(side=TOP)
        options = {}
        options['initialdir'] = os.getcwd()
        options['title'] = "Select your data folder"
        options['mustexist'] = False
        print("Select your data folder")
        data_folder = filedialog.askdirectory(**options)
        print("Select your plugin folder")
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
    else:
        skypref = get_dir("Select your SkyrimPref.ini")
        spec = get_dir("Select your graphic setting file (.ini | ex : low.ini")
        merge(skypref,spec)
        
        
#can = Canvas(width=800,height=600)
#can.pack()

#tk.mainloop()
