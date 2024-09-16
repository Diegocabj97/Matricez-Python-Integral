# matriz = [  [2,  4,  6,  8,  10],   # 0
#             [3,  6,  9,  12, 15],  # 1
#             [5,  10, 15, 20, 25] # 2
#         ]#   0   1   2   3    4


#for i in range(len(matriz)):
#    for j in range (len(matriz[i])):
#      
#        #Ejemplo
#        print(matriz[2][4])  # fila 2 columna 3
#        # Devuelve 20
        

def incializar_matriz( cant_filas, cant_columnas):
    matriz = []
    for _ in range(cant_filas):
        fila = [0] * cant_columnas
        matriz += [fila]
    return matriz
  
matriz_creada = incializar_matriz(5,5)


for i in range(5):
    print(f"Fila: {i+1}")
    for j in range(5):
        matriz_creada[i][j] = int(input("Ingrese un numero: "))
      
      
def mostrar_matriz(matriz_creada):
   for i in range(len(matriz_creada)):
       for j in range(len(matriz_creada[i])):
           print (matriz_creada[i][j], end= " ")
       print("")
  
#Matriz
#   [[0, 0, 0, 0, 0], 
#    [0, 0, 0, 0, 0], 
#    [0, 0, 0, 'hola', 0], 
#    [0, 0, 0, 0, 0], 
#    [0, 0, 'hola', 0, 0]]
# print(matriz_creada)



pregunta = "S"

while pregunta == "S":
    fila_seleccionada = int(input("Ingrse fila a modificar: "))
    print(matriz_creada[fila_seleccionada])
    columna_seleccionada = int(input("Ingrse columna a modificar: "))
    
    dato_ingresado = int(input("Dato a ingresar: "))
    
    
    matriz_creada[columna_seleccionada][fila_seleccionada] = dato_ingresado
    
    mostrar_matriz(matriz_creada)
    pregunta = input("Desea seguir?: ")