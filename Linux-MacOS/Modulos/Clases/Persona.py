from datetime import datetime

class Persona:
    def __init__(self):
        self.dni=0
        self.nombre="name"
        self.apellido="last name"
        self.fecha_nacimiento="dd-mm-aaaa"
    
    date_format='%d-%m-%Y'

    def edad(self):
        date_bir=datetime.strptime(self.fecha_nacimiento,self.date_format)
        #Si el mes y dia de nacimiento es mayor al mes y dia actual entonces
        #la persona aun es joven y is_young=1 caso contrario is_young=0
        #Obs: en la comparacion de tuplas, al usar < o > si las componentes 
        #correspondientes son iguales la comparacion continua con el sigueinte par de
        #elementos, pero si todos los pares de elementos son iguales el resultado es False
        is_young=(datetime.now().month,datetime.now().day)<(date_bir.month,date_bir.day)
        return (datetime.now().year-date_bir.year)-is_young

    def MayorEdad(self):
        if(self.edad()>17): return True
        return False

    def set_dni(self,dni): self.dni=dni
    def get_dni(self): return self.dni

    def set_nombre(self,nombre): self.nombre=nombre
    def get_nombre(self): return self.nombre
    def set_apellido(self,apellido): self.apellido=apellido
    def get_apellido(self): return self.apellido

    def set_fecha_nacimiento(self,fecha_nacimiento): self.fecha_nacimiento=fecha_nacimiento
    def get_fecha_nacimiento(self): return self.fecha_nacimiento