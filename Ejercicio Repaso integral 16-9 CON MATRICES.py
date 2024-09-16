'''
En un local de venta de zapatillas, se necesita desarrollar un programa para llevar un
registro de las compras realizadas durante toda una semana. El programa debe permitir al
usuario ingresar las compras diarias y calcular ciertas estadísticas al final de la semana.
Funcionalidades del Programa:

1. Registro de Ingresos: El usuario podrá guardar en una única matriz los ingresos
totales realizados durante cada día de la semana de un mes.

2. Análisis de Datos:
● De cada semana, determinar el día con más ingresos.
● De cada semana, Determinar el día con menos ingresos.
● Calcular el promedio de ingresos del mes.
● Calcular el total de ingresos en el mes.
● Calcular el promedio de ingresos en días laborables (de lunes a viernes) y
en días del fin de semana (sábado y domingo) de cada semana.
● Calcular la semana con la mayor variación en los ingresos respecto a la semana
anterior (Semana 4 -> Semana 1 -> Semana 2 -> Semana 3 -> Semana 4).

3. Muestra de datos: Una vez calculados todos los datos del punto 2, se deberán
imprimir en pantalla.
'''

def incializar_matriz(cant_filas, cant_columnas):
    matriz = []
    for _ in range(cant_filas):
        fila = [0] * cant_columnas
        matriz += [fila]
    return matriz
  
matriz_creada = incializar_matriz(4,7)


for i in range(4):
    print(f"Fila: {i+1}")
    for j in range(7):
        matriz_creada[i][j] = int(input("Ingrese un numero: "))
      
      
def mostrar_matriz(matriz_creada):
   for i in range(len(matriz_creada)):
       for j in range(len(matriz_creada[i])):
           print (matriz_creada[i][j], end= " ")
       print("")
  
  
mostrar_matriz(matriz_creada)
