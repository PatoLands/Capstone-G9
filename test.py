import csv
import generador_calidad

parte = 7

ruta = "q_lt_lluvia_esperada.csv"
q_generador = []
with open(ruta, "r") as archivo:
    lineas = archivo.readlines()
    lineas.pop(0)
    for linea in lineas:
        datos = linea.strip()
        datos = datos.split(";")
        lote = datos.pop(0)
        #lote = int(lote.split("_")[1])
        datos2 = []
        for elem in datos:
            datos2.append(float(elem))
        q_generador.append([lote]+datos2)
q_generado = generador_calidad.simulador_rodante(q_generador, 30+10*(parte-1))
q = q_generado
for i in range(len(q)):
    q[i] = q[i][1:]
for i in range(len(q)):
    q[i] = q[i][30:130]

with open(f"q_pt{parte}.csv", "a") as archivo:
    for i in range(len(q)):
        lote = int(q_generador[i][0].split("_")[1])
        linea = str(lote) + ";" + str(q[i]).replace(',',';').replace('.',',').strip('[').strip(']') + "\n"
        archivo.write(linea)

#print(q[0])
#print(q[10])
#print(q[100])
