from tkinter import *

class Application:
    def __init__(self):
        self.tk = Tk()
        #Header
        
        self.header = Frame(self.tk)
        self.path_but = Button(self.header, text="Path to Skyrim folder")
        self.path_label = Label(self.header, text="Path not set yet")
        self.merge_but = Button(self.header, text="Merge difficulty file")
        
        self.header.pack(side=TOP)
        self.path_but.pack(side=LEFT)
        self.path_label.pack(side=LEFT)
        self.merge_but.pack(side=LEFT)

        #Content
        
        self.content = Frame(self.tk)
        self.title_label = Label(self.content, text="Mods Management")
        self.scroll_frame = Frame(self.content,relief=GROOVE,width=50,height=100,bd=1)
        self.scroll_frame.pack(side=LEFT)
        self.scroll_canvas = Canvas(self.scroll_frame)
        self.mods_list = Frame(self.scroll_canvas)
        self.scrollbar = Scrollbar(self.scroll_frame,orient="vertical",command=self.scroll_canvas.yview)
        self.scroll_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.create_but = Button(self.content, text="Create Plugins.txt")
        

        self.content.pack(side=BOTTOM)
        self.title_label.pack(side=TOP)
        
        self.scrollbar.pack(side=RIGHT,fill="y")
        self.scroll_canvas.pack(side=LEFT)
        self.scroll_canvas.create_window((0,0),window=self.mods_list,anchor='nw')
        
        self.create_but.pack(side=BOTTOM)

        #Events
        self.mods_list.bind("<Configure>",self.scroll_upd)

        #Other
        self.data()
        #End
        self.tk.mainloop()
    def scroll_upd(self,event):
        self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox("all"),width=200,height=200)

    def data(self):
        for i in range(50):
           Label(self.mods_list,text=i).grid(row=i,column=0)
           Label(self.mods_list,text="my text"+str(i)).grid(row=i,column=1)
           Label(self.mods_list,text="..........").grid(row=i,column=2)

if __name__ == '__main__':
    app = Application()
        
        
