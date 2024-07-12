
print ("----Calculadora promedio de 3 notas----")
nota1 = float(input("Ingrese primera nota: "))
nota2 = float(input("Ingrese segunda nota: "))
nota3 = float(input("Ingrese tercera nota: "))

result= round(((nota1+nota2+nota3)/3),2)

if result >= 4.0:
    print("Aprobado")
else:
    print("Reprobado")