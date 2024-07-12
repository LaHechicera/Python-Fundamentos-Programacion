
##Ingreso datos del trabajador

print(" ")
print("-----Calculo de Liquidacion de Sueldo-----")
print(" ")


while True:
    try:
        nomC = input("Ingrese nombre del trabajador: ")
        if len(nomC) > 30:
            print ("Introduzca nombre valido con menos de 30 caracteres")
        elif len(nomC) == 0:
            print ("Nombre no debe quedar vacio")
        else:
            break
    except TypeError:
        print("Ingrese un nombre valido")


sueldoBase = -1

while sueldoBase < 0:
    try:
        sueldoBase = int(input("Ingrese sueldo base del trabajador: "))
        if sueldoBase < 0:
            print("Numero no valido")
        else:
            break
    except ValueError:
        print("Ingrese un numero valido")
        
horasExtra = -1

while horasExtra < 0:
    try:
        horasExtra = float(input("Ingrese horas extra de trabajador: "))
        if horasExtra < 0:
            print("Numero no valido")
        else:
            break
    except ValueError:
        print("Ingrese un numero valido")
    


##Calculo de Liquidación

horaNormal = float(f"{sueldoBase / 180:.0f}")
horaExtra = ((horaNormal*100)/50)
fonasa = sueldoBase*0.07
afp = sueldoBase*0.10
sueldoBase2 = sueldoBase-afp-fonasa

if horasExtra <= 180:
    sueldoBase
else:
    horasExtra > 180
    sueldoBase3 = sueldoBase + (horasExtra-180)+horaExtra

if horasExtra > 180:
    horEx1 = (horasExtra-180)+horaExtra
else:
    horEx1 = 0

total = sueldoBase2

##Liquidacion

print(" ")
print("-----Desglose Liquidacion de Sueldo-----")
print(" ")
print(f"\nNombre del trabajador: {nomC}")
print(f"\nSueldo Base trabajador: {sueldoBase:.0f}")
print(f"\nTotal horas extras a pagar: {horEx1:.0f}")
print(f"\nTotal de ingresos sin descuentoss: {sueldoBase:.0f}")
print(f"\nDescuento por Fonasa 7%: {fonasa:.0f}")
print(f"\nDescuento por AFP 10%: {afp:.0f}")
print(f"\nSueldo neto a pagar: {total:.0f}")


import datetime
fechaHora = datetime.datetime.now()

with open(f'Liquidacion_{nomC}.txt', 'w') as archivo:
    archivo.write("\n-----Liquidacion de Sueldo-----")
    archivo.write("\n ")
    archivo.write(f"\nFecha y hora actual: {fechaHora}")
    archivo.write("\n ")
    archivo.write(f"\nNombre del trabajador: {nomC}")
    archivo.write(f"\nSueldo Base trabajador: {sueldoBase:.0f}")
    archivo.write(f"\nTotal horas extras a pagar: {horEx1:.0f}")
    archivo.write(f"\nTotal de ingresos sin descuentoss: {sueldoBase:.0f}")
    archivo.write(f"\nDescuento por Fonasa 7%: {fonasa:.0f}")
    archivo.write(f"\nDescuento por AFP 10%: {afp:.0f}")
    archivo.write(f"\nSueldo neto a pagar: {total:.0f}")

print ("Se ha creado un archivo con el resumen de liquidacion de sueldo")
