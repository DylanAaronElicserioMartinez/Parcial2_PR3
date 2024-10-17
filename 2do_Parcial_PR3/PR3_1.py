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