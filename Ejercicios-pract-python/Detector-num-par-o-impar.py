#Detector número par o impar

num = input("Ingrese número: ")
num1 = int(num)

num1 = (num1%2)

if num1 > 0:
    print("Es un número impar")

else:
    print("Es un número par")