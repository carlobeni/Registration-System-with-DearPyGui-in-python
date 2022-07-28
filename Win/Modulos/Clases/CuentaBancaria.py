from Modulos.Clases.Pjuridica import Pjuridica

class CuentaBancaria:
    def __init__(self):
        self.id_banc=""
        self.propietario=Pjuridica()
        self.ahorros=0
        self.ingresos=0

    #Lo ahorrado se transfiere de los ingresos al ahorro
    def ahorrar(self,val):
        self.ahorros+=val
        self.ingresos-=val
    def extraer(self,val):
        self.ingresos-=val
    def cuenta_corriente(self):
        return (self.ingresos,self.ahorros)
    def deposito(self,val):
        self.ingresos+=val

    def set_id_banc(self,id_banc):self.id_banc=id_banc
    def get_id_banc(self): return self.id_banc

    def set_propietario(self,propietario):self.propietario=propietario
    def get_propietario(self): return self.propietario

    def set_ahorros(self,ahorros):self.ahorros=ahorros
    def get_ahorros(self): return self.ahorros

    def set_ingresos(self,ingresos):self.ingresos=ingresos
    def get_ingresos(self): return self.ingresos
