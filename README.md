
# Convertidor de Imágenes a Ícono (.ico)

Script en Python para convertir cualquier imagen en un archivo `.ico` cuadrado de **200x200 px**, ideal para iconos de aplicaciones, accesos directos y páginas web.

---

## Características

- Convierte imágenes en formatos comunes (JPG, PNG, BMP, etc.) a `.ico`.
- Redimensiona automáticamente la imagen a **200x200 píxeles**.
- El ícono generado se guarda en el mismo directorio que la imagen original.
- Interfaz por consola, amigable y a color.
- Compatible con Windows, Mac y Linux.

---

## Requisitos

- [Python 3](https://www.python.org/)
- [Pillow (PIL)](https://pypi.org/project/Pillow/)
- [Colorama](https://pypi.org/project/colorama/)

Instala las dependencias ejecutando:

```bash
pip install pillow colorama
```

---

## Uso

1. Copia el script `crear_ico.py` en tu equipo.
2. Abre una terminal en la carpeta donde esté el script.
3. Ejecuta el siguiente comando:

    ```bash
    python crear_ico.py
    ```

4. Cuando el script lo solicite, escribe o pega la **ruta completa** de la imagen que deseas convertir. Por ejemplo:  
   `C:\Users\usuario\Pictures\imagen.png` o `/home/usuario/images/logo.jpg`.

5. El archivo `.ico` será generado en el mismo directorio de la imagen original.

---

## Ejemplo de uso

```
==================================================
 CONVERTIDOR DE IMÁGENES A ICONO (.ico) - v1.0
==================================================

Este script convierte cualquier imagen a formato .ico (200x200 px)
Ideal para crear iconos de aplicaciones, páginas web, accesos directos, etc.
Solo debes ingresar la ruta de tu imagen (JPG, PNG, BMP, etc).
→ El icono se guardará en el mismo directorio que la imagen original.

Introduce la ruta de la imagen: C:\Users\usuario\Pictures\logo.png

¡Icono creado con éxito: C:\Users\usuario\Pictures\logo.ico !
```

---

## Notas

- Si ingresas una carpeta o una ruta incorrecta, el script te mostrará un mensaje de error y podrás intentarlo de nuevo.
- El script limpia la pantalla automáticamente al iniciar para mejorar la experiencia visual.
- Se usan colores en la consola para mayor claridad. Si no ves colores, prueba otra terminal compatible (CMD, PowerShell, Terminal de VSCode, etc.).

---

## Autor

Creado por [Tu Nombre o Alias]JESÚS ENRIQUE CARRANZA GONZÁLEZ.

