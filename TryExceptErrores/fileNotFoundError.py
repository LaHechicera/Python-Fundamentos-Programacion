#cuando el archivo no existe o la ruta esta mal declarada

try:
    archivo = open("Archivo-que-no-existe","r")
except FileNotFoundError:
    print("Watafak bro no existe esa madre de archivo")