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


def iniciaTablero(filas, columnas, valorInicial):
    return [[valorInicial for i in range(columnas)] for j in range(filas)]

def imprimirTablero(tablero, ocultarMina=False):
    # Imprimir el encabezado de las columnas
    print("   " + " ".join([str(i) for i in range(1, len(tablero[0]) + 1)]))

    # Imprimir el tablero
    for i in range(len(tablero)):
        # Imprimir el número de fila
        print(f"{i + 1} ", end=' ')

        # Imprimir cada celda del tablero
        for j in range(len(tablero[0])):
            if tablero[i][j] == '*' and ocultarMina:
                print('.', end=' ')  # Ocultar las minas
            else:
                print(tablero[i][j], end=' ')

        print()  # Nueva línea para la siguiente fila

def rellenarMinas(tableroMinas, cantidadMina
):
    # Número de minas son 10
    for _ in range(cantidadMina
    ):
        fila, columna = random.randint(0, 7), random.randint(0, 7)
        while tableroMinas[fila][columna] == '*':
            fila, columna = random.randint(0, 7), random.randint(0, 7)
        tableroMinas[fila][columna] = '*'

def contarMinasCercanas(tableroMinas, fila, columna):
    contador = 0
    posicionesAdyacentes = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for desplazamientoFila, desplazamientoColumna in posicionesAdyacentes:
        nuevaFila, nuevaColumna = fila + desplazamientoFila, columna + desplazamientoColumna

        if 0 <= nuevaFila < len(tableroMinas) and 0 <= nuevaColumna < len(tableroMinas[0]):
            if tableroMinas[nuevaFila][nuevaColumna] == '*':
                contador += 1

    return contador

def actualizarTableroVisible(tableroVisible, tableroMinas, fila, columna):
    if tableroMinas[fila][columna] == '*':
        # El jugador tocó una mina, juego terminado
        return "mina"
    elif tableroVisible[fila][columna] == '.':
        # La celda no ha sido revelada antes
        minas_cercanas = contarMinasCercanas(tableroMinas, fila, columna)
        tableroVisible[fila][columna] = str(minas_cercanas)

        if minas_cercanas == 0:
            # Si la celda es vacía, revelar celdas adyacentes
            revelarCeldasAdyacentes(tableroVisible, tableroMinas, fila, columna)

        return "continuar"
    else:
        # La celda ya ha sido revelada
        return "revelada"

def revelarCeldasAdyacentes(tableroVisible, tableroMinas, fila, columna):
    posicionesAdyacentes = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for desplazamientoFila, desplazamientoColumna in posicionesAdyacentes:
        nuevaFila, nuevaColumna = fila + desplazamientoFila, columna + desplazamientoColumna

        if 0 <= nuevaFila < len(tableroMinas) and 0 <= nuevaColumna < len(tableroMinas[0]):
            if tableroVisible[nuevaFila][nuevaColumna] == '.':
                minas_cercanas = contarMinasCercanas(tableroMinas, nuevaFila, nuevaColumna)
                tableroVisible[nuevaFila][nuevaColumna] = str(minas_cercanas)

                if minas_cercanas == 0:
                    # Si la celda es vacía, seguir revelando celdas adyacentes
                    revelarCeldasAdyacentes(tableroVisible, tableroMinas, nuevaFila, nuevaColumna)

def verificarVictoria(tableroVisible, tableroMinas):
    for i in range(len(tableroVisible)):
        for j in range(len(tableroVisible[0])):
            if tableroMinas[i][j] != '*' and tableroVisible[i][j] == '.':
                return False
    return True
def marcarCelda(tableroVisible, fila, columna):
    if tableroVisible[fila][columna] == '.':
        tableroVisible[fila][columna] = 'F'
        print(f"Celda en ({fila + 1}, {columna + 1}) marcada con 'F'.")
    else:
        print("La celda ya ha sido revelada. No se puede marcar.")
def jugar():
    filas, columnas = 8, 8
    cantidadMina = 10

    tableroMinas = iniciaTablero(filas, columnas, '.')
    rellenarMinas(tableroMinas, cantidadMina)

    tableroVisible = iniciaTablero(filas, columnas, '.')

    while True:
        imprimirTablero(tableroVisible)
        print("Elige una acción:")
        print("1. Revelar celda")
        print("2. Marcar celda")
        print("3. Salir")

        eleccion = input("Tu elección: ")

        if eleccion == "1":
            fila, columna = map(int, input("Ingresa coordenadas (fila, columna): ").split(","))
            resultado = actualizarTableroVisible(tableroVisible, tableroMinas, fila - 1, columna - 1)

            if resultado == "mina":
                imprimirTablero(tableroMinas, ocultarMina=False)  # Mostrar las minas
                print("¡Has encontrado una mina! ¡Juego terminado!")
                break
            elif resultado == "continuar":
                if verificarVictoria(tableroVisible, tableroMinas):
                    imprimirTablero(tableroMinas, ocultarMina=False)  # Mostrar las minas
                    print("¡Felicidades! ¡Has despejado todas las celdas sin detonar ninguna mina!")
                    break
        elif eleccion == "2":
            fila, columna = map(int, input("Ingresa coordenadas (fila, columna) para marcar con 'F': ").split(","))
            marcarCelda(tableroVisible, fila - 1, columna - 1)
        elif eleccion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("¡Esa no es una opción válida! Inténtalo de nuevo.")

if __name__ == "__main__":
    jugar()