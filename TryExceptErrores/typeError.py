#cando tipo de dato no es compatible

try: 
    resultado = 5 + "10"
except TypeError:
    print("son diferentes datos, no compatibilizan me cachai")