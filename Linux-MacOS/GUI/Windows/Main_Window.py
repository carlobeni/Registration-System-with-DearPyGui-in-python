from dearpygui.core import *
from dearpygui.simple import *

#from win32api import GetSystemMetrics

class Main_Window:
    def __init__(self,ID_main_win="Main Window",title="Window"):
        self.title=title
        self.ID_main_win=ID_main_win
        self.width_to_full_screen=1080#GetSystemMetrics(0)
        self.height_to_full_screen=720#GetSystemMetrics(1)-100
        set_main_window_title(title)
        set_main_window_size(width=self.width_to_full_screen,height=self.height_to_full_screen)
        self.set_default_setting()

    def my_space(self):
        add_window(name=self.ID_main_win)

    def set_default_setting(self):
        set_theme("Cherry")
        set_style_window_padding(30,30)

    def start(self,ID_window=""):
        set_main_window_pos(0,0)   
        start_dearpygui(primary_window=ID_window) 