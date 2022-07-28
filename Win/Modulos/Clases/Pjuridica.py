from datetime import datetime
from Modulos.Clases.Persona import Persona

class Pjuridica(Persona):
    def __init__(self):
        super().__init__()
        self.ruc=""
        self.empresa=""
        self.fecha_pago=""
        self.ingresos=0
        self.iva=False
        self.irp=False

    def calcular_iva(self):
        return self.ingresos*0.05
    def calcular_irp(self):
        return self.ingresos*0.10
    def dias_p_pagar(self):
        return (datetime.strptime(self.fecha_pago,Persona().date_format)-datetime.now()).days+1
    def get_total_pagar(self):
        return (57/400)*self.ingresos
    def aumentar_ingreso(self,val=2192839):
        if val=="2192839": self.ingresos+=2192839
        else: self.ingresos+=val
    
    def set_ruc(self,ruc):self.ruc=ruc
    def get_ruc(self): return self.ruc

    def set_empresa(self,empresa):self.empresa=empresa
    def get_empresa(self): return self.empresa

    def set_iva(self,iva):self.iva=iva
    def get_iva(self): return self.iva

    def set_irp(self,irp):self.irp=irp
    def get_irp(self): return self.irp

    def set_fecha_pago(self,fecha_pago):self.fecha_pago=fecha_pago
    def get_fecha_pago(self): return self.fecha_pago

    def set_ingresos(self,ingresos):self.ingresos=ingresos
    def get_ingresos(self): return self.ingresos
