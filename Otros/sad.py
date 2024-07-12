
while True:
        nomC = input("Ingrese nombre del trabajador: ")
        if len(nomC) > 30:
            print ("Introduzca nombre valido con menos de 30 caracteres")
        elif len(nomC) == 0:
            print ("Nombre no debe quedar vacio")
        elif nomC.isalpha()
            print("Nombre Validado")

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

