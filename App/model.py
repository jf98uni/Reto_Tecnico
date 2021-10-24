import controller
import random
numero_actual = 0

def seleccionar_categoria_preguntas (category): # carga las preguntas 
    
    numero = random.randint(1, 5) # da un numero al azar para asi dar una pregunta de la categoria correspondiente de forma aleatoria 
    
    global numero_actual 
    
    numero_actual = numero # Carga el numero fuera de la funcion para ser usado por otras varia cada vez que se llama a la funcion
    
    if category == 1:
        
        preguntas = {1:'La capital de francia es:',2:"¿En que continente se encuentra el rio Amazonas?",3:"¿Cual es la capital de Canada?",4:"El Quijote fue escrito por:",5:"11 x 2 ="}
        
    elif category == 2:
        
        preguntas = {1:"¿Cuál es el río más largo del mundo?",2:"¿Cuál es el país con más habitantes del mundo?",3:"¿Cuál es el edificio más alto del mundo?",4:"¿Cuántos años duró la Segunda Guerra Mundial?",5:" ¿Cuál es el himno de la Unión Europea?"}
    
    elif category == 3:
        
        preguntas = {1:"¿Cuándo empezó la Revolución Rusa?",2:"¿Cuál es el atleta con más medallas olímpicas?",3:"¿Cuál es el planeta más grande del Sistema Solar?",4:"¿Cuál es la luna más grande de Saturno?",5:"¿Cuál es el álbum musical más vendido de la historia?"}
        
    elif category == 4:
        
        preguntas ={1:"¿Cuándo se inventó la imprenta?",2:"¿Cuántos corazones tiene un gusano de tierra?",3:"¿Cuántos habitantes tiene Tokio?",4:"¿Cuándo asesinaron al presidente John F. Kennedy?",5:"¿Cuánto duró “La Guerra de los Cien Años”?"}    
        
    elif category == 5: 
        
        preguntas ={1:"¿Cuál es el gas mayoritario de la atmósfera terrestre?",2:"¿Qué animal contagió a los humanos en la pandemia de peste negra?",3:" ¿Qué río atraviesa la ciudad de Benarés, en la India?",4:"¿Cuál es la universidad más antigua del mundo?",5:"¿Cuál es el idioma más antiguo de Europa que sigue usándose?"}
    
    return preguntas[numero]

def selec_cate_respuestas (category): # carga las respuestas 
    
    
    if category == 1:
        
        respuestas = {1:["1: Tirana","2: Berlín","3: París","4: Banjul"],2:["1: Europa","2: Asia","3: America","4: Africa"],3:["1: Vancouver","2: Toronto","3: Ottawa ","4: Quebec "],4:["1: Camilo José Cela","2: Pío Baroja","3: Miguel de Cervantes ","4: Miguel Delibes "],5:["1: 12","2: 42","3: 22 ","4: 32"]}
    
    elif category == 2:
    
        respuestas = {1:["1: Nilo","2: Volga","3: Rin","4: Amazonas"],2:["1: USA","2: Rusia","3: India","4: China"],3:["1: Makkah Royal Clock Tower","2: Burj Khalifa","3: Shanghai Tower","4: Ping An Finance Center "],4:["1: 6","2: 5 ","3: 4  ","4: 7 "],5:["1: La Marsellesa ","2: Orientales, la patria o la tumba","3: Oda a la Alegría ","4: Land of my fathers "]}
    
    elif category == 3:
        
        respuestas = {1:["1: 1917","2: 1849","3: 1939 ","4: 1915 "],2:["1: Larisa Latynina","2: Michael Phelps","3: Nikolai Andrianov ","4: Boris Shajlín "],3:["1: Júpiter ","2: Saturno ","3: Urano ","4: Neptuno "],4:["1: Titán ","2: Epimeteo ","3: Jano ","4: Japeto "],5:["1: The Dark Side of the Moon","2: Bat Out of Hell ","3: Back in Black ","4: Thriller "]}
    
    elif category == 4:
        
        respuestas = {1:["1: 1448 ","2: 1528 ","3: 1498 ","4: 1592 "],2:["1: 3 ","2: 2  ","3: 5 ","4: 1 "],3:["1: 20 millones ","2: 40 millones ","3: 12 millones ","4: 15 millones"],4:["1: 2 de Junio de 1965","2: 22 de noviembre de 1963","3: 12 de Mayo de 1964 ","4: 25 de Agosto de 1963 "],5:["1: 100","2: 116","3: 99 ","4: 84"]}
    
    elif category == 5:
        
        respuestas = {1:["1: nitrógeno","2: oxígeno","3: argón ","4: helio "],2:["1: Ratas","2: Pulgas","3: Moscas ","4: Garrapatas "],3:["1: Ganges","2: Volga","3: Narmada ","4: Indo "],4:["1: Universidad de Bolonia ","2: Universidad de Oxford ","3: Universidad de París  ","4: Universidad de Montpelier  "],5:["1: Euskera","2: Macedonio","3: Lituano ","4: Islandés "]}
    
    return respuestas[numero_actual]    # usa el numero aleatorio usado en la funcion anterior para asi dar las respuestas correspondientes 
    
    

def respuestas_correctas (respuesta,list): # Compara la respuesta seleccionada con las respuestas correctas 
    
    stringAcomparar = list[respuesta-1]
    # Todas las respuestas correcta segun su numero
    
    respuestas_inde_1 = ["1: 6","1: 1917","1: Júpiter ","1: Titán ","1: 1448 ","1: nitrógeno","1: Ganges","1: Universidad de Bolonia ","1: Euskera"]
    respuestas_inde_2 = ["2: Burj Khalifa","2: Michael Phelps","2: 40 millones ","2: 22 de noviembre de 1963","2: 116","2: Pulgas"]
    respuestas_inde_3 = ["3: París","3: America","3: Ottawa ","3: Miguel de Cervantes ","3: 22 ","3: Oda a la Alegría ","3: 5 "]
    respuestas_inde_4 = ["4: Amazonas","4: China","4: Thriller "]
    
    if respuesta == 1 and stringAcomparar in respuestas_inde_1:
        
        return 1
        
    elif respuesta == 2 and stringAcomparar in respuestas_inde_2:
        
        return 1 
        
    elif respuesta == 3 and stringAcomparar in respuestas_inde_3:
        
        return 1 
    
    elif respuesta == 4 and stringAcomparar in respuestas_inde_4:
        
        return 1
        
    else:
        
        return 0
    
        


def puntaje (category): # asigna un puntaje segun la categoria y si la respuesta fue correcta.
    
    if category ==  1:

        dollars = 1000
    
    elif category == 2:
        
        dollars = 10000
    
    elif category == 3 :
        
        dollars = 100000
    
    elif category == 4: 
        
        dollars = 1000000
    
    elif category == 5:
        
        dollars = 10000000
    
    return dollars 


    