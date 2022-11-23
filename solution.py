import csv
parte = 6
with open(f'Solucion_E3_pt{parte}.sol', newline='\n') as csvfile:
    reader = csv.reader((line.replace('  ', ' ') for line in csvfile), delimiter=' ')
    next(reader)  # skip header
    sol = {}
    variables = 0
    for var, value in reader:
        variables += 1
        if float(value) != 0:
            sol[var] = float(value)
    #print(len(sol))
print(variables)
print()

with open(f"solution_pt{parte}.csv", "a") as archivo:
    for key in sol:
        linea = str(key) + ";" + str(sol[key]).replace('.',',') + "\n"
        archivo.write(linea)


def extract_variable(var):
    for i in range(len(var)):
        if var[i] == "_":
            return var[:i]

# Guardar variables
v = []
gamma = []
z = []
alpha = []
wC = []
wE = []
for key in sol:
    key2 = extract_variable(key)
    if key2 == "v":
        v.append(key)
    if key2 == "gamma":
        # gamma = m^3 de vino = 1000 litros de vino = 1000/0.75 botellas
        botellas = (sol[key] * 1000) / 0.75
        elem = [key, round(botellas, 4)]
        gamma.append(elem)
    if key2 == "z":
        z.append([key, sol[key]])
    if key2 == "alpha":
        alpha.append([key, sol[key]])
    if key2 == "wC":
        wC.append([key, sol[key]])
    if key2 == "wE":
        wE.append([key, sol[key]])

# Calculo de azucar
print("USO DE ÁZUCAR:")
TL = [0, 72.5, 172.5, 150.0, 56.25, 81.25, 50.0, 186.25, 147.5, 100.0, 36.25, 185.0, 137.5, 182.5, 166.25, 33.75, 167.5, 178.75, 82.5, 152.5, 75.0, 142.5, 140.0, 87.5, 121.25, 56.25, 147.5, 56.25, 127.5, 95.0, 33.75, 102.5, 173.75, 101.25, 45.0, 113.75, 150.0, 110.0, 61.25, 53.75, 48.75, 157.5, 117.5, 36.25, 122.5, 166.25, 148.75, 75.0, 153.75, 137.5, 180.0, 137.5, 150.0, 82.5, 102.5, 186.25, 161.25, 77.5, 55.0, 162.5, 170.0, 111.25, 76.25, 51.25, 127.5, 113.75, 36.25, 166.25, 78.75, 62.5, 51.25, 162.5, 72.5, 97.5, 47.5, 103.75, 92.5, 141.25, 146.25, 128.75, 101.25, 123.75, 118.75, 177.5, 92.5, 65.0, 87.5, 175.0, 130.0, 106.25, 35.0, 152.5, 138.75, 133.75, 123.75, 71.25, 98.75, 173.75, 136.25, 42.5, 108.75, 63.75, 177.5, 181.25, 162.5, 43.75, 142.5, 122.5, 67.5, 55.0, 183.75, 167.5, 123.75, 186.25, 162.5, 143.75, 53.75, 126.25, 182.5, 52.5, 72.5, 128.75, 40.0, 96.25, 46.25, 46.25, 62.5, 62.5, 97.5, 50.0, 47.5, 66.25, 147.5, 66.25, 63.75, 125.0, 167.5, 157.5, 172.5, 138.75, 42.5, 138.75, 160.0, 42.5, 70.0, 61.25, 183.75, 92.5, 98.75, 130.0, 171.25, 65.0, 122.5, 85.0, 122.5, 111.25, 43.75, 150.0, 123.75, 60.0, 83.75, 61.25, 121.25, 32.5, 168.75, 46.25, 47.5, 146.25, 172.5, 92.5, 98.75, 43.75, 173.75, 71.25, 62.5, 172.5, 43.75, 41.25, 121.25, 47.5, 165.0, 38.75, 133.75, 143.75, 72.5, 182.5, 151.25, 106.25, 81.25, 57.5, 182.5, 176.25, 50.0, 121.25, 167.5, 142.5, 136.25, 110.0, 126.25, 102.5, 178.75, 50.0, 105.0, 101.25, 46.25, 156.25, 135.0, 155.0, 78.75, 126.25, 165.0, 181.25, 120.0, 157.5, 166.25, 125.0, 58.75, 176.25, 37.5, 138.75, 76.25, 162.5, 152.5, 167.5, 165.0, 33.75, 145.0, 37.5, 183.75, 77.5, 58.75, 100.0, 148.75, 143.75, 142.5, 56.25, 121.25, 38.75, 66.25, 88.75, 36.25, 107.5, 82.5, 166.25, 83.75, 98.75, 183.75, 122.5, 122.5, 186.25, 170.0, 42.5, 58.75, 50.0, 55.0, 176.25, 40.0, 146.25, 51.25, 42.5, 136.25, 131.25, 153.75, 78.75, 175.0, 152.5, 177.5, 182.5, 115.0, 112.5, 33.75, 61.25, 148.75, 86.25, 138.75, 127.5, 115.0, 116.25, 68.75, 148.75, 143.75, 53.75, 162.5, 92.5, 120.0, 127.5, 82.5, 62.5, 68.75, 147.5, 105.0]
AT = 27253/900

