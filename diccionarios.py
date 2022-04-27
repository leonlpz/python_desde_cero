"""
paciente = {"nombre":"Juan", "edad":32, "peso":70.5, "fuma":False}
print(paciente["nombre"])
print(paciente["fuma"])
print(paciente.get("edad"))
#valor = paciente.pop("edad") #quita edad del diccionario
paciente.update({"edad":18}) #actualiza un valor del diccionario por uno nuevo
print(paciente)
paciente["edad"] = 20 # otra manera de actualizar un valor
print(paciente)
print("peso" in paciente) # in permite preguntar si un valor esta en el diccionario
"""
#recorrer un diccionario
paciente1 = {"nombre":"Juan1", "edad":42, "peso":70.5, "fuma":True, "Hist clin":"bla..."}
paciente2 = {"nombre":"Juan2", "edad":32, "peso":60.5, "fuma":False, "Hist clin":"bla..."}
paciente3 = {"nombre":"Juan3", "edad":23, "peso":50.5, "fuma":False, "Hist clin":"bla..."}

pacientes = [paciente1,paciente2,paciente3] #lista de diccionarios

#demo = ['uno','dos','tres','cuatro','cinco']
#for x in rangre(len(demo))
#    print(demo[x])

for x in range(len(pacientes)):
    print("")
    print("--------------------")
    print("- DICCIONARIO N°",x+1,"-")
    print("--------------------")
    print("CLAVE\t\tVALOR\t\t<33\t\t\n")
    for clave, valor in pacientes[x].items():
        menor = ""
        if (clave == "edad" and valor < 33):
            menor = "*"
        print(clave,"\t\t",valor,"\t\t",menor)
            
