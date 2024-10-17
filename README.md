# Parcial2_PR3
Actividad en clase


#Codigo 1

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control1179")

print(" ")

#Creacion de diccionario con las divisas

diccionario = {

    'Euro': '€',
    
    'Dollar': '$',
    
    'Yen': '¥'
}

#Pide al usuario que ingrese la divisa 

DIVISA = str(input("Ingrese una divisa: "))

#Verifcara o no que la divisa esta dentro del diccionario y mostrara el simbolo

if DIVISA in diccionario:

    print (diccionario[DIVISA])
    
else:

    print ("Ingresa una valida")
    
    print("")

  ![image](https://github.com/user-attachments/assets/4c9e45d2-6039-49c6-9530-c6398ceebfa4)
  ![image](https://github.com/user-attachments/assets/b245f504-42c8-4e4c-888e-f6cc1f1b73bb)

  #Codigo 2

  print(" ")
  
print("Dylan Aaron Elicserio Martínez 3°W #Control1179")

print(" ")

Nombre = input("Ingresa tu nombre:")

Edad = input("Ingresa tu edad:")

Direccion = input("Ingresa tu direccion(País):")

Telefono = input("Ingresa tu nomero de telefono:")

diccionario = {

    "nombre" : Nombre,
    
    "edad" : Edad,
    
    "dicc" : Direccion,
    
    "tel" : Telefono
    
}

print(" ")

print("usted se llama:")

print(diccionario["nombre"])

print("su edad es:")

print(diccionario["edad"])

print("su direccion o localizacion actual es:")

print(diccionario["dicc"])

print("su numero de telefono es:")

print(diccionario["tel"])

print("Muchas gracias por confiar en nosotros digo en mi para ingresar tu informacion personal hasta luego")

![image](https://github.com/user-attachments/assets/2b9412cb-43fc-4e9a-89c0-07b3dd4de65a)
![image](https://github.com/user-attachments/assets/caac5542-d7ab-43e1-952d-b5cdb06e7219)

#Codigo 3

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control1179")

print(" ")

#Creacion de diccionario

precio_frutas = {

    'Melon': 5.6,
    
    'Sandia': 4.4,
    
    'Platano': 3.2,
    
    'Pera': 1.4,
    
    'Mango': 1.2
    
}

#Pedira la introduccion de la fruta y cuanto va a llevar

frutas = input("Ingrese la fruta de su seleccion: ")

print("")

kilos = float(input("Ingrese la cantidad de kilos que quiere comprar: "))

print("")

#Imprimira si la fruta esta y cuanto dinero sera, en caso de no estar imprimira un mensaje avisando

if frutas in precio_frutas:

    precio_final = precio_frutas[frutas] * kilos

    print(f"{kilos} kilos de {frutas} serán: {precio_final:.2f} de dinero")
    
    print("")
    
    print (precio_frutas[frutas])

else:

    print ("No tenemos esa fruta")
    
    print("")

![image](https://github.com/user-attachments/assets/41d344a7-24cd-4c6e-9313-de28f53ebef2)
![image](https://github.com/user-attachments/assets/d0085016-d96e-4846-ba75-7dd9e08b070c)


