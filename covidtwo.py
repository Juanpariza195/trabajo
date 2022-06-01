# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 17:43:27 2022

@author: DELL3467
"""

# 20. Liste de mayor a menor el número de contagiados por país de procedencia
data['Nombre del país'].replace('VENEUELA', 'VENEZUELA', inplace=True)
data['Nombre del país'].replace('MEXICO', 'MÉXICO', inplace=True)

pais = data['Nombre del país'].value_counts()
print(f'\n{pais}')


# 21. Liste de mayor a menor las fechas donde se presentaron mas contagios
fech_contagio = data.groupby(
    ['Fecha de diagnóstico']).size().sort_values(ascending=False)
print(f'\n{fech_contagio}')


# 22. Diga cual es la tasa de mortalidad y recuperación que tiene Colombia
mortalidad = (len(data[data['Estado'] == 'Fallecido']) / len(data)) * 100
recuperacion = (len(data[data['Recuperado'] == 'Recuperado']) / len(data)) * 100
print('\nTasa de mortalidad: ', "{:.2f}".format(mortalidad))
print('\nTasa de recuperacion: ', "{:.2f}".format(recuperacion))


# 23. Liste la tasa de mortalidad y recuperación que tiene cada departamento

# 24. Liste la tasa de mortalidad y recuperación que tiene cada ciudad

# 25. Liste por cada ciudad la cantidad de personas por atención
aten = data.groupby(['Nombre municipio', 'Ubicación del caso']).size()
print(f'\n{aten}')


# 26. Liste el promedio de edad por sexo por cada ciudad de contagiados
prom_edad_sexo = data.groupby(['Nombre municipio', 'Sexo']).Edad.mean()
print(f'\n{prom_edad_sexo}')


# 27. Grafique las curvas de contagio, muerte y recuperación de toda Colombia acumulados
data['Sexo'].replace('f', 'F', inplace=True)
data['Sexo'].replace('m', 'M', inplace=True)
data['Estado'].replace('LEVE', 'Leve', inplace=True)
data['Estado'].replace('leve', 'Leve', inplace=True)

contg = data.groupby('Fecha de diagnóstico').size(
).sort_values().plot(figsize=(15, 4))
print('\nCurva de Contagios')
plt.show(contg)

falle = data[data['Recuperado'] == 'fallecido'].groupby(
    'Fecha de diagnóstico').size().sort_values().plot(figsize=(15, 4))
print('\nCurva de Fallecidos')
plt.show(falle)

recup = data[data['Recuperado'] == 'Recuperado'].groupby(
    'Fecha de diagnóstico').size().sort_values().plot(figsize=(15, 4))
print('\nCurva de Recuperados')
plt.show(recup)


# 28. Grafique las curvas de contagio, muerte y recuperación de los 10
# departamentos con mas casos de contagiados acumulados
curv_contg_depar = data.groupby('Nombre departamento').size(
).sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 departamentos con mas contagios')
plt.show(curv_contg_depar)

curv_falle_depar = data[data['Recuperado'] == 'fallecido'].groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 departamentos con mas personas fallecidas')
plt.show(curv_falle_depar)

curv_recu_depar = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 departamentos con mas personas recuperadas')
plt.show(curv_recu_depar)


# 29. Grafique las curvas de contagio, muerte y recuperación de las 10
# ciudades con mas casos de contagiados acumulados
curv_contg_munic = data.groupby('Nombre municipio').size(
).sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 municipios con mas contagios')
plt.show(curv_contg_munic)

curv_falle_munic = data[data['Recuperado'] == 'fallecido'].groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 municipios con mas personas fallecidas')
plt.show(curv_falle_munic)

curv_recu_munic = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 municipios con mas personas recuperadas')
plt.show(curv_recu_munic)


# 30. Liste de mayor a menor la cantidad de fallecidos por edad en toda Colombia.
edad_falle = data[data['Estado'] == 'Fallecido'].groupby(['Edad']).size().sort_values(ascending=False)
print(f'\n{edad_falle}')


# 31. Liste el porcentaje de personas por atención de toda Colombia
porcen_atenc = ((data.groupby('Ubicación del caso').size().sort_values(ascending = False)) / ((data.groupby('Ubicación del caso').size().sort_values(ascending = False)).sum())) * 100
print(f'\n {porcen_atenc}')


# 32. Haga un gráfico de barras por atención de toda Colombia
graf_atenc = data['Ubicación del caso'].value_counts().plot.bar()
print('\nGrafico de barras segun su tipo de atencion')


# 33. Haga un gráfico de barras por Sexo de toda Colombia
graf_sexo = data['Sexo'].value_counts().plot.bar()
print('\nGrafico de barras por sexo en Colombia')


# 34. Haga un gráfico de barras por tipo de contagio de toda Colombia
graf_tip_contag = data['Tipo de contagio'].value_counts().plot.bar()
print('\nGrafico de barras por tipo de contagio en Colombia')


# 35. Haga un gráfico de barras del número de contagiados, recuperados y fallecidos por fecha de toda Colombia
graf_contg = data.groupby('Fecha de diagnóstico').size().sort_values().plot.bar(figsize=(15, 4))
print('\nGrafico de barras de fecha de contagiados')
plt.show(graf_contg)

graf_recup = data[data['Recuperado'] == 'Recuperado'].groupby('Fecha de diagnóstico').size().sort_values().plot.bar(figsize=(15, 4))
print('\nGrafico de barras de fecha de los recuperados')
plt.show(graf_recup)

graf_falle = data[data['Estado'] == 'Fallecido'].groupby('Fecha de diagnóstico').size().sort_values().plot.bar(figsize=(15, 4))
print('\nGrafico de barras de fecha de los fallecidos')
plt.show(graf_falle)