nublado = True
aburrido = False
aburrido = not(aburrido) #negar o revertir booleanas

if nublado == True:
    print("esta nublado")
    if aburrido == True:
        print("ya que esta nublado y estamos aburridos, vamos a cine")

print("Finalizado1")

if nublado == True and aburrido == True:
    print("ya que esta nublado y estamos aburridos, vamos a cine")

print("Finalizado2")

if nublado == True or aburrido == True:
    print("ya que esta nublado y estamos aburridos, vamos a cine")

print("Finalizado3")