"""
En esta solución, se ha estructurado el código para que sea claro y fácil de seguir. 
Cada función tiene una responsabilidad específica, lo que hace que el código sea más legible 
y mantenible. Además, se han utilizado constantes para mejorar la comprensión del código y 
evitar el uso de "números mágicos" o cadenas de texto repetidas.

Notas Adicionales
La función revelar_celdas_vacias y verificar_victoria necesitan ser implementadas según las 
reglas del Buscaminas.
Este ejercicio es una excelente manera de evaluar y mejorar las habilidades de programación 
de tus alumnos, enfocándose en las estructuras de datos y el manejo de lógica básica 
en Python.

"""
import random
def iniciaTablero(filas, columnas):
    # Crear un tablero vacío
    tablero = [['.' for i in range(columnas)] for i in range(filas)]
    return tablero
def imprimirTablero(tablero):
     # Imprimir el encabezado de las columnas
    print("   " + " ".join([str(i) for i in range(1, len(tablero[0]) + 1)]))

    # Imprimir el tablero
    for i in range(len(tablero)):
        # Imprimir el número de fila
        print(f"{i + 1} ", end=' ')

        # Imprimir cada celda del tablero
        for j in range(len(tablero[0])):
            print(tablero[i][j], end=' ')

        print()  # Nueva línea para la siguiente fila

    return tablero
def rellenarMinas(tableroInicial):
    '''
    numero de mimas son 10
    '''
    for i in range(10):
        tableroInicial[random.randint(0, 7)][random.randint(0, 7)] = '*'
def celdasVacias():
    '''
    Las celdas sin minas ni números adyacentes son "vacías".
    '''
def revelarCelda(fila,columna,tableroInicial):
    '''
    celdaVacia = ""
    mina ="*"
    numero = 0
    '''
    if tableroInicial[fila][columna] =='.':
        numeros(fila,columna)
def numeros(tableroInicial):
    '''
    Las celdas sin minas muestran el número de minas en las celdas adyacentes.
    '''
    for i in range(len(tableroInicial)):
        for j in range(len(tableroInicial[0])):
            # Verificar que la celda está dentro de los límites y es vacía
            if 0 <= j < 8 and 0 <= i < 8 and tableroInicial[i][j] == '.':
                numeroMinas = 0
                posicionesAdyacentes = [
                    (-1, -1), (-1, 0), (-1, 1),
                    (0, -1),           (0, 1),
                    (1, -1), (1, 0), (1, 1)
                ]
                # Iterar sobre las posiciones adyacentes
                for desplazamientoFila,desplazamientoColumna in posicionesAdyacentes:
                    numeroFila, numeroColumna = i + desplazamientoFila, j + desplazamientoColumna
                    # Verificar que la posición adyacente está dentro de los límites
                    if 0 <= numeroFila < len(tableroInicial) and 0 <= numeroColumna < len(tableroInicial[0]):
                        # Verificar si la celda adyacente contiene una mina
                        if tableroInicial[numeroFila][numeroColumna] == '*':
                            numeroMinas += 1

                # Asignar el número de minas a la celda actual
                tableroInicial[i][j] = str(numeroMinas)



def jugar():
    """
    Esta función ejecuta el juego.

    """
    
    
if __name__ == "__main__":
    """
    Esta sección del código se ejecuta solo si ejecutamos este archivo directamente.
    """
    jugar()
   