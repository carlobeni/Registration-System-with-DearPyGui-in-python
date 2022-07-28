from Modulos.SystemBanc import SyetemBanc
#Obs:
#1- Antes de compilar App.py, instalar DearPyGUI con pip install dearpygui o pip3 install dearpygui en la consola de python
#2- SyetemBanc es hija de
        #>layout
        #>SystemCore>posee los atributos
            #>obj_p: Persona
            #>obj_pj: Pjuridica
            #>obj_cb: CuentaBancaria
        #layout
#3- En la consola se imprimiran los atributos de los objetos de tipo Persona, Pjuridica y CBancaria
#4- En programa solo permite cargar/editar datos de un cliente
#5- En programa puede tener errores en la GUI aun no subsanados por falta de tiempo
#6- Para usar en linux/mac 
#   6.1-Cambiar from win32api import GetSystemMetrics en las clases de window
#   6.2-Cambiar "cls" por "clear" en la linea 177 de Layout.py

app =  SyetemBanc()
if __name__ == "__main__":
    app.init_all_layouts()

def priting():
    print("-------------Update-------------")
    print("Persona:\n",app.obj_p.__dict__)
    print("Persona Juridica:\n",app.obj_pj.__dict__)
    print("Cuenta Bancaria:\n",app.obj_cb.__dict__)


#Debido a problemas de importacion circular tuve que programar el gestor de eventos onClick
#directamente aqui, y no en una clase como System Core o"""
def onClick(sender,data):
        #Save/Edition (Terminado)
        if sender=="btn_load>table_p" or sender=="btn_load>table_pj" or sender=="btn_load>table_b": data.show(True)

        #To Aumentar ingreos, ahorrar, extraer, deposito(Terminado)
        elif sender=="btn_plus_money" or sender=="btn_aho" or sender=="btn_ex" or sender=="btn_de": 
            data.show(True) 

        #To total a pagar(Terminado)
        elif sender=="btn_tot_pag":
            win=data
            print(str(app.obj_pj.get_total_pagar()))
            win.set_title("El total a pagar es: "+str(app.obj_pj.get_total_pagar()))
            win.show(True)

        #Inputs (Aumentar Ingresos)
        elif sender=="btn_save_ib_ag":
            [win,table,inp_load,msg]=data
            text=inp_load.get_text()
            if app.is_only_numeric(text) or text=="":
                msg.set_text("")
                #Update dates
                #Object
                if app.is_only_numeric(text): app.obj_pj.aumentar_ingreso(int(text))
                else: app.obj_pj.aumentar_ingreso()
                #Table
                app.data_tpj[3]=app.obj_pj.get_ingresos()
                if app.obj_pj.iva: app.data_tpj[4]=app.obj_pj.calcular_iva()
                else: app.data_tpj[4]=0
                if app.obj_pj.irp: app.data_tpj[5]=app.obj_pj.calcular_irp()
                else: app.data_tpj[5]=0
                app.data_tpj[6]=app.obj_pj.dias_p_pagar()
                table.load_new_row(app.data_tpj)

                win.show(False)
            else: 
                msg.set_text("Error de carga en el parametro "+str(inp_load.title)+"\nSi deja el campo en blanco \nse aumentara un ingreso\nequivalente a un salario minimo")
        
        elif sender=="btn_save_ib_ah" or sender=="btn_save_ib_ex" or sender=="btn_save_ib_de":
            [win,table,inp_load,msg]=data
            text=inp_load.get_text()
            if app.is_only_numeric(text):
                msg.set_text("")
                #Update dates
                #Object
                if sender=="btn_save_ib_ah": app.obj_cb.ahorrar(int(text))
                elif sender=="btn_save_ib_ex": app.obj_cb.extraer(int(text))
                else: app.obj_cb.deposito(int(text))
                #Table
                app.data_tcb[2]=app.obj_cb.get_ahorros()
                app.data_tcb[3]=app.obj_cb.get_ingresos()
                table.load_new_row(app.data_tcb)
                win.show(False)
            else: 
                msg.set_text("Error de carga en el parametro "+str(inp_load.title))

        #Save to windows (Terminado)
        elif sender=="btn_save_p" or sender=="btn_save_pj" or sender=="btn_save_b":
                [win,table,list_inp_text,msg,next_table]=data[0:5]
                if sender=="btn_save_pj": 
                    text=app.get_text_and_type(list_inp_text,2)
                else: text=app.get_text_and_type(list_inp_text)
                #text[0]: text
                #text[1]: type valid
                eval=app.is_ok_all_data(text)
                if eval==100:
                    msg.set_text("")
                    if sender=="btn_save_p": 
                        app.update_p(text)
                    elif sender=="btn_save_pj": 
                        text[0].extend([list_inp_text[4].get_state()])
                        text[0].extend([list_inp_text[5].get_state()])
                        app.update_pj(text)
                        data[6].set_text(app.obj_pj.nombre)
                    else:
                        app.update_cb(text)
                    table.load_new_row(text[0])
                    win.show(False)
                    next_table.show(True)
                    if sender=="btn_save_pj" or sender=="btn_save_b":
                        gbtn=data[5]
                        for i in gbtn: i.show(True)
                else:
                    msg.set_text("Error de carga en el parametro \n"+list_inp_text[eval].title)
        priting()