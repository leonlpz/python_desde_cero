"""
total = 0
for x in range(0, 100, 10):
    print(x)

for i in range(7):
    print("Estamos en la iteración número " + str(i))
    total += 5
    print("El total es -> " + str(total))
print("finalizo el for")
"""
#como desarrolladores debemos pensar en algoritmos flexibles, que sean reutilizables
#y que no solo sirvan para esta oportunidad!!! hacer cosas mejor que las que nos piden
#print("HOLA".lower())
#print("hola".upper())

#LOOP FOR
"""
part_max = int(input("Por favor ingrese la cantidad de participantes -> "))
print("")
print("El sistema ha sido configurado para aceptar", part_max," participantes. A partir de ahora, el ordenador esta listo para recibirlos.")
print("")

for x in range(part_max):
    nombre = input("Ingrese su nombre -> ")
    email = input("Ingrese su email -> ")
    print("Hola ",nombre," su email es: ",email," ¿desea confirmar la inscripción?")
    print("Escriba \"SI\" para confirmar, o escriba \"NO\" para rechazar.")
    respuesta = input()
    respuesta = respuesta.lower()#no importa como escriban la respuesta, el str queda minusculizado
    if respuesta == "si":
        print("")
        print("*****************************************************")
        print("*Gracias, confirmamos su inscripción, lo esperamos!*")
        print("*****************************************************")
        print("\n\n\n")
        print("SU NÚMERO DE PARTICIPANTE ES: ",x)
    else:
        print("")
        print("*********************")
        print("*Operación cancelada*")
        print("*********************")

print("Cantidad maxima alcanzada")
"""
#LOOP WHILE
#contador = 0
#while contador<100:
 #   print("La cuenta es -> ",contador)
  #  contador += 1 #contador = contador + 1

part_max = int(input("Por favor ingrese la cantidad de participantes -> "))
print("")
print("El sistema ha sido configurado para aceptar", part_max," participantes. A partir de ahora, el ordenador esta listo para recibirlos.")
print("")

cant_part = 0
while(cant_part < part_max): 
    nombre = input("Ingrese su nombre -> ")
    email = input("Ingrese su email -> ")
    print("Hola ",nombre," su email es: ",email," ¿desea confirmar la inscripción?")
    print("Escriba \"SI\" para confirmar, o escriba \"NO\" para rechazar.")
    respuesta = input()
    respuesta = respuesta.lower()#no importa como escriban la respuesta, el str queda minusculizado
    if respuesta == "si":
        print("")
        print("*****************************************************")
        print("*Gracias, confirmamos su inscripción, lo esperamos!*")
        print("*****************************************************")
        print("\n\n\n")
        print("SU NÚMERO DE PARTICIPANTE ES: ",cant_part)
        cant_part += 1
    else:
        print("")
        print("*********************")
        print("*Operación cancelada*")
        print("*********************")

print("Cantidad maxima alcanzada")
