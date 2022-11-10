import random
import numpy as np
import statistics

random.seed(10)

parametros = {}
with open("parabolas.csv", "r") as parabolas:
    data = parabolas.readlines()
    data.pop(0)
    for linea in data:
        linea = linea.strip().split(";")
        parametros[linea[0]] = (linea[1:])
# print(parametros)

nu = {1:0.02, 2:0.015, 3:0.02, 4:0.03, 5:0.03, 6:0.025, 7:0.01, 8:0.015}
# print(nu[1])

lotes = {}
with open("lotes.csv", "r") as archivo:
    data = archivo.readlines()
    for linea in data:
        linea = linea.strip().split(";")
        lotes[linea[0]] = (linea[1:])
# print(lotes)

def calidad(lote):
    j = lotes[lote][0]
    key = "J" + str(j)
    calidad = []
    for t in range(-7, 8):
        qjt = round((float(parametros[key][0]) * t ** 2 + float(parametros[key][1]) * t + 1), 4)
        qjt = max(qjt, 0.0)
        if qjt > 1:
            qjt = 1.0
        calidad.append(qjt)
    return calidad

def calidad_lluvia(lote):
    j = lotes[lote][0]
    key = "J" + str(j)
    plls = float(lotes[lote][3]) * 0.9
    pllll = float(lotes[lote][4]) * 0.9
    nu1 = nu[int(lotes[lote][0])]

    evento2 = []
    evento3 = []
    calidad = []

    estado = 1
    for t in range(-7, 8):
        qjt = round((float(parametros[key][0]) * t ** 2 + float(parametros[key][1]) * t + 1) * (1 - nu1 * sum(evento2)), 4)
        qjt = max(qjt, 0.0)
        if qjt > 1:
            qjt = 1.0
        if sum(evento3) >= 1:
            qjt = 0.0
        calidad.append(qjt)

        #cambios de estado
        if estado == 1:
            proba_x = plls
        elif estado == 2:
            proba_x = pllll

        proba = random.random()
        if proba < proba_x:
            proba2 = random.random()
            if proba2 < 0.1:
                estado = 2
                evento2.append(1)
                evento3.append(1)
            else:
                estado = 2
                evento2.append(1)
                ultimos_6_dias = evento2[-6:]
                if sum(ultimos_6_dias) >= 4:
                    evento3.append(1)
                else:
                    evento3.append(0)
        else:
            estado = 1
            evento2.append(0)
            ultimos_6_dias = evento2[-6:]
            if sum(ultimos_6_dias) >= 4:
                evento3.append(1)
            else:
                evento3.append(0)

        ultimos_3_dias = evento2[-3:]
        if sum(ultimos_3_dias) == 0:
            evento2 = []
    return calidad

def calidad_lluvia_esperada(lote):
    datax = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    data = []
    for i in range(1000):
        q = calidad_lluvia(lote)
        for t in range(15):
            datax[t].append(q[t])
    for t in range(15):
        data.append(statistics.mean(datax[t]))
    return data

def lista_de_ceros(lista, n):
    for i in range(n):
        lista.append("0")
    return lista

#with open("q_lt_lluvia_esperada.csv", "a") as archivo:
#    linea = "Lote"
#    r = 180
#    for i in range(1, r):
#        linea += ";" + str(i)
#    archivo.write(linea + "\n")
#    for lote in lotes:
#        opt = int(lotes[lote][2])
#        qlt = []
#        qlt = lista_de_ceros(qlt, opt - 8)
#        for q in calidad_lluvia_esperada(lote):
#            qlt.append(str(q))
#        qlt = lista_de_ceros(qlt, r - 8 - opt)
#        linea = lote + ";" + ";".join(qlt) + "\n"
#        archivo.write(linea)

def simular(lista, lote, t):
    # lista es esperado
    lista_simulada = [lote]
    if np.count_nonzero(lista[:t+1]) == 0:
        # no se simula nada
        for x in range(len(lista)):
            lista_simulada.append(lista[x])
        return lista_simulada
    elif np.count_nonzero(lista[:t+1]) > 0 and np.count_nonzero(lista[t+1:]) == 0:
        # se simula todo
        q = calidad_lluvia(lote)
        for x in range(len(lista)):
            if lista[x] == 0:
                lista_simulada.append(lista[x])
            else:
                lista_simulada.append(q.pop(0))
        return lista_simulada
    else:
        # se simula y se ajusta
        perdida = False
        q = calidad_lluvia(lote)
        for x in range(len(lista)):
            if lista[x] == 0:
                lista_simulada.append(lista[x])
            else:
                if x < t:
                    qt = q.pop(0)
                    if qt == 0:
                        perdida = True  
                    lista_simulada.append(qt)
                elif x == t:
                    qt = q.pop(0)
                    dif = qt - lista[x]
                    lista_simulada.append(qt)
                elif x > t:
                    if perdida == False:
                        lista_simulada.append(lista[x] + dif)
                    else:
                        lista_simulada.append(0)
        return lista_simulada

def simulador_rodante(q, t):
    q_rh = []
    for linea in q:
        lote = linea[0]
        linea2 = linea[1:]
        q_sim = simular(linea2, lote, t)
        q_rh.append(q_sim)
    return q_rh

ruta = "q_lt_lluvia_esperada.csv"
q = []
with open(ruta, "r") as archivo:
    lineas = archivo.readlines()
    lineas.pop(0)
    for linea in lineas:
        datos = linea.strip()
        datos = datos.split(";")
        datos2 = []
        for k in range(len(datos)):
            if k == 0:
                datos2.append(datos[k])
            else:
                datos2.append(float(datos[k]))
        q.append(datos2)

qqq = simulador_rodante(q, 81)
for elem in qqq:
    print(elem)


