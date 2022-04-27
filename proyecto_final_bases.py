#Pequeño proyecto de practica en python
import os #libreria de herramientas para operar desde python comandos de terminal
#habra un bucle infinito hasta que el usuario lo detenga
os.system('cls')
print("")
print("╔═════════════════════════════════════════════════════════╗")
print("║Bienvenidos al sistema de historias clínicas del hospital║")
print("╚═════════════════════════════════════════════════════════╝")
print("")

#******************
#VARIABLES GLOBALES
#******************

running = True
database = list()

#*********
#FUNCIONES
#*********

def show_menu():
    print("")
    print("")
    print("\t\t* 1 - Cargar paciente")
    print("\t\t* 2 - Buscar paciente")
    print("\t\t* 3 - Listar pacientes")
    print("\t\t* 4 - Salir")
    print("")
    res = input("INGRESE UNA OPCION ► ")  
    os.system('cls')
    return res

def response_validate(r):
    validated = False
    num_res = 0

    if response.isdigit():
        num_res = int(response)
        if num_res >= 1 and num_res <= 4:
            msg = "esta en rango"
            validated = True
        else:
            msg = "Fuera de rango"
    else:
        msg = "Entrada incorrecta"
    
    return validated,num_res,msg     


#******************
#LOOP PRINCIPAL
#******************

while running:
    response = show_menu()
    validated,num_res,msg = response_validate(response)
    if validated:
        if num_res == 1:
           name = input("Ingrese el nombre del paciente ► ")
           history = input("Ingrese la historia clinica del paciente ► ")
           paciente = {"nombre":name, "historia":history}
           database.append(paciente)
           #print(database)

        elif num_res == 2:
            name = input("Ingrese el nombre del paciente: ")
            finded = False
            for x in range(len(database)):
                if database[x]["nombre"].lower() == name.lower():
                    finded = True
                    print("")
                    print("PACIENTE ENCONTRADO! :D | His. CLINICA  ► ",database[x]["historia"] )
                    print("")
                   
            if finded == False:
                print("")
                print("PACIENTE NO ENCONTRADO! :(") 
                                        
        elif num_res == 3:  
            print("")
            print("╔═══════════════════════╗")
            print("║ LISTADO DE PACIENTES  ║")
            print("╚═══════════════════════╝")
            print("")
            for x in range(len(database)):
                print("Nombre ► ".ljust(10),database[x]["nombre"], "H. clinica ► ".ljust(10),database[x]["historia"])
        
            print("FIN DE LISTA")

        else:
            running = False
    else:
        print(msg)


print("")  
print("Aplicacion finalizada. Regrese pronto.")
print("")  
       
    