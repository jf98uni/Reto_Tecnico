

import controller
import sys


    
print("\n\nHola Bienvenido a quien quiere ser millonario\n")
print("\n¿Quieres jugar? presiona (y) para jugar y (n) para salir\n\n")
print ("Recuerda simpre darle enter cuando respondas")


#---------------------- Menu principal ------------------
inputs = input('\n Seleccione una opcion para continuar: \n \n')
    
if inputs[0] == "y":  # inicia el juego
    
    inputs6 = input ("\n Por favor escribe tu nombre: ")
    
    controller.jugador = inputs6
        
    pregunta = controller.iniciar_juego_pregutnas(inputs[0])

    respuestas = controller.iniciar_juego_respuestas(inputs[0])
        
    print ("\n{}\n".format(pregunta))
        
    for respuesta in respuestas:
            
        print (respuesta)
        
    seguir = True
    
    while seguir == True:
        
        inputs1 = int( input('\n Seleccione una respuesta del 1 al 4 \n \n'))
        
        
        if controller.verificar_respuesta(inputs1) ==  1 :
            
            dollars = controller.Dollars
            
            print ("\nRespuesta Correcta ahora tu saldo es de: {}\n \n".format(dollars))
            
            if controller.categoria_acatual == 5 and controller.Dollars == 11111000:
                
                #controller.guardar()
                
                print ("\n \nGanador Ahora eres millonario")
                
                inputs4 = input("\n ¿Quieres jugar de nuevo? \n")
                
                if inputs4[0] == "y":
                    
                    print ("\nPara jugar de nuevo dale a run file desde el archivo view \n Recuerda que puedes ver tu puntuacion en el archivo Historial.csv")
                    sys.exit(0)
                
                if inputs4[0] == "n":
                    
                    print ("\n Hasta luego \n Recuerda que puedes ver tu puntuacion en el archivo Historial.csv ")
                    sys.exit(0)
                    
            
            inputs2 = input('\n Deseas continuar o retirarte: (presiona (y) para continuar y (n) para salir)\n')
            
            if inputs2[0] == "y":
                
                preguntas2 = controller.continuar_1_Actualizar_preguntas(inputs2[0])
                
                respuestas2 = controller.continuar_1_Actualizar_respuestas(inputs2[0])
                
                print ("\n{}\n".format(preguntas2))
        
                for respuesta in respuestas2:
            
                    print (respuesta)  
                    
            if inputs2[0] == "n":
                
                preguntas2 = controller.continuar_1_Actualizar_preguntas(inputs2[0])
                
                print ("\nHasta luego {}\n".format(preguntas2))
                
                print ("\nPara jugar de nuevo dale a run file desde el archivo view \n Recuerda que puedes ver tu puntuacion en el archivo Historial.csv")
                
                sys.exit(0)
                
                    
                
        elif controller.verificar_respuesta(inputs1) == 0:
            
            controller.Dollars = 0
            
            print ("\n Has perdido y has perdido todo\n \nPara jugar de nuevo dale a run file desde el archivo view \n Recuerda que puedes ver tu puntuacion en el archivo Historial.csv\n \n")
            sys.exit(0)

    sys.exit(0)    
            

if inputs[0] == "n":
        
    print(controller.iniciar_juego_respuestas(inputs[0]))
        
    sys.exit(0)
        












