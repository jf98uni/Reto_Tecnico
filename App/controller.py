
from os import name
import model
import csv
import config as cf
# cosas globales q ue se usan en todo el juego algunas son fijas otras variables

categorias = [1,2,3,4,5] # categorias del juego

categoria_acatual = 1 # variable, da la categoria en la que se encuentra el jugador

pregunta_actual = "" # la pregunta aleatoria que se esta jugando

respuestas = [] # las respuestas a la pregunta

Dollars = 0 #el dinero acomulado del jugador

jugador = ""


def iniciar_juego_pregutnas (respuesta): # inica el juego "El jugador debe especificar si quiere o no jugar"
    
    global categoria_acatual
    
    if respuesta == "y" :
        
        categoria = categoria_acatual 
        
        global pregunta_actual  # inicializa solo las preguntas
        
        pregunta_actual = model.seleccionar_categoria_preguntas(categoria)
        
        return pregunta_actual
    if respuesta == "n":
        
        pass
    
    


def iniciar_juego_respuestas (respuesta): # inica el juego "El jugador debe especificar si quiere o no jugar"
    
    global categoria_acatual
    global respuestas  # inicializa solo las respuestas
    
    
    if respuesta == "y" : 
        
        categoria = categoria_acatual
        
        respuestas = model.selec_cate_respuestas(categoria)
        
        return respuestas
        
    if respuesta == "n":
        
        print ('Nos vemos Luego !!')
    
    

# estos le preguntan al usuario si continua 

def continuar_1_Actualizar_preguntas (respuesta):
    
    global categoria_acatual
    
    global pregunta_actual
    
    global jugador
    
    global Dollars
    
    
    if respuesta == "y": # eleva la categoria del juego para pasar al siguiente nivel
        
        categoria_acatual = categoria_acatual + 1
        
        pregunta_actual = model.seleccionar_categoria_preguntas(categoria_acatual)
        

        
        return pregunta_actual
    
    elif respuesta == "n":
        
        guardar(jugador,Dollars)
        
        print (" Te llevas a casa: {}".format(Dollars))



def continuar_1_Actualizar_respuestas (respuesta):
    
    global categoria_acatual
    
    global respuestas
    
    if respuesta == "y": # eleva la categoria del juego para pasar al siguiente nivel
        
        respuestas = model.selec_cate_respuestas(categoria_acatual)
        
        return respuestas


   
    
def verificar_respuesta (respuesta): # verifica que la respuesta escogida por el jugador sea la correcta
    
    verificador = model.respuestas_correctas(respuesta,respuestas)
    
    if verificador == 1:

        global Dollars
        
        global categoria_acatual
        
        global jugador
        
        if categoria_acatual == 5:
            
            guardar(jugador,Dollars)
        
        # suma el monto del premio si la respues fue correcta
        
        Dollars = Dollars + model.puntaje(categoria_acatual)
        
        return 1 
    
    else:
        Dollars = 0
        guardar(jugador,Dollars)
        return 0




def guardar (jugador,dinero):
    
    info = []
    
    info.append([jugador,dinero])
    
    myFile = open(cf.data_dir +'Historial.csv', 'a')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(info)


