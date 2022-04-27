#funcion simple
def calcula():
    calculo = 43 * 12 * 80
    calculo = calculo / 7
    coeficiente = 45 * 3.1416
    calculo = calculo * coeficiente
    calculo = "El resultado es -> " + str(calculo)
    print(calculo)

#Funcion que recibe parametros
def calcula_valor(mensaje, numero1, numero2):
    resultado = numero1 + numero2
    print(mensaje + str(resultado))

calcula_valor("La suma es -> \n", 5, 10)

#Funcion que recibe y devuelve parametros
def calcula_valor_2(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    return suma, resta
   
res1, res2 = calcula_valor_2(10,100)

print(res1)
print(res2)

def calcula_valor_3(numero1,numero2,comando):
    if comando == "-":
        resultado = numero1 - numero2
    if comando == "+":
        resultado = numero2 + numero1

    return resultado

res1 = calcula_valor_3(20,200,"+")
print(res1)