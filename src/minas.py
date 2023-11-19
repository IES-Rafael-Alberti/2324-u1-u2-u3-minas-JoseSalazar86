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
def revelarCelda():
    '''
    celdaVacia = ""
    mina ="*"
    numero = 0
    '''
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
    while True:
        imprimirTablero(tableroInicial)
        print("Elige una acción:")
        print("1. Revelar celda")
        print("2. Marcar celda")
        print("3. Salir")

        eleccion = input("Tu elección: ")

        if eleccion == '1':
            fila, columna = map(int, input("Ingresa coordenadas (fila, columna): ").split(','))
            if revelarCelda(tablero, fila, columna, celdas_reveladas):
                print("¡Has encontrado una mina! ¡Juego terminado!")
                break
            if verificar_victoria(tablero, celdas_reveladas, minas):
                print("¡Felicidades! Has despejado la isla sin detonar ninguna mina. ¡Victoria!")
                break
        elif eleccion == '2':
            fila, columna = map(int, input("Ingresa coordenadas (fila, columna): ").split(','))
            marcar_celda(tablero, fila, columna, celdas_marcadas)
        elif eleccion == '3':
            print("¡Adiós! Gracias por jugar.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
    tableroInicial = iniciaTablero(8, 8)
    rellenarMinas(tableroInicial)
    numeros(tableroInicial)
    
if __name__ == "__main__":
    """
    Esta sección del código se ejecuta solo si ejecutamos este archivo directamente.
    """
    jugar()
   