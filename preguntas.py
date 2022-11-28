"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

def read_texto():
    lineas_texto=[]
    with open("data.csv", "r") as file:
        data = file.readlines()
    for line in data:
        line = line.replace('\n','')
        row = line.split(sep='\t')
        lineas_texto.append(row) 
    return lineas_texto



def reducer(sequence):
    counter = {}
    for key, value in sequence:
        if key in counter:
            counter[key] += int(value)
        else:
            counter[key] = int(value)
    return sorted([(key, counter[key]) for key in counter])


def pregunta_01():
    data=read_texto()
    valores_columna2=[int(data[i][1]) for i in range(0,len(data))] 
    return sum(valores_columna2) 

def pregunta_02():
    data=read_texto()
    lista_columna1=[(data[i][0],1) for i in range(0,len(data))]
    map_1_unicos=reducer(sequence=lista_columna1)
    return map_1_unicos


def pregunta_03():
    data=read_texto()
    lista_columna1_2=[(data[i][0],int(data[i][1])) for i in range(0,len(data))]
    map_1_2_unicos=reducer(sequence=lista_columna1_2)
    return map_1_2_unicos

def pregunta_04():
    data=read_texto()
    lista_mes=[]
    for i in range(0,len(data)):
        lista_fecha=data[i][2].split('-')
        mes=lista_fecha[1]
        lista_mes.append((mes,1))
    map_mes=reducer(sequence=lista_mes)
    return map_mes


def pregunta_05():
    data=read_texto()
    lista_columna1_2=[(data[i][0],int(data[i][1])) for i in range(0,len(data))]
    counter = {}
    for key, value in lista_columna1_2:
        if key in counter:         
            if counter[key][0] < value:
                counter[key][0] = value
            elif counter[key][1] >value:
                counter[key][1] = value
        else:
            counter[key] = [int(value),int(value)]
    return sorted([(key, counter[key][0],counter[key][1]) for key in counter])


def pregunta_06():
    data=read_texto()
    data_texto=""
    for i in range(0,len(data)):
        data_texto+=data[i][4]+','
    lista_de_clave = list(subString.split(":") for subString in data_texto.split(","))
    #elimar la ultima posicion de el lista lista_de_claves ya que esta vacia
    lista_de_clave.pop()
    lista_de_tulas=[(lista_de_clave[i][0],lista_de_clave[i][1]) for i in range(0,len(lista_de_clave))]
    counter = {}
    for key, value in lista_de_tulas:
        value=int(value)
        if key in counter:
            if counter[key][0] > value:
                counter[key][0] = value
            elif counter[key][1] < value:
                counter[key][1] = value
        else:
            counter[key] = [int(value),int(value)]
    return sorted([(key, counter[key][0],counter[key][1]) for key in counter])


def pregunta_07():
    data=read_texto()
    counter={}
    for line in data:
        letter=line[0]
        value=int(line[1])
        if value in counter:
            counter[value].append(letter)
        else:
            counter[value]=[letter]
    return sorted([(key, value) for key, value in counter.items()])


def pregunta_08():
    data=read_texto()
    counter={}
    for line in data:
        letter=line[0]
        value=int(line[1])
        if value in counter:
            if letter not in counter[value]:
                counter[value].append(letter)
        else:
            counter[value]=[letter]
    return sorted([(key, sorted(value)) for key, value in counter.items()])


def pregunta_09():
    data=read_texto()
    data_texto=""
    for i in range(0,len(data)):
        data_texto+=data[i][4]+','
    lista_de_clave = list(subString.split(":") for subString in data_texto.split(","))
    #elimar la ultima posiciond el lista lista_de_claves ya que esta vacia
    lista_de_clave.pop()
    lista_de_tulas=[(lista_de_clave[i][0],1) for i in range(0,len(lista_de_clave))]
    cantidad=reducer(sequence=lista_de_tulas)
    return {cantidad[i][0]:cantidad[i][1] for i in range(len(cantidad))}


def pregunta_10():
    data=read_texto()
    counter=[]
    for i in range(0,len(data)):
        letter=data[i][0]
        cont_columna_4=len(data[i][3].split(","))
        cont_columna_5=len(data[i][4].split(","))
        counter.append((letter,cont_columna_4,cont_columna_5))
    return counter


def pregunta_11():
    data=read_texto()
    counter=[]
    for i in range(0,len(data)):
        valor_columna_2=int(data[i][1])
        columna_4=data[i][3].split(",")
        for j in columna_4:
            counter.append((j,valor_columna_2))
    cantidad=reducer(sequence=counter)
    return {cantidad[i][0]:cantidad[i][1] for i in range(len(cantidad))}

def pregunta_12():
    data=read_texto()
    counter=[]
    for i in range(0,len(data)):
        letter=data[i][0] #valor de la perimera columna
        #convertirmos la columan  5 de data.csv de jjj:12,bbb:3,ddd:9,ggg:8,hhh:2
        #a [['jjj', '12'], ['bbb', '3'], ['ddd', '9'], ['ggg', '8'], ['hhh', '2']]
        columna_4=list(subString.split(":") for subString in data[i][4].split(","))
        #recorremos las matriz columna_4 para sumar los valores de cada de la segunda columna
        suma_columna_4=sum([int(columna_4[j][1]) for j in range(len(columna_4))])
        #se agrega a counter un tupla con el la letra y la suma de la columna 4
        counter.append((letter,suma_columna_4))
    #se llama a reducer para que cuente las cpincidencias
    cantidad=reducer(sequence=counter)
    #reducer de vuelve una lista de tupla asi que convertimos esa lista en un dicc y retornamos 
    return {cantidad[i][0]:cantidad[i][1] for i in range(len(cantidad))}