import generador_calidad
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
# ruta = "q_lt.csv"
# q = []
# with open(ruta, "r") as archivo:
#     lineas = archivo.readlines()
#     lineas.pop(0)
#     for linea in lineas:
#         datos = linea.strip()
#         datos = datos.split(";")
#         datos.pop(0)
#         datos2 = []
#         for elem in datos:
#             datos2.append(float(elem))
#         q.append(datos2)

q_v = []
azucar = 0
for elem in v:
    elem = elem.split("_")
    q_v.append(q[int(elem[1])-1][int(elem[2])-1])
    azucar += AT*TL[int(elem[1])]*(1-q[int(elem[1])-1][int(elem[2])-1])
print(q_v)
print("Lotes cosechados:", len(q_v))
print("Promedio calidad:", sum(q_v)/len(q_v))
print("Costo azucar total:", azucar)
print("Costo promedio azucar por lote:", azucar/len(q_v))
print()

# Cálculo de demanda
print("PRODUCCIÓN Y DEMANDA")

# miles de botellas demandadas por receta r
D = [0, 6123.0, 4443.0, 4599.0, 5324.0, 4380.0, 6193.0, 5256.0, 5740.0, 5913.0, 0, 5387.0, 0, 0, 6132.0, 5037.0, 0, 5475.0, 0]

# precio de venta botellas de receta r
PR = [0, 2.796, 2.029, 2.1, 2.431, 2.0, 2.828, 2.4, 2.621, 2.7, 2.7, 2.46, 2.46, 2.46, 2.8, 2.3, 2.3, 2.5, 2.5]

botellas_receta = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
botellas_planta = [[], [], [], []]
botellas_dia = []
for dia in range(162):
    botellas_dia.append([])

for elem in gamma:
    var = elem[0].split("_")
    value = elem[1]
    botellas_receta[int(var[1])].append(value)
    botellas_planta[int(var[2])].append(value)
    botellas_dia[int(var[3])].append(value)

#print(botellas_receta)
#print(botellas_planta)
#print(botellas_dia)

botellas_receta2 = []
for elem in botellas_receta:
    dato = sum(elem)
    botellas_receta2.append(dato)
#print(botellas_receta2)

botellas_planta2 = []
for elem in botellas_planta:
    dato = sum(elem)
    botellas_planta2.append(dato)
#print(botellas_planta2)

botellas_dia2 = []
for elem in botellas_dia:
    dato = sum(elem)
    botellas_dia2.append(dato)
#print(botellas_dia2)

ingresos = []
for i in range(len(botellas_receta2)):
    if i > 0 and D[i] > 0:
        print("Botellas receta", i, "producidas:", botellas_receta2[i])
        print("Porcentaje de demanda cubierto:", round(botellas_receta2[i] / (D[i] * 1000), 2))
        print()

        ingreso = botellas_receta2[i] * (PR[i] - 1.98)
        ingresos.append(ingreso)

print("Cuota de mercado:", sum(botellas_receta2) / (sum(D) * 1000))
print("Ingresos por venta:", sum(ingresos))
print()

# Uso de plantas
print("USO DE PLANTAS")

elaboracion_dia_planta = []
for dia in range(162):
    elaboracion_dia_planta.append([[0], [0], [0], [0]])

for elem in z:
    var = elem[0].split("_")
    value = elem[1]
    p = int(var[2])
    t = int(var[3])
    for k in range(9):
        # Se mantienen ocupados por los siguientes 9 días.
        elaboracion_dia_planta[t + k][p].append(value)
#print(elaboracion_dia_planta)

elaboracion_dia_planta2 = []
for dia in range(162):
    elaboracion_dia_planta2.append([[], [], [], []])

for i in range(len(elaboracion_dia_planta)):
    for j in range(4):
        elaboracion_dia_planta2[i][j].append(sum(elaboracion_dia_planta[i][j]))

with open(f"uso_de_tanques_pt{parte}.csv", "a") as archivo:
    linea = "Planta;"
    for p in range(1, 4):
        linea += str(p) + ";"
    linea += "\n"
    archivo.write(linea)
    
    linea = [[]]
    for i in range(len(elaboracion_dia_planta2)):
        if i > 0:
            linea2 = ""
            for p in range(1, 4):
                linea2 += str(elaboracion_dia_planta2[i][p][0]) + ";"
            linea2 += "\n"
            linea.append(linea2)
    
    for i in range(len(linea)):
        if i > 0:
            archivo.write(str(i) + ";" + linea[i]) 

# Tramos contratados
# Tanques x tramo
capacidades = [[], [], [], []]
TT = [[0,0,0,0,0],[0, 20, 20, 8, 4], [0, 16, 12, 8, 8], [0, 14, 16, 8, 6]]
for i in range(len(alpha)):
    var = alpha[i][0].split("_")
    value = alpha[i][1]
    capacidades[int(var[2])].append(TT[int(var[2])][int(var[1])])

for p in range(4):
    if p > 0:
        tramos = capacidades[p]
        print("Capacidad planta", str(p) + ":", sum(tramos))
print()

# Uva desechada
#print(wC)
#print(wE)
print("DESECHOS")

desechos_E = 0
desechos_C = 0

for elem in wC:
    var = elem[0].split("_")
    value = elem[1]
    desechos_C += value

for elem in wE:
    var = elem[0].split("_")
    value = elem[1]
    desechos_E += value
desechos_E *= 1000

print("Toneladas de uva desechadas en cosecha:", desechos_C)
print("litros de vino desechado en planta:", desechos_E)