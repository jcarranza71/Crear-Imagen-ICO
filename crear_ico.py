from PIL import Image
import os
from colorama import init

# Inicializa colorama para que funcione en Windows
init(autoreset=True)  # Así los colores se resetean automáticamente

CYAN    = "\033[96m"
MAGENTA = "\033[95m"
YELLOW  = "\033[93m"
GREEN   = "\033[92m"
RED     = "\033[91m"
RESET   = "\033[0m"

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def presentacion():
    print(CYAN + "="*50 + RESET)
    print(CYAN + " CONVERTIDOR DE IMÁGENES A ICONO (.ico) - v1.0" + RESET)
    print(CYAN + "="*50 + RESET)
    print()
    print("Este script en PYTHON convierte cualquier imagen a formato .ico (200x200 px)")
    print("Ideal para crear iconos de aplicaciones, páginas web, accesos directos, etc.")
    print("Solo debes ingresar la ruta de tu imagen (JPG, PNG, BMP, etc).")
    print("→ El icono se guardará en el mismo directorio que la imagen original.")
    print()

def convertir_a_ico(ruta_imagen):
    try:
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((200, 200), Image.LANCZOS)
        directorio = os.path.dirname(ruta_imagen)
        nombre_base = os.path.splitext(os.path.basename(ruta_imagen))[0]
        ruta_ico = os.path.join(directorio, f"{nombre_base}.ico")
        imagen.save(ruta_ico, format='ICO')
        print(GREEN + f"\n¡Icono creado con éxito: {ruta_ico} !" + RESET)
    except PermissionError:
        print(RED + "¡Error! No tienes permisos para abrir ese archivo o es un directorio." + RESET)
    except FileNotFoundError:
        print(RED + "¡Error! Archivo no encontrado. Verifica la ruta e inténtalo de nuevo." + RESET)
    except Exception as e:
        print(RED + f"Ocurrió un error: {e}" + RESET)

if __name__ == "__main__":
    limpiar_pantalla()
    presentacion()
    while True:
        ruta_imagen = input(YELLOW + "Introduce la ruta de la imagen: " + RESET)
        if os.path.isfile(ruta_imagen):
            convertir_a_ico(ruta_imagen)
            break
        else:
            print(RED + "La ruta proporcionada no es un archivo válido. Inténtalo de nuevo." + RESET)
            print()

