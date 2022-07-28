from dearpygui.core import add_spacing

from GUI.Widgets import *
from GUI.Windows.Main_Window import Main_Window
from GUI.Windows.DearPy_Window import DearPy_Window
import os

class Layout:
        def __init__(self):
                #Ventanas 
                self.main_window=Main_Window(title="Sistema Bancario")
                self.win_edit_p=DearPy_Window(ID_win="Win_edit_p",label="Editar Datos Personales")
                self.win_edit_pj=DearPy_Window(ID_win="Win_edit_pj",label="Editar Datos Juridicos")
                self.win_edit_b=DearPy_Window(ID_win="Win_edit_b",label="Editar Datos Bancarios")
                #Windows to input
                self.win_inp_box_ag=DearPy_Window(ID_win="Win_inp_box_ag",label="Ingrese un monto: ")
                self.win_inp_box_ag.resize_for_input()

                self.win_inp_box_ah=DearPy_Window(ID_win="Win_inp_box_ah",label="Ingrese un monto: ")
                self.win_inp_box_ah.resize_for_input()

                self.win_inp_box_ex=DearPy_Window(ID_win="Win_inp_box_ex",label="Ingrese un monto: ")
                self.win_inp_box_ex.resize_for_input()

                self.win_inp_box_de=DearPy_Window(ID_win="Win_inp_box_de",label="Ingrese un monto: ")
                self.win_inp_box_de.resize_for_input()

                #Window to output
                self.win_out=DearPy_Window(ID_win="Win_out",label="",no_close=False)
                self.win_out.resize_for_out()
                self.tip_valid=[
                        "Debe ser un numero entero \ny no puede comenzar con 0",
                        "Debe cargar unicamente letras, \nsin espacios y caracteres especiales",
                        "Debe tener el formato aaaa-mm-dd"]
                self.titles_win_p=[
                        "DNI:                ",
                        "Nombre:             ",
                        "Apellido:           ",
                        "Fecha de nacimiento:"]
                self.titles_win_pj=[
                        "RUC:           ",
                        "Empresa:       ",
                        "Fecha de Pago: ",
                        "Ingresos:      ",
                        "IVA (5%): ",
                        "IRP (10%): "]
                self.titles_win_b=[
                        "ID Bancario:  ",
                        "Propietario:  ",
                        "Ahorros:      ",
                        "Ingresos:     ",]
                self.tip_button="Recuerde cargar primeramente\nlos datos en la tabla y guardar\nlos cambios en caso de algun cambio"
                self.tip_sm="Si deja el campo en blanco \nse aumentara un ingreso\nequivalente a un salario minimo"
                self.tab_p=[]
                self.tab_pj=[]
                self.tab_b=[]
                self.gbtn_pj=[]
                self.gbtn_cb=[]

        def init_hide_start(self):
                self.tab_b.show(False)
                self.tab_pj.show(False)
                for i in self.gbtn_pj: i.show(False)
                self.tab_b.show(False)
                for i in self.gbtn_cb: i.show(False)
                self.win_edit_p.show(False)
                self.win_edit_pj.show(False)
                self.win_edit_b.show(False)
                self.win_out.show(False)
                self.win_inp_box_ag.show(False)
                self.win_inp_box_ah.show(False)
                self.win_inp_box_ex.show(False)
                self.win_inp_box_de.show(False)

        def init_layout_to_mwin(self):
                self.main_window.my_space()

                #Tables>Persona
                titles_tab_p=self.titles_win_p
                titles_tab_p.extend(["Edad","Mayor de Edad"])
                self.tab_p=Table("table_p","Datos personales del cliente",titles_tab_p,self.win_edit_p)

                #Tables>Persona Juridica
                titles_tab_pj=self.titles_win_pj
                titles_tab_pj.extend(["Dias faltantes \npara el pago"])
                self.tab_pj=Table("table_pj","Datos juridicos del cliente",titles_tab_pj,self.win_edit_pj)
                add_same_line()
                self.gbtn_pj.extend([Button("btn_plus_money","Aumentar ingresos",self.win_inp_box_ag,self.tip_button)])
                add_same_line()
                self.gbtn_pj.extend([Button("btn_tot_pag","Total a pagar",self.win_out,self.tip_button)])

                #Tables>Cuenta Bancaria
                self.tab_b=Table("table_b","Datos bancarios del cliente",self.titles_win_b,self.win_edit_b)
                add_same_line()
                self.gbtn_cb.extend([Button("btn_aho","Ahorrar",self.win_inp_box_ah,self.tip_button)])
                add_same_line()
                self.gbtn_cb.extend([Button("btn_ex","Extraer",self.win_inp_box_ex,self.tip_button)])
                add_same_line()
                self.gbtn_cb.extend([Button("btn_de","Deposito",self.win_inp_box_de,self.tip_button)])

        def init_layout_to_dwins(self):
                #Ventana de cargas
                self.win_inp_box_ag.my_space()
                load_ib_ag=Input_Text("##inp_ib_ag","Valor:    ",int(self.win_inp_box_ag.width/2),[self.tip_valid[0],0])
                add_spacing(count=10)
                msg_ib_ag=Text("msg_edit_ib_ag","",[255,0,0])
                add_spacing(count=3)
                btn_save_ib_ag=Button("btn_save_ib_ag","Cargar",[self.win_inp_box_ag,self.tab_pj,load_ib_ag,msg_ib_ag],self.tip_sm)

                self.win_inp_box_ah.my_space()
                load_ib_ah=Input_Text("##inp_ah","Valor:    ",int(self.win_inp_box_ah.width/2),[self.tip_valid[0],0])
                add_spacing(count=10)
                msg_ib_ah=Text("msg_edit_ah","",[255,0,0])
                add_spacing(count=3)
                btn_save_ib_ah=Button("btn_save_ib_ah","Cargar",[self.win_inp_box_ah,self.tab_b,load_ib_ah,msg_ib_ah])

                self.win_inp_box_ex.my_space()
                load_ib_ex=Input_Text("##inp_ib_ex","Valor:    ",int(self.win_inp_box_ex.width/2),[self.tip_valid[0],0])
                add_spacing(count=10)
                msg_ib_ex=Text("msg_edit_ib_ex","",[255,0,0])
                add_spacing(count=3)
                btn_save_ib_ex=Button("btn_save_ib_ex","Cargar",[self.win_inp_box_ex,self.tab_b,load_ib_ex,msg_ib_ex])

                self.win_inp_box_de.my_space()
                load_ib_de=Input_Text("##inp_ib_de","Valor:    ",int(self.win_inp_box_de.width/2),[self.tip_valid[0],0])
                add_spacing(count=10)
                msg_ib_de=Text("msg_edit_ib_de","",[255,0,0])
                add_spacing(count=3)
                btn_save_ib_de=Button("btn_save_ib_de","Cargar",[self.win_inp_box_de,self.tab_b,load_ib_de,msg_ib_de])

                #Ventana de mensajes
                self.win_out.my_space()

                #Ventana de Edicion de Persona
                self.win_edit_p.my_space()
                loads_p=[
                        Input_Text("##inp_p1",self.titles_win_p[0],int(self.win_edit_p.width/3),[self.tip_valid[0],0]),
                        Input_Text("##inp_p2",self.titles_win_p[1],int(self.win_edit_p.width/3),[self.tip_valid[1],1]),
                        Input_Text("##inp_p3",self.titles_win_p[2],int(self.win_edit_p.width/3),[self.tip_valid[1],1]),
                        Input_Text("##inp_p4",self.titles_win_p[3],int(self.win_edit_p.width/3),[self.tip_valid[2],2])]
                add_spacing(count=10)
                msg_p=Text("msg_edit_p","",[255,0,0])
                add_spacing(count=10)
                btn_save_p=Button("btn_save_p","Guardar",[self.win_edit_p,self.tab_p,loads_p,msg_p,self.tab_pj])

                #Ventana de Edicion de Cuenta Bancaria
                self.win_edit_b.my_space()
                loads_b=[
                        Input_Text("##inp_b1",self.titles_win_b[0],int(self.win_edit_pj.width/3),[self.tip_valid[0],0]),
                        Input_Text("##inp_b2",self.titles_win_b[1],int(self.win_edit_pj.width/3),[self.tip_valid[1],1],enabled=False),
                        Input_Text("##inp_b3",self.titles_win_b[2],int(self.win_edit_pj.width/3),[self.tip_valid[0],0]),
                        Input_Text("##inp_b4",self.titles_win_b[3],int(self.win_edit_pj.width/3),[self.tip_valid[0],0])]
                add_spacing(count=10)
                msg_b=Text("msg_edit_b","",[255,0,0])
                add_spacing(count=10)
                btn_save_b=Button("btn_save_b","Guardar",[self.win_edit_b,self.tab_b,loads_b,msg_b,self.tab_b,self.gbtn_cb])

                #Ventana de Edicion de Persona Juridica
                self.win_edit_pj.my_space()
                loads_pj=[
                        Input_Text("##inp_pj1",self.titles_win_pj[0],int(self.win_edit_pj.width/3),[self.tip_valid[0],0]),
                        Input_Text("##inp_pj2",self.titles_win_pj[1],int(self.win_edit_pj.width/3),[self.tip_valid[1],1]),
                        Input_Text("##inp_pj3",self.titles_win_pj[2],int(self.win_edit_pj.width/3),[self.tip_valid[2],2]),
                        Input_Text("##inp_pj4",self.titles_win_pj[3],int(self.win_edit_pj.width/3),[self.tip_valid[0],0]),
                        CheckBox("##cb_pj1",self.titles_win_pj[4]),
                        CheckBox("##cb_pj2",self.titles_win_pj[5])
                ]
                add_spacing(count=10)
                msg_pj=Text("msg_edit_pj","",[255,0,0])
                add_spacing(count=10)
                btn_save_pj=Button("btn_save_pj","Guardar",[self.win_edit_pj,self.tab_pj,loads_pj,msg_pj,self.tab_b,self.gbtn_pj,loads_b[1]])

        def init_all_layouts(self):
                self.init_layout_to_mwin()
                self.init_layout_to_dwins()
                self.init_hide_start()
                os.system("clear")
                print("Program is runnig...")
                self.main_window.start(self.main_window.ID_main_win)