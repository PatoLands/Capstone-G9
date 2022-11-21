# import csv
# import generador_calidad
# 
# ruta = "q_lt_lluvia_esperada.csv"
# q_esperado = []
# q_generador = []
# with open(ruta, "r") as archivo:
#     lineas = archivo.readlines()
#     lineas.pop(0)
#     for linea in lineas:
#         datos = linea.strip()
#         datos = datos.split(";")
#         lote = datos.pop(0)
#         lote = float(lote.split("_")[1])
#         datos2 = []
#         for elem in datos:
#             datos2.append(float(elem))
#         q_generador.append([lote]+datos2)
#         q_esperado.append(datos2)
# q = generador_calidad.simulador_rodante(q_generador, 60)
# for i in range(len(q)):
#     q[i] = q[i][1:]
# 
# print(q[0])
# print(q[10])
# print(q[100])

print("Modelo E3_pt2.lp")
parte = 2
print(f"Modelo E3_pt{parte}.lp")