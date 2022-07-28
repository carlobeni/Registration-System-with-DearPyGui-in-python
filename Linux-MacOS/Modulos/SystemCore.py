from Modulos.Clases.Persona import Persona
from Modulos.Clases.Pjuridica import Pjuridica
from Modulos.Clases.CuentaBancaria import CuentaBancaria

from datetime import datetime
class SystemCore:
    def __init__(self,obj_p,obj_pj,obj_cb):
        self.data_tp=[]
        self.date_tpj=[]
        self.date_tcb=[]
        self.taxs=[]

        self.obj_p=obj_p
        self.obj_pj=obj_pj
        self.obj_cb=obj_cb

    def set_at_in_obj(self,obj,text,ex=100):
        at = obj.__dict__.keys()
        for i,val in enumerate(at):
            #For numeric data
            if i==ex: continue
            if text[1][i]==0: obj.__setattr__(val,int(text[0][i]))
            else: obj.__setattr__(val,text[0][i])     
    
    def update_p(self,text):
        #Sets in object
        self.set_at_in_obj(self.obj_p,text)
        #Sets in tabla
        text[0].extend([self.obj_p.edad()])
        if self.obj_p.MayorEdad(): text[0].extend(["Si"])
        else: text[0].extend(["No"])
        self.data_tp=text[0]

    def update_pj(self,text):
        #Sets in object
        temp1=list(self.obj_p.__dict__.values())
        temp1.extend(text[0])
        temp2=[0,1,1,2]
        temp2.extend(text[1])
        temp2.extend([1,1])
        temp=[temp1,temp2]
        self.set_at_in_obj(self.obj_pj,temp)
        #Sets in tabla
        if self.obj_pj.iva: text[0][4]=self.obj_pj.calcular_iva()
        else: text[0][4]=0
        if self.obj_pj.irp: text[0][5]=self.obj_pj.calcular_irp()
        else: text[0][5]=0
        text[0].extend([self.obj_pj.dias_p_pagar()])

        self.data_tpj=text[0]

    def update_cb(self,text):
        #Sets in object
        self.set_at_in_obj(self.obj_cb,text,ex=1)
        self.obj_cb.set_propietario(self.obj_pj)
        #Sets in tabla
        self.data_tcb=text[0]
    
    #methods to validation
    def is_valid(self,val,type):
        if type==0: return self.is_only_numeric(val)
        elif type==1: return self.is_only_alphanumeric(val)
        elif type==2: return self.is_ok_date(val)
        else: return False

    def is_only_numeric(self,text):
        for i in range(len(text)):
            if ord(text[i])<48 or ord(text[i])>57 or text[0]=="0": return False
            if i==len(text)-1: return True

    def is_only_alphanumeric(self,text):
        if (text).isalpha(): return True
        return False

    def is_ok_date(self,strdate):
        try:
            date=datetime.strptime(strdate,Persona.date_format)
            return True
        except:
            return False
    
    #Other
    def get_text_and_type(self,list_inp_text,e=0):
        text=[[],[]]
        for i in range(len(list_inp_text)):
                text[0].extend([list_inp_text[i].get_text()])
                text[1].extend([list_inp_text[i].type_valid])
                if i==(len(list_inp_text)-e-1): break
        return text

    def is_ok_all_data(self,text):
        for i in range(len(text[0])):
            if self.is_valid(text[0][i],text[1][i])==False or text[0][i]=="" :
                return i  
            if i==len(text[0])-1:
                return 100
               