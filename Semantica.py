class TablaVar:
    def __init__(self):  
        self.tabla = {}

    def get_tabla(self):
        return self.tabla

    def add_var(self, nombre, tipo):
        if not self.buscar_var(nombre):
            self.tabla[nombre] = tipo
            return True
        else:
            raise ValueError(f"'{nombre}' Ya definido.")

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
