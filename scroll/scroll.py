# from Tkinter import *
#
# root = Tk()
# scrollbar = Scrollbar(root)
# scrollbar.pack( side = RIGHT, fill=Y )
#
# mylist = Listbox(root, yscrollcommand = scrollbar.set )
# for line in range(100):
#    mylist.insert(END, "This is line number " + str(line))
#
# mylist.pack( side = LEFT, fill = BOTH )
# scrollbar.config( command = mylist.yview )
#
# mainloop()

from Tkinter import *

class zoomer(Tk):

    def __init__(self):
        x=100
        y=100
        Tk.__init__(self)
        self.border = 10
        self.size_x = x
        self.size_y = y

        #SIZE
        self.app_sizex = 200
        self.app_sizey = 200
        fontSize=int(x/20)

        self.title("Graphic")
        self.geometry(str(self.app_sizex+10) + "x" + str(self.app_sizey+40))

        #CANVAS + BORDER
        self.canvas = Canvas(self, width = self.app_sizex, height = self.app_sizey, scrollregion=(0,0,x,y))
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.canvas.create_line(self.border, self.border, self.border, y-self.border)
        self.canvas.create_line(x-self.border, self.border, x-self.border, y-self.border)
        self.canvas.create_line(self.border,   self.border, x-self.border, self.border)
        self.canvas.create_line(self.border, y-self.border, x-self.border, y-self.border)
        self.canvas.create_line(self.border,   self.border, x-self.border, y-self.border)
        text1=self.canvas.create_text(50, 50, fill="white",font=("Purisa", fontSize))
        self.canvas.itemconfig(text1, text="Graphic Text")

        #SCROLLING BARS
        self.vbar=Scrollbar(self,orient=VERTICAL)
        self.vbar.grid(row=0, column=1, sticky="ns")
        self.vbar.config(command=self.canvas.yview)
        self.hbar=Scrollbar(self,orient=HORIZONTAL)
        self.hbar.grid(row=2, column=0, sticky="ew")
        self.hbar.config(command=self.canvas.xview)
        self.canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)

        #zoom button
        save_button = Button(self, text = "Zoom")
        save_button["command"] = lambda: self.zoom_in()
        save_button.grid(row=3, column = 0, pady = 5)

    def zoom_in(self):
        #Clean canvas
        self.canvas.delete("all")
        self.size_x = int(self.size_x * 1.1)
        self.size_y = int(self.size_y * 1.1)
        x=self.size_x
        y=self.size_y
        fontSize=int(x/20)
        self.canvas.create_line(self.border, self.border, self.border, y-self.border)
        self.canvas.create_line(x-self.border, self.border, x-self.border, y-self.border)
        self.canvas.create_line(self.border, self.border, x-self.border, self.border)
        self.canvas.create_line(self.border, y-self.border, x-self.border, y-self.border)
        self.canvas.create_line(self.border,   self.border, x-self.border, y-self.border)
        text1=self.canvas.create_text(self.size_x/2, self.size_y/2, fill="white",font=("Purisa", fontSize) )
        self.canvas.itemconfig(text1, text="Graphic Text")
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        #SCROLLING BARS
        self.vbar.config(command=self.canvas.yview)
        self.hbar.config(command=self.canvas.xview)
        self.canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)


if __name__ == '__main__':
    my_gui=zoomer()
    my_gui.mainloop()

# from Tkinter import *
#
# class Graphic(Tk):  #Graphical Interface
#     def __init__(self, x, y):
#
#         #INITIALIZATION
#         Tk.__init__(self)
#         self.border = 10
#         self.size_x = x
#         self.size_y = y
#         self.mouse = ""
#         self.cross_list = []
#         self.mode = ""
#
#         #SIZE
#         self.app_sizex = 1800
#         self.app_sizey = 1000
#
#
#         self.title("Graphic")
#         self.geometry(str(self.app_sizex+10) + "x" + str(self.app_sizey+40))
#
#         #CANVAS + BORDER
#         self.canvas = Canvas(self, width = self.app_sizex, height = self.app_sizey, scrollregion=(0,0,x,y))
#         self.canvas.grid(row=0, column=0, sticky="nsew")
#         self.canvas.create_line(self.border, self.border, self.border, y-self.border)
#         self.canvas.create_line(x-self.border, self.border, x-self.border, y-self.border)
#         self.canvas.create_line(self.border, self.border, x-self.border, self.border)
#         self.canvas.create_line(self.border, y-self.border, x-self.border, y-self.border)
#         self.cross_x = self.canvas.create_line(self.border, self.border, self.border, self.border)
#         self.cross_y = self.canvas.create_line(self.border, self.border, self.border, self.border)
#
#         #SCROLLING BARS
#         self.vbar=Scrollbar(self,orient=VERTICAL)
#         self.vbar.grid(row=0, column=1, sticky="ns")
#         self.vbar.config(command=self.canvas.yview)
#         self.hbar=Scrollbar(self,orient=HORIZONTAL)
#         self.hbar.grid(row=2, column=0, sticky="ew")
#         self.hbar.config(command=self.canvas.xview)
#         self.canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
#
#         #BUTTONS
#         self.buttonframe = Frame(self)
#         self.buttonframe.grid(row=1, column=0)
#         Button(self.buttonframe, text = "+", command=self.zoom_in).grid(row=0, column=0)
#         Button(self.buttonframe, text = "-").grid(row=0, column=1)
#
#
#         self.canvas.bind("<1>",     lambda event: self.canvas.focus_set())
#         self.canvas.bind("a",  lambda event: self.canvas.xview_scroll(-1, "units"))
#         self.canvas.bind("d", lambda event: self.canvas.xview_scroll( 1, "units"))
#         self.canvas.bind("w",    lambda event: self.canvas.yview_scroll(-1, "units"))
#         self.canvas.bind("s",  lambda event: self.canvas.yview_scroll( 1, "units"))
#         self.canvas.focus_set()
#
#     def zoom_in(self):
#         #Clean canvas
#         self.canvas.delete("all")
#         self.size_x = self.size_x * 1.1
#         self.size_y = self.size_y * 1.1
#         x=self.size_x
#         y=self.size_y
#         self.canvas.scrollregion=(0,0,self.size_x,self.size_y)
#         self.canvas.create_line(self.border, self.border, self.border, y-self.border)
#         self.canvas.create_line(x-self.border, self.border, x-self.border, y-self.border)
#         self.canvas.create_line(self.border, self.border, x-self.border, self.border)
#         self.canvas.create_line(self.border, y-self.border, x-self.border, y-self.border)
#
#         #SCROLLING BARS
#         self.vbar.config(command=self.canvas.yview)
#         self.hbar.config(command=self.canvas.xview)
#         self.canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
#
# graphics_window = Graphic(1000, 1000)
# graphics_window.mainloop()
