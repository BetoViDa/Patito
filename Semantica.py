class TablaVar:
    def __init__(self):  
        self.tabla = {}

    def get_tabla(self):
        return self.tabla

    def add_var(self, nombre, tipo,direccion):
        if not self.buscar_var(nombre):
            self.tabla[nombre] = {"nombre":nombre,"tipo":tipo,"direccion":direccion}
            return True
        else:
            raise ValueError(f"'{nombre}' Ya definido.")
        
    def add_constante(self,nombre,tipo,direccion):
        self.tabla[direccion] = {"nombre":nombre,"tipo":tipo,"direccion":direccion}

    def get_tipo(self,nombre):
        if self.buscar_var(nombre):
            return self.tabla[nombre]["tipo"]
        else:
            raise ValueError(f"Variable no definida", nombre)
    
    def get_direccion(self,nombre):
        if self.buscar_var(nombre):
            return self.tabla[nombre]["direccion"]
        else:
            direccion = self.encontrar_por_nombre(nombre)
            if direccion :
                return direccion["direccion"]
            else:
                raise ValueError("Error en get direccion",nombre)
            
    def encontrar_por_nombre(self,nombre):
        return next((item for item in self.tabla.values() if item["nombre"] == nombre), None)

    def editar_val_por_direccion(self,direccion,valor):
        val = next((item for item in self.tabla.values() if item["direccion"] == direccion), False)
        if val:
            self.tabla[val["nombre"]]["nombre"] = valor
        else:
            raise ValueError(f"Error en editar por direccion")
    
    def buscar_var(self, nombre):
        return nombre in self.tabla


class Dirfuncion:
    def __init__(self):  
        self.funciones = {}

    def get_dir(self):
        if self.funciones != {}:
            for func_nombre, func_info in self.funciones.items():
                tabla = func_info["tabla"].get_tabla()
                print(f"Funcion: {func_nombre}")
                print(f"Tipo: {func_info['tipo']}")
                print(
                    f"Variables: {tabla if tabla else 'Sin variables'}"
                )
            return True
        else:
            print("Sin funciones")



    def add_funcion(self, nombre, func_tipo):
        if not self.buscar_funcion(nombre):
            self.funciones[nombre] = {
                "nombre": nombre,
                "tipo": func_tipo,
                "tabla": TablaVar(),
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