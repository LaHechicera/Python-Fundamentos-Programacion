#valueError
#creando error a proposito

try:
    numero = int("asd") #
except:
    print("Error de valor valueError")
else:
    print("Si no hay error aparece el else")
finally:
    print("Esto se ejecuta si o si shavales")