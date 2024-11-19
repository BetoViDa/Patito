import os
from interpretador import Interpreter

def main():
    print("Los archivos de prueba deben estar en la carpeta tests")
    file_name = input("Nombre del archivo sin extensión: ")

    try:
        file_path = f"{file_name}.txt"
        if not os.path.exists(file_path):
            raise FileNotFoundError("No se pudo leer el archivo")
        
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.read()
        
        interpreter = Interpreter(data)
        interpreter.execute()
    
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
