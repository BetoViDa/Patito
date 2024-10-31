import sys
from antlr4 import *
from PatitoLexer import PatitoLexer
from PatitoParserParser import PatitoParserParser
from Semantica import Dirfuncion

def main(input_file):
    # Leer el archivo de entrada
    with open(input_file, 'r') as file:
        input_data = file.read()

    # Crear un lexer y un parser
    input_stream = InputStream(input_data)
    lexer = PatitoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PatitoParserParser(stream)
    
    funciones = Dirfuncion()
    parser.funcdir = funciones
    
    # Parsear la entrada según la regla 'programa'
    tree = parser.programa()
    
  

    # Imprimir el árbol de parseo
    print("Árbol de parseo:")
    print(tree.toStringTree(recog=parser))
    funciones.get_dir()
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python parse_file.py <archivo_entrada>")
    else:
        main(sys.argv[1])