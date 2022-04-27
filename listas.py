
sabores = ["chocolate","crema","vainilla",True,10,12.3] #una variable de variables:str,int,float,...

print(sabores)

elemento_eliminado = sabores.pop(1) #metodo .pop elimina elemento
print(elemento_eliminado)

print(sabores)

sabores.append("esto es el ultimo") # .append agrega un elemento al final de la lista
print(sabores)

sabores.insert(0,"objeto insertado") # . insert inserta un elemento
print(sabores)

sabores1 = ["chocolate","crema"]
sabores2 = ["vainilla","dulce de leche","crema"]

sabores1.extend(sabores2) # .extend agrega una lista a otra
print(sabores1)

sabores1.remove("crema") # .remove elimina la primera aparicion del elemento en el array
print(sabores1)




