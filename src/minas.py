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
def celdasVacias(fila, columna, tablero, celdasReveladas):
    '''
    Las celdas sin minas ni números adyacentes son "vacías".
    '''
    if (fila, columna) not in celdasReveladas:
        return tablero[fila][columna] == '.'
    return False

def revelarCelda(fila, columna, tableroInicial, celdasReveladas):
    if (fila, columna) in celdasReveladas:
        # La celda ya ha sido revelada, no se puede revelar de nuevo
        return "revelada"

    celda = tableroInicial[fila][columna]

    if celda == '*':
        # La celda contiene una mina, el juego termina
        return "mina"
    elif celda.isdigit():
        # La celda contiene un número, se muestra el número
        celdasReveladas.add((fila, columna))
        return "numero"
    elif celda == '.':
        # La celda está vacía, se revelan las celdas adyacentes vacías
        celdasReveladas.add((fila, columna))
        numeros(fila, columna, tableroInicial, celdasReveladas)
        return "vacia"
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


def verificarVictoria(tablero, celdasReveladas):
    """
    Verifica si el jugador ha despejado todas las celdas sin minas.
    """
    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            if tablero[fila][columna] != '*' and (fila, columna) not in celdasReveladas:
                return False
    return True
def jugar():
    """
    Esta función ejecuta el juego.

    """
    filas, columnas = 8, 8
    tablero = iniciaTablero(filas, columnas)
    rellenarMinas(tablero)
    
    while True:
        imprimirTablero(tablero)
        print("Elige una acción:")
        print("1. Revelar celda")
        print("2. Marcar celda")
        print("3. Salir")

        eleccion = input("Tu elección: ")

        if eleccion == "1":
            fila, columna = map(int, input("Ingresa coordenadas (fila, columna): ").split(","))
            resultado = revelarCelda(fila - 1, columna - 1, tablero)
            if resultado == "mina":
                print("¡Has encontrado una mina! ¡Juego terminado!")
                break
            elif resultado == "victoria":
                print("¡Felicidades! ¡Has despejado todas las celdas sin detonar ninguna mina!")
                break
        elif eleccion == "2":
            # Implementar lógica para marcar celdas
            pass
        elif eleccion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("¡Esa no es una opción válida! Inténtalo de nuevo.")
    
if __name__ == "__main__":
    """
    Esta sección del código se ejecuta solo si ejecutamos este archivo directamente.
    """
    jugar()
   