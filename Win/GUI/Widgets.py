from dearpygui.core import *
from dearpygui.simple import show_item,hide_item

class Table:
    def __init__(self,ID_table,title,list,edit_win):
        self.ID_table=ID_table
        self.list=list
        self.title=title
        self.edit_win=edit_win
        add_spacing(count=10)
        add_text(self.title)
        add_table(self.ID_table,self.list)
        add_spacing(count=10)
        self.btn_load=Button("btn_load>"+self.ID_table,"Cargar/Editar",self.edit_win)

    def load_new_row(self,list_text):
        tabledata = []
        for i in range(0, 1):
            row = []
            for j in range(0, len(list_text)):
                row.append(list_text[j])
            tabledata.append(row)
        set_table_data(self.ID_table, tabledata)

    def show(self,view):
        self.btn_load.show(view)
        if view==True: 
            show_item(self.ID_table)
            show_item(self.title)
        else: 
            hide_item(self.ID_table)
            hide_item(self.title)

class Text:
    def __init__(self,ID_Text,text,color):
        self.ID_Text=ID_Text
        self.color=color
        self.text=text
        add_text(name=self.ID_Text,default_value=self.text,color=self.color)
        set_value(name=self.ID_Text,value=self.text)
    
    def set_text(self,text):
        set_value(name=self.ID_Text,value=text)
        self.text=text

class Input_Text:
    def __init__(self,ID_inText,title,width,valid,default_value="",enabled=True):
        self.ID_inText=ID_inText
        self.title=title
        self.default_value=default_value
        self.tip_valid=valid[0]
        self.type_valid=valid[1]
        self.width=width
        self.enabled=enabled
        add_text(title)
        add_same_line()
        add_input_text(name=self.ID_inText,width=self.width,default_value="",tip=self.tip_valid,enabled=self.enabled)

    def get_text(self):
        return get_value(self.ID_inText)

    def set_text(self,text):
        set_value(self.ID_inText,text)

class Button:
    def __init__(self,ID_button,label,context,tip=""):
        self.context=context
        self.ID_button=ID_button
        self.label=label
        self.tip=tip
        from App import onClick
        add_button(name=self.ID_button,label=self.label,callback=onClick,callback_data=self.context,tip=self.tip)

    def show(self,view):
        if view==True: 
            show_item(self.ID_button)
        else: 
            hide_item(self.ID_button)

class CheckBox:
    def __init__(self,ID_check,title):
        self.ID_check=ID_check
        self.title=title
        add_text(title)
        add_same_line()
        add_checkbox(name=self.ID_check) 

    def get_state(self):
        return get_value(self.ID_check)