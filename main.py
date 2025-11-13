from colorama import Fore, Style, init
import time
import os
from colorama import Back, Style, init

# Inicializar colorama para que funcione en diferentes terminales
init()


def finland_flag(wide=25, height=15):
    """
    Crea y muestra la bandera de Finlandia en la terminal.

    """
    # Definir los colores
    white = Back.WHITE + ' '
    blue = Back.BLUE + ' '
    reset = Style.RESET_ALL

    # Calcular las dimensiones de la cruz
    wide_flag = int(wide / 20)
    height_flag = int(height / 15)

    # Imprimir la parte superior de la bandera (fondo blanco)
    for _ in range(height_flag):
        # print(white * wide + reset)
        parte_blanca = white * int((wide - wide_flag)/2)
        # Franja vertical de la cruz
        parte_azul = blue * wide_flag
        # Imprimir la línea completa
    print(parte_blanca + parte_azul + parte_blanca + reset)

    # Imprimir la franja horizontal de la cruz azul
    for _ in range(wide_flag):
       # medio= blue* int((wide-wide_flag)/2)
        # print(medio+reset)
        print(blue * wide + reset)

    # Imprimir la parte inferior de la bandera (fondo blanco y franja vertical azul)
    for _ in range(height_flag * 2):
        # Fondo blanco para los lados de la cruz
        parte_blanca = white * int((wide - wide_flag)/2)
        # Franja vertical de la cruz
        parte_azul = blue * wide_flag
        # Imprimir la línea completa
        print(parte_blanca + parte_azul + parte_blanca + reset)


# Patron

# Inicializar colorama
init(autoreset=True)


def dibujar_patron():
    """
    Dibuja un patrón de dos círculos negros sólidos.
    """
    negro = "●"  # Círculo sólido Unicode
    blanco = " "  # Espacio en blanco

    patron = [
        blanco*2 + negro*4 + blanco*2 + negro*4 + blanco*2,
        blanco*1 + negro*6 + blanco*1 + negro*6 + blanco*1,
        blanco*1 + negro*6 + blanco*1 + negro*6 + blanco*1,
        blanco*2 + negro*4 + blanco*2 + negro*4 + blanco*2,
    ]
    return "\n".join(patron) + Style.RESET_ALL


def mostrar_patron_en_columna(repeticiones=5):
    """
    Muestra el patrón repetido en forma de columna vertical.
    """

    patron = dibujar_patron()
    for _ in range(repeticiones):
        print(patron + "\n")


# GRÁFICO DE FUNCIÓN y = x/2

def grafico_funcion():
    print("GRPHIC y = x/2 \n")
    ancho = 20   # eje X
    alto = 10    # eje Y

    for y in range(alto, -1, -1):  # recorrer de arriba hacia abajo
        linea = ""
        for x in range(ancho + 1):
            if y == int(x / 2):     # punto de la función
                linea += "*"
            elif y == 0:
                linea += "_"         # eje X
            elif x == 0:
                linea += "|"         # eje Y
            else:
                linea += " "
        print(linea)
    print("\n")


# LECTURA DE ARCHIVO Y DIAGRAMA PORCENTUAL


def leer_secuencia():
    """
    Lee los datos numéricos desde sequence.txt
    usando la ruta fija proporcionada.
    """
    ruta = r"C:\Users\chavi\Downloads\Nueva carpeta\sequence.txt"

    if not os.path.exists(ruta):
        print(f"⚠️  No se encontró el archivo: {ruta}")
        return []

    with open(ruta, "r", encoding="utf-8") as f:
        return [float(line.strip()) for line in f if line.strip()]


def diagrama_porcentual(datos):
    """
    Calcula y muestra un diagrama porcentual en texto.
    Solo se consideran los números entre 5–10 y -5–-10.
    """
    if not datos:
        print("No hay datos para graficar.")
        return

    # Filtramos los datos válidos
    datos_filtrados = [x for x in datos if (5 <= x <= 10) or (-10 <= x <= -5)]

    if not datos_filtrados:
        print("⚠️  No hay números en el rango válido (5–10 o -5–-10).")
        return

    total = len(datos_filtrados)
    positivos = len([x for x in datos_filtrados if 5 <= x <= 10])
    negativos = len([x for x in datos_filtrados if -10 <= x <= -5])

    porc_positivos = positivos / total * 100
    porc_negativos = negativos / total * 100

    # Función auxiliar para crear una barra de porcentaje
    def barra(p):
        n = int(p / 2)  # Escala (50 = barra completa)
        return "█" * n + f" {p:.1f}%"

    print("\nDIAGRAM ( 5–10 y -5–-10)\n")
    print(f"Positivos: {barra(porc_positivos)}")
    print("")
    print(f"Negativos: {barra(porc_negativos)}\n")
    print("")


# EJECUCIÓN
if __name__ == "__main__":
    print("\nFINLAND FLAG\n")
    finland_flag()
    print("\nPATRON\n")
    mostrar_patron_en_columna(repeticiones=5)
    grafico_funcion()
    datos = leer_secuencia()
    diagrama_porcentual(datos)
