import json

enterocontg= 1000
flotantecontg = 3000

enteroconttemp = 5000
flotanteconttemp = 7500

constanteintcont = 15000
constanteflotcont = 20000
constanteletcont = 25000

class TablaVar:
    def __init__(self):  
        self.tabla = {}

    def get_tabla(self):
        return self.tabla

    def add_var(self, nombre, tipo):
        if not self.buscar_var(nombre):
            if tipo == "entero":
                if enterocontg < 3000 :
                    add = enterocontg + 1
                else : 
                    raise ValueError("Limite de memoria alcanzado para : ", tipo ,".")
            elif tipo == "flotante":
                if flotantecontg < 5000:
                    add = flotantecontg + 1
                else:
                    raise ValueError("Limite de memoria alcanzado para : ", tipo ,".")
            else:
                raise ValueError(f"Tipo de variable inexistente.")
            
            self.tabla[nombre] = {"nombre":nombre,"tipo":tipo,"direccion":add}
            return True
        else:
            raise ValueError(f"'{nombre}' Ya definido.")
        
    def add_temp(self,nombre,tipo):
        if tipo == "entero":
            if enteroconttemp < 7500 :
                add = enteroconttemp + 1
            else : 
                raise ValueError("Limite de memoria alcanzado para : ", tipo ,".")
        elif tipo == "flotante":
            if flotanteconttemp < 10000:
                add = flotanteconttemp + 1
            else:
                raise ValueError("Limite de memoria alcanzado para : ", tipo ,".")
        else:
            raise ValueError(f"Tipo de variable inexistente.")
        
        self.tabla[nombre] = {"nombre":nombre,"tipo":tipo,"direccion":add}
        return True
    
    def get_tipo(self,nombre):
        if(self.buscar_var(nombre)):
            return self.tabla[nombre]["tipo"]
        else:
            raise ValueError("Variable no definida")
    
    def get_dir(self,nombre):
        if self.buscar_var(nombre):
            return self.tabla[nombre]["direccion"]
        else:
            add = self.encontrar_por_nombre(nombre)
            if add != None:
                return add.direccion
            else:
                raise ValueError("Error get_dir")
            
    def editar_tipo(self,nombre,tipo):
        if self.buscar_var(nombre):
            self.tabla[nombre]["tipo"] = tipo
            return True
        else:
            raise ValueError(f"Variable ",nombre," no definido.")
        
    def editar_llave(self,llave,nueva):
        if self.buscar_var(llave):
            val = self.tabla[llave]
            val["nombre"] = nueva
            self.tabla[nueva]=val
            del self.tabla[llave]
        else:
            raise ValueError("Error en editar_llave")
            
    
    def buscar_var(self, nombre):
        return nombre in self.tabla


class TablaConstante:
    def __init__(self):  
        self.tabla = {}

    def get_tabla(self):
        return self.tabla

    def add_const(self, nombre, tipo):
        if not self.buscar_const(nombre):
            if tipo == "entero":
                if constanteintcont < 20000 :
                    add = constanteintcont + 1
                else : 
                    raise ValueError("Limite de memoria alcanzado para : ", tipo ,".")
            elif tipo == "flotante":
                if constanteflotcont < 25000:
                    add = constanteflotcont + 1
                else:
                    raise ValueError("Limite de memoria alcanzado para : ", tipo ,".")
            elif tipo == "letrero":
                if constanteletcont < 30000:
                    add = constanteletcont + 1
                else:
                    raise ValueError("Limite de memoria alcanzado para : ", tipo ,".")
            else:
                raise ValueError(f"Tipo de variable inexistente.")
            
            self.tabla[nombre] = {"nombre":nombre,"tipo":tipo,"direccion":add}
            return True
        else:
            raise ValueError(f"'{nombre}' Ya definido.")
        
    def add_string_const(self,nombre):
        if not self.buscar_const(nombre):
            if constanteletcont < 30000:
                add = constanteletcont + 1
            else:
                raise ValueError("Limite de memoria alcanzado para constante letrero")
            self.tabla[nombre] = {"nombre": nombre,"tipo": "letrero","direccion": add}
            return add
        else:
            return self.get_dir(nombre)
    
    def get_tipo(self,nombre):
        if(self.buscar_const(nombre)):
            return self.tabla[nombre]["tipo"]
        else:
            raise ValueError("Variable no definida")
    
    def get_dir(self,nombre):
        if self.buscar_const(nombre):
            return self.tabla[nombre]["direccion"]
        else:
            add = self.get_const_por_nombre(nombre)
            if add != None:
                return add["direccion"]
            else:
                raise ValueError("Error get_dir")
            
    def get_const_por_nombre(self,nombre):
        if nombre in self.tabla:
            return self.tabla[nombre]
        else:
            raise ValueError("Constante ", nombre, " no definida")
        
    def editar_val_por_nombre(self,nombre,nuevo):
        if nombre in self.tabla:
            val = self.tabla[nombre]
            val["nombre"] = nuevo
            self.tabla[nuevo] = val
            del self.tabla[nombre]
        else:
            raise ValueError("Error en editar_val_por_nombre")
            
    
    def buscar_const(self, nombre):
        return nombre in self.tabla

class Dirfuncion:
    def __init__(self):  
        self.funciones = {}

    def get_dir(self):
        for nombre in self.funciones:
            if nombre in self.funciones:
                tabla_var = self.funciones[nombre]["tabla_var"].get_tabla()
                constante_tabla = self.funciones[nombre]["constante_tabla"].get_tabla()
                print(f"funcion: {nombre}")
                print(f"tipo: {self.funciones[nombre]["tipo"]}")
                print(
                    f"variables: {json.dumps(tabla_var) if len(tabla_var) != 0 else 'Sin variables'}"
                )
                print(
                    f"constantes: {json.dumps(constante_tabla) if len(constante_tabla) != 0 else 'Sin constantes'}"
                )
        return True
    
    def get_dir_por_nombre(self,nombre):
        if self.buscar_funcion(nombre):
            tabla_var = self.funciones[nombre]["tabla_var"].get_tabla()
            constante_tabla = self.funciones[nombre]["constante_tabla"].get_tabla()
            print(f"funcion: {nombre}")
            print(f"tipo: {self.funciones[nombre]["tipo"]}")
            print(
                f"variables: {json.dumps(tabla_var) if len(tabla_var) != 0 else 'Sin variables'}"
            )
            print(
                f"constantes: {json.dumps(constante_tabla) if len(constante_tabla) != 0 else 'Sin constantes'}"
            )
        return True

    def add_funcion(self, nombre, func_tipo):
        if not self.buscar_funcion(nombre):
            self.funciones[nombre] = {
                "nombre": nombre,
                "tipo": func_tipo,
                "tabla_var": TablaVar(),
                "constante_tabla": TablaConstante(),
            }
            return True
        else:
            raise ValueError(f"'{nombre}' Ya definido.")

    def buscar_funcion(self, nombre):
        return nombre in self.funciones
    
    def editarVal_nombre(self,llave,valor):
        if self.tabla.buscar_var(llave):
            self.tabla[llave] = valor
        else:
            raise ValueError("Error de Actualizacion")
