#Problema: Cálculo de bonificaciones para empleados de CodeMontt
print(" ")
print("----Calculo bonificación----")
print(" ")
#Ingreso de variables
nom = input("Ingrese su nombre: ")
antiguedad = int(input("Ingrese años de antiguedad del empleado (en años): "))

evaDes = input("Evaluación de desempeño empleado \nA)Buena \nB)Intermedia \nC)Mala \nIngrese su respuesta (Ej: a): ")
print(" ")
suelBase = 1000000

#Segun la antiguedad se realizara el calculo de bonificacion del empleado
#El codigo evaluara la antiguedad del empleado y evaluara en que parametro if, elif y else encajara, y dentro de cada funcion se anidan otras funciones if. elif y else, las cualles nos derivaran a los bonos correspondientes segun el desempeño del empleado.

if antiguedad >= 0 and antiguedad <= 2:
    if evaDes == "A":
        evaDes = suelBase*0.05
    elif evaDes == "B":
        evaDes = suelBase*0.03
    else:
        evaDes =suelBase*0.00

    print("Bonificación para el empleado", nom)
    print("Sueldo Base: ", suelBase)
    print(f"Bonificación:  {evaDes:.0f}")
    print(f"Sueldo total:  {suelBase+evaDes:.0f}")

elif antiguedad >= 2 and antiguedad <= 5:
    if evaDes == "A":
        evaDes = suelBase*0.08
    elif evaDes == "B":
        evaDes = suelBase*0.05
    else:
        evaDes = suelBase*0.02
    
    print("Bonificación para el empleado", nom)
    print("Sueldo Base: ", suelBase)
    print(f"Bonificación:  {evaDes:.0f}")
    print(f"Sueldo total:  {suelBase+evaDes:.0f}")

else:
    if evaDes == "A":
        evaDes = suelBase*0.12
    elif evaDes == "B":
        evaDes = suelBase*0.08
    else:
        evaDes = suelBase*0.05

    print("Bonificación para el empleado", nom)
    print("Sueldo Base: ", suelBase)
    print(f"Bonificación:  {evaDes:.0f}")
    print(f"Sueldo total:  {suelBase+evaDes:.0f}")



