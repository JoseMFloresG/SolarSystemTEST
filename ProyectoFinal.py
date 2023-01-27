'''
Este programa sirve para comprobar tu nivel de aprendizaje sobre el Sistema Solar
'''
lista=[]
def facil():
    while True:
        try:
            print("Has seleccionado la dificultad Facil. Recuerda leer muy bien tu pregunta y responderla correctamente\n \n")
            print("Primera pregunta \n")
            print("Cuantos Planetas hay en el sistema solar? \n")
            print("a: 8")
            print("b: 7")
            print("c: 9")
            respuesta1 = input ("Cual es tu respuesta? ")
            if respuesta1 == "a":
                respuesta1 = 20
                lista.append("8")
            else:
                respuesta1 = 0
            
            print()
            
            print("Segunda pregunta \n")
            print("¿El sol dejará de existir en algún momento? \n")
            print("a: Si")
            print("b: No")
            
            respuesta2 = input ("Cual es tu respuesta? ")
            if respuesta2 == "a":
                respuesta2 = 20
                lista.append("Si")
            else:
                respuesta2 = 0
            
            print()
            
            print("Tercera Pregunta \n")
            print("¿Qué planeta posee la atmósfera más caliente del sistema solar? \n")
            print("a: Mercurio")
            print("b: Venus")
            print("c: Marte")

            respuesta3 = input ("Cual es tu respuesta? ")
            if respuesta3 == "b":
                respuesta3 = 20
                lista.append("Venus")
            else:
                respuesta3 = 0
            
            print()
            
            print("Cuarta Pregunta \n")
            print("¿Qué planeta posee un año más largo, la Tierra o Marte? \n")
            print("a: Tierra")
            print("b: Marte")

            respuesta4 = input ("Cual es tu respuesta? ")
            if respuesta4 == "b":
                respuesta4 = 20
                lista.append("Marte")
            else:
                respuesta4 = 0
            
            print()
            
            print("Quinta Pregunta \n")
            print("¿Cuál es el planeta con más edad del sistema solar? \n")
            print("a: Venus")
            print("b: Jupiter")
            print("c: Saturno")

            respuesta5 = input ("Cual es tu respuesta? ")
            if respuesta5 == "b":
                respuesta5 = 20
                lista.append("Jupiter")
            else:
                respuesta5 = 0
            
            print()

            resultado = (respuesta1 + respuesta2 + respuesta3 + respuesta4 + respuesta5)
            print("El resultado de tu examen es de! " + str(resultado))
            
            print("Que quieres hacer?")
            print("1: Volver al menú principal")
            print("2: Reiniciar tu examen")
            print("3: Salir \n")
            respuesta = int(input("Seleccione su respuesta"))
            
            if respuesta == 1:
                menu()
            
            if respuesta == 2:
                facil()
            
            if respuesta == 3:
                break
        
        except ValueError as error:
            print("Ha ocurrido un error " + str(error) + " Selecciona una opcion valida \n")
            break
    
    
    


def intermedio():
    while True:
        try:
            print("Has seleccionado la dificultad Intermedio. Recuerda leer muy bien tu pregunta y responderla correctamente\n \n")
            print("Primera pregunta \n")
            print("¿Cuál es el planeta más denso del sistema solar? \n")
            print("a: La Tierra")
            print("b: Marte")
            print("c: Jupiter")
            respuesta1 = input ("Cual es tu respuesta? ")
            if respuesta1 == "a":
                respuesta1 = 20
                lista.append("Tierra")
            else:
                respuesta1 = 0
            
            print()
            
            print("Segunda pregunta \n")
            print("¿El sol dejará de existir en algún momento? \n")
            print("a: 5")
            print("b: 8")
            print("c: 7")
            
            respuesta2 = input ("Cual es tu respuesta? ")
            if respuesta2 == "a":
                respuesta2 = 20
                lista.append("5")
            else:
                respuesta2 = 0
            
            print()
            
            print("Tercera Pregunta \n")
            print("¿Cuántos planetas del sistema solar poseen anillos? \n")
            print("a: 5")
            print("b: 4")
            print("c: 3")

            respuesta3 = input ("Cual es tu respuesta? ")
            if respuesta3 == "b":
                respuesta3 = 20
                lista.append("4")
            else:
                respuesta3 = 0
            
            print()
            
            print("Cuarta Pregunta \n")
            print("¿Cuál es el planeta más similar a la Tierra en tamaño, masa y composición?  \n")
            print("a: Marte")
            print("b: Venus")
            print("c: Mercurio")

            respuesta4 = input ("Cual es tu respuesta? ")
            if respuesta4 == "b":
                respuesta4 = 20
                lista.append("Venus")
            else:
                respuesta4 = 0
            
            print()
            
            print("Quinta Pregunta \n")
            print("¿Cuál es el planeta más radiactivo del sistema solar? \n")
            print("a: Urano")
            print("b: Jupiter")
            print("c: Saturno")

            respuesta5 = input ("Cual es tu respuesta? ")
            if respuesta5 == "b":
                respuesta5 = 20
                lista.append("Jupiter")
            else:
                respuesta5 = 0
            
            print()

            resultado = (respuesta1 + respuesta2 + respuesta3 + respuesta4 + respuesta5)
            print("El resultado de tu examen es de! " + str(resultado))
            
            print("Que quieres hacer?")
            print("1: Volver al menú principal")
            print("2: Reiniciar tu examen")
            print("3: Salir \n")
            respuesta = int(input("Seleccione su respuesta"))
                    
            if respuesta == 1:
                menu()
                    
            if respuesta == 2:
                intermedio()
                    
            if respuesta == 3:
                break
            
        except ValueError as error:
            print("Ha ocurrido un error " + str(error) + " Selecciona una opcion valida \n")
            break
    
