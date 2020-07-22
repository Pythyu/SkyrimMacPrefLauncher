from tkinter import *
from tkinter import filedialog
import os
from os import listdir
from os.path import isfile, join
import configparser

def merge(Pref_file,Spec_file):
    cfg_p = configparser.ConfigParser()
    cfg_s = configparser.ConfigParser()
    cfg_p.read(Pref_file)
    cfg_s.read(Spec_file)
    for st in cfg_s.sections():
        if st in cfg_p.sections():
            for key in cfg_s[st]:
                cfg_p[st][key] = cfg_s[st][key]
        else:
            cfg_p[st] = {}
            for key in cfg_s[st]:
                cfg_p[st][key] = cfg_s[st][key]
    
    with open(Pref_file, 'w') as configfile:
        cfg_p.write(configfile)

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



def get_dir(msg,file=False):
    if file:
        path =filedialog.askopenfilename(filetypes=(("ini files","*.ini"),("All files","*.*")))
    else:       
        options = {}
        options['initialdir'] = os.getcwd()
        options['title'] = msg
        options['mustexist'] = False
        path = filedialog.askdirectory(**options)
    return path


class Application:
    def __init__(self):
        self.raw_data = None
        
        self.tk = Tk()
        #Header
        
        self.header = Frame(self.tk)
        self.path_but = Button(self.header, text="Path to Skyrim folder",command=self.set_path)
        self.path_label = Label(self.header, text="Path not set yet")
        self.label = ""
        self.merge_but = Button(self.header, text="Merge difficulty file",command=self.merge_diff)
        
        self.header.pack(side=TOP)
        self.path_but.pack(side=LEFT)
        self.path_label.pack(side=LEFT)
        self.merge_but.pack(side=LEFT)

        #Content
        
        self.content = Frame(self.tk)
        self.title_label = Label(self.content, text="Mods Management")
        self.scroll_frame = Frame(self.content,relief=GROOVE,width=50,height=100,bd=1)
        self.scroll_frame.pack(side=RIGHT)
        self.scroll_canvas = Canvas(self.scroll_frame)
        self.mods_list = Frame(self.scroll_canvas)
        self.scrollbar = Scrollbar(self.scroll_frame,orient="vertical",command=self.scroll_canvas.yview)
        self.scroll_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.create_but = Button(self.content, text="Create Plugins.txt",command=self.write_data)
        

        self.content.pack(side=BOTTOM)
        self.title_label.pack(side=TOP)
        
        self.scrollbar.pack(side=RIGHT,fill="y")
        self.scroll_canvas.pack(side=LEFT)
        self.scroll_canvas.create_window((0,0),window=self.mods_list,anchor='nw')
        
        self.create_but.pack(side=BOTTOM)

        #Events
        self.mods_list.bind("<Configure>",self.scroll_upd)

        #Other
        
        #End
        self.tk.mainloop()
    def write_data(self):
        if self.raw_data is None:
            return
        final = []
        for k,elem in enumerate(self.raw_data):
            if self.checks_var[k].get() == 1:
                final.append(elem)
        create_data_file(self.label+"/%USERPROFILE%/Local Settings/Application Data/Skyrim",final)
    def set_path(self):
        self.label = get_dir("Select the path to your skyrim folder")
        self.path_label.configure(text=self.label)
        self.data()
    def merge_diff(self):
        spec = get_dir("Select your graphic setting file (.ini | ex : low.ini",True)
        try:
            merge(self.label+"/%USERPROFILE%/My Documents/My Games/Skyrim/SkyrimPrefs.ini",spec)
        except Exception as e:
            print("Process terminated due to error : ", e)
    def scroll_upd(self,event):
        self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox("all"),width=400,height=200)

    def data(self):
        try:
            self.raw_data = find_data_files(self.label+"/Data")

            self.checks_var = [IntVar() for i in range(len(self.raw_data))]
            self.checks = []
            for k,raw in enumerate(self.raw_data):
                self.checks.append(Checkbutton(self.mods_list,text=raw.split('/')[-1],variable=self.checks_var[k]))
                self.checks[k].grid(row=k,column=0)

        except Exception as e:
            print("Process terminated due to error : ", e)
##        for i in range(50):
##           Label(self.mods_list,text=i).grid(row=i,column=0)
##           Label(self.mods_list,text="my text"+str(i)).grid(row=i,column=1)
##           Label(self.mods_list,text="..........").grid(row=i,column=2)

if __name__ == '__main__':
    app = Application()
        
        
