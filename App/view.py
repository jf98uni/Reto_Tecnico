

import controller
import sys



# estos tres print dan la bienvenida al juego 
print("\n\nHola Bienvenido a quien quiere ser millonario\n")
print("\n¿Quieres jugar? presiona (y) para jugar y (n) para salir\n\n")
print ("Recuerda simpre darle enter cuando respondas y responder en minuscula")


#---------------------- Menu principal ------------------
inputs = input('\n Seleccione una opcion para continuar: \n \n')
    
if inputs[0] == "y":  # inicia el juego
    
    inputs6 = input ("\n Por favor escribe tu nombre: ")
    
    controller.jugador = inputs6  # Agrega el nombre del jugador para guardar en el historial
        
    pregunta = controller.iniciar_juego_pregutnas(inputs[0])  #inicia las preguntas

    respuestas = controller.iniciar_juego_respuestas(inputs[0]) #inicia las opciones de respuesta para la pregunta
        
    print ("\n{}\n".format(pregunta))
        
    for respuesta in respuestas: # impreme las posibles respuestas
            
        print (respuesta)
        
    seguir = True
    
    while seguir == True: # crea un loop para jugar hasta la categoria 5 
        
        inputs1 = int( input('\n Seleccione una respuesta del 1 al 4 \n \n'))
        
        
        if controller.verificar_respuesta(inputs1) ==  1 : # verifica la respuesta que el usuario dio y da el acomulado del premio hasta el momento
            
            dollars = controller.Dollars
            
            print ("\nRespuesta Correcta ahora tu saldo es de: {}\n \n".format(dollars)) 
            
            if controller.categoria_acatual == 5 and controller.Dollars == 11111000: # confirma si el usuario llego al ultimo nivel y respondio correctamente 
                
                #controller.guardar()
                
                print ("\n \nGanador Ahora eres millonario")
                
                inputs4 = input("\n ¿Quieres jugar de nuevo? (presiona (y) para si y (n) para salir)\n \n")
                
                if inputs4[0] == "y":
                    
                    print ("\nPara jugar de nuevo dale a run file desde el archivo view \n Recuerda que puedes ver tu puntuacion en el archivo Historial.csv")
                    sys.exit(0)
                
                if inputs4[0] == "n":
                    
                    print ("\n Hasta luego \n Recuerda que puedes ver tu puntuacion en el archivo Historial.csv ")
                    sys.exit(0)
                    
            
            inputs2 = input('\n Deseas continuar o retirarte: (presiona (y) para continuar y (n) para salir)\n') # pregunta al usuario si desea continuar en el juego o llevarse sus ganancias
            
            if inputs2[0] == "y": # si decide continuar avanza a la siguiente categoria y se muestra la pregunta con sus respectivas respuestas
                
                preguntas2 = controller.continuar_1_Actualizar_preguntas(inputs2[0])
                
                respuestas2 = controller.continuar_1_Actualizar_respuestas(inputs2[0])
                
                print ("\n{}\n".format(preguntas2))
        
                for respuesta in respuestas2:
            
                    print (respuesta)  
                    
            if inputs2[0] == "n": # saca al usuario del juego cuando este lo decide volutariamente
                
                preguntas2 = controller.continuar_1_Actualizar_preguntas(inputs2[0])
                
                print ("\nHasta luego {}\n".format(preguntas2))
                
                print ("\nPara jugar de nuevo dale a run file desde el archivo view \n Recuerda que puedes ver tu puntuacion en el archivo Historial.csv")
                
                sys.exit(0)
                
                    
                
        elif controller.verificar_respuesta(inputs1) == 0: #saca al usuario de forma forzada ya que respondio mal
            
            controller.Dollars = 0 # le quita al usuario todo lo ganado hasta el momento.
            
            print ("\n Has perdido y has perdido todo\n \nPara jugar de nuevo dale a run file desde el archivo view \n Recuerda que puedes ver tu puntuacion en el archivo Historial.csv\n \n")
            sys.exit(0)

    sys.exit(0)    
            

if inputs[0] == "n": # si el usuario no quiere jugar lo saca de la aplicacion
        
    print(controller.iniciar_juego_respuestas(inputs[0]))
        
    sys.exit(0)
        