def dificil():
    while True:
        try:
            print("Has seleccionado la dificultad Dificil. Recuerda leer muy bien tu pregunta y responderla correctamente\n \n")
            print("Primera pregunta \n")
            print("¿En qué planeta se encuentran los vientos más fuertes del sistema solar? \n")
            print("a: Neptuno")
            print("b: Urano")
            print("c: Saturno")
            respuesta1 = input ("Cual es tu respuesta? ")
            if respuesta1 == "a":
                respuesta1 = 20
                lista.append("Neptuno")
            else:
                respuesta1 = 0
            
            print()
            
            print("Segunda pregunta \n")
            print("¿Cuántos satélites naturales posee el planeta Marte? \n")
            print("a: 2")
            print("b: 1")
            print("c: 0")
            
            respuesta2 = input ("Cual es tu respuesta? ")
            if respuesta2 == "a":
                respuesta2 = 20
                lista.append("2")
            else:
                respuesta2 = 0
            
            print()
            
            print("Tercera Pregunta \n")
            print("¿Cuál es el planeta menos denso del sistema solar?\n")
            print("a: Jupiter")
            print("b: Saturno")
            print("c: Urano")

            respuesta3 = input ("Cual es tu respuesta? ")
            if respuesta3 == "b":
                respuesta3 = 20
                lista.append("Saturno")
            else:
                respuesta3 = 0
            
            print()
            
            print("Cuarta Pregunta \n")
            print("¿Cuáles son los principales elementos en la atmósfera de Urano?  \n")
            print("a: Oxigeno y Helio")
            print("b: Hidrogeno y Helio")
            print("c: Fosforo y Azufre")

            respuesta4 = input ("Cual es tu respuesta? ")
            if respuesta4 == "b":
                respuesta4 = 20
                lista.append("Hidrogeno y Helio")
            else:
                respuesta4 = 0
            
            print()
            
            print("Quinta Pregunta \n")
            print("¿Cómo se llama el satélite natural más grande de Saturno? \n")
            print("a: Mimas")
            print("b: Titan")
            print("c: Jápeto")

            respuesta5 = input ("Cual es tu respuesta? ")
            if respuesta5 == "b":
                respuesta5 = 20
                lista.append("Titan")
            else:
                respuesta5 = 0
            
            print()

            resultado = (respuesta1 + respuesta2 + respuesta3 + respuesta4 + respuesta5)
            print("El resultado de tu examen es de! " + str(resultado))
            
            print("Que quieres hacer?")
            print("1: Volver al menú principal")
            print("2: Reiniciar tu examen")
            print("3: Salir \n")
            respuesta = int(input("Seleccione su respuesta"))
                            
            if respuesta == 1:
                menu()
                            
            if respuesta == 2:
                intermedio()
                            
            if respuesta == 3:
                break
                    
        except ValueError as error:
            print("Ha ocurrido un error " + str(error) + " Selecciona una opcion valida \n")
            break    

def menu():
    while True:
        try:
            print("1- Fácil")
            print("2- Intermedio")
            print("3- Avanzado")
            print("0- Salir \n")
            
            dificultad = int(input("Selecciona la dificultad "))
            
            if dificultad == 1:
                facil()
            
            if dificultad == 2:
                intermedio()
            
            if dificultad == 3:
                dificil()
            
            if dificultad == 0:
                break
        except ValueError as error:
            print("Ha ocurrido un error " + str(error) + " Selecciona una opcion valida \n")
    
    
nombre = input("Bienvenido!, antes de acceder al programa digite su nombre ")
print("Hola! " + nombre + " este es un test de conocimiento sobre su aprendizaje del Sistema Solar.")
print("Se te realizará un total de 5 preguntas dependiendo de la dificultad seleccionada.")
print("Cada pregunta vale 20 puntos de 100, asi que lee y responde correctamente!\n")

menu()
referenciado=[]
arch1=open("Referencia.txt","r")
referenciado=arch1.readlines()
arch1.close()
archEscribir=open("ProyectoFinalProgra.txt","w")
archEscribir.write("Este programa fue escrito por:\n")
archEscribir.write("José Miguel Flores y José Andres Ordieres")
archEscribir.write("\nTus respuestas correctas fueron: " + str(lista))
archEscribir.write("\nLas preguntas fueron sacadas de la siguiente pagina en caso de que quieras consultar mas preguntas:\n" +str(referenciado))
archEscribir.close()
    

    

