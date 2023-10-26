import random
import os
import time

def run():
    #pass
    DB = [
        "C",
        "PYTHON",
        "JAVASCRIPT",
        "JAVA",
        "PHP"
    ]
    
    Imagen = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''','''
     \O/ 
      |
     / \ 
    ======''']


    #LIMPIAR LA PANTALLA
    borrarPantalla = lambda: os.system ("cls")
    borrarPantalla() #Limpia la pantalla

    #IDENTIFICANDO EL USUARIO
    nombre = os.getenv("USERNAME")

    if nombre == "Ninguno":
        nombre = "Usuario"
    else:
        nombre = os.getenv("USERNAME")

    #----------------------------------------------------------------
    if os.name == "posix":
        var = "clear"
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       var = "cls"
    os.system(var)
    print("")
    print(" E ")
    time.sleep(0.1)
    os.system(var)
    print("")
    print(" EM ")
    time.sleep(0.1)
    os.system(var)
    print("")
    print(" EMP ")
    time.sleep(0.1)
    os.system(var)
    print("")
    print(" EMPE")
    time.sleep(0.1)
    os.system(var)
    print("")
    print(" EMPEC")
    time.sleep(0.1)
    os.system(var)
    print("")
    print(" EMPECE")
    time.sleep(0.1)
    os.system(var)
    print("")
    print(" EMPECEM")
    time.sleep(0.1)
    os.system(var)
    print("")
    print(" EMPECEMO")
    time.sleep(0.1)
    os.system(var)
    print("")
    print(" EMPECEMOS")
    time.sleep(0.1)
    os.system(var)
    print("")
    print(" EMPECEMOS :)")
    time.sleep(0.1)
    os.system(var)
    #----------------------------------------------------------------
    
    print(f"Bienvenido/a {nombre} al juego AHORCADO :)")
    time.sleep(1)
    
    #solicitar a la persona que ingrese
    palabra = random.choice(DB)
    espacios = ["_"] * len(palabra)
    intentos_tot = 6
    intentos_fallidos = 0
    #limpieza de la pantalla para un ciclo infinito
    #se utiliza librería
    
    #ARREGLO PARA GUARDAR LA INFORMACIÓN INGRESADA
    DataIngresada = []
    
    while True:
        borrarPantalla() #os.system("cls")
        
        print(f"Usted tiene {intentos_tot} intentos por realizar.")
            
        for character in espacios:
            print(character, end = " ")
        print(Imagen[intentos_fallidos])
        palabra_recibida = input("Elige una letra: ").upper()
        
        if palabra_recibida in DataIngresada:
            print(f"Usted ha ingresado la misma letra: {palabra_recibida}")
            intentos_tot -= 1
            intentos_fallidos += 1
            time.sleep(1)
            os.system(var)
        
        DataIngresada.append(palabra_recibida)
        
        if len(palabra_recibida) > 1:
            input("Debe ingresar solo una letra.")
            time.sleep(0.3)
            os.system(var)
        else:
            found = False
            for idx, character in enumerate(palabra):
                if character == palabra_recibida:
                    espacios[idx] = palabra_recibida
                    found = True 
                    
            if not found:
                intentos_tot -= 1
                intentos_fallidos += 1
                       
            if "_" not in espacios:
                borrarPantalla() #os.system("cls")
                print("Ganaste :)")
                print(Imagen[7])
                break
                #input()
            
            if intentos_tot == 0:
                borrarPantalla() #os.system("cls")
                print("Perdiste :(")
                print("La palabra era: "+ palabra)
                print(Imagen[intentos_fallidos])
                break
                #input()
def continuar(): 
    var = input("¿Quisieras continuar con otra partida? : SI o NO \n").upper()
    
    if var == "SI":
        run()
    else:
        print("Gracias :) ")
    
if __name__ == '__main__':
    run()
    continuar()