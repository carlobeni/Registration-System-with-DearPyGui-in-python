from dearpygui import simple
from dearpygui.core import add_window

#from win32api import GetSystemMetrics

class DearPy_Window:
    def __init__(self,ID_win,label="",no_close=True,no_scroll=True,no_collapse=False):
        self.label=label
        self.ID_win=ID_win
        self.no_close=no_close
        self.no_scroll=no_scroll
        self.no_collapse=no_collapse

        x_to_full_screen=1080#GetSystemMetrics(0)
        y_to_full_screen=720#GetSystemMetrics(1)
        #Size
        self.width=int(x_to_full_screen/4)
        self.height=int(y_to_full_screen/3)
        #Position
        self.posX=int(x_to_full_screen/2-self.width/2)
        self.posY=int(y_to_full_screen/2-self.height/2)
    
    def my_space(self):
        add_window(name=self.ID_win,width=self.width,height=self.height,label=self.label,no_resize=True,no_close=self.no_close,no_scrollbar=self.no_scroll,no_collapse=self.no_collapse)
        simple.set_window_pos(window=self.ID_win,x=self.posX,y=self.posY)
    
    def set_label(self,label):
        self.label=label
        simple.set_item_label(self.ID_win,label)

    def show(self,view):
        if view==True: simple.show_item(self.ID_win)
        else: simple.hide_item(self.ID_win)

    def resize_for_input(self):
        self.height=int(self.width/2)

    def resize_for_out(self):
        self.height=int(self.width/50)

    def set_title(self,text):
        simple.set_item_label(self.ID_win,text)