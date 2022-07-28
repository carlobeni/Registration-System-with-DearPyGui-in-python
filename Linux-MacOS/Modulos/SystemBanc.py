from Modulos.Clases.CuentaBancaria import CuentaBancaria
from Modulos.Clases.Pjuridica import Pjuridica
from Modulos.Layout import Layout
from Modulos.SystemCore import SystemCore

from Modulos.Clases.Persona import Persona

class SyetemBanc(Layout,SystemCore):
    def __init__(self,obj_p=Persona(),obj_pj=Pjuridica(),obj_cb=CuentaBancaria()):
        Layout.__init__(self)
        SystemCore.__init__(self,obj_p,obj_pj,obj_cb)

