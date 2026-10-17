
import os
import tkinter as tk
from tkinter import filedialog, messagebox

TEXTO = "_spotdown.org"

def elegir_carpeta():
    carpeta = filedialog.askdirectory(
        title="Selecciona la carpeta"
    )
    if not carpeta:
        return

    cambios = []
    conflictos = []

    for nombre in os.listdir(carpeta):
        ruta = os.path.join(carpeta, nombre)

        if not os.path.isfile(ruta) or TEXTO not in nombre:
            continue

        nuevo_nombre = nombre.replace(TEXTO, "")
        destino = os.path.join(carpeta, nuevo_nombre)

        if os.path.exists(destino):
            conflictos.append(nombre)
            continue

        cambios.append((ruta, destino))

    if not cambios and not conflictos:
        messagebox.showinfo(
            "Resultado",
            "No se encontraron archivos con ese texto."
        )
        return

    if not messagebox.askyesno(
        "Confirmar",
        f"Se renombrarán {len(cambios)} archivos.\n"
        f"Conflictos omitidos: {len(conflictos)}.\n\n"
        "¿Continuar?"
    ):
        return

    renombrados = 0

    for origen, destino in cambios:
        try:
            os.rename(origen, destino)
            renombrados += 1
        except OSError:
            pass

    messagebox.showinfo(
        "Terminado",
        f"Archivos renombrados: {renombrados}\n"
        f"Conflictos omitidos: {len(conflictos)}"
    )

ventana = tk.Tk()
ventana.title("Eliminar _spotdown.org")
ventana.geometry("360x170")
ventana.resizable(False, False)

tk.Label(
    ventana,
    text="Eliminar _spotdown.org de los nombres",
    wraplength=330,
    font=("Segoe UI", 11, "bold")
).pack(pady=20)

tk.Button(
    ventana,
    text="Seleccionar carpeta y renombrar",
    command=elegir_carpeta
).pack(pady=10)

ventana.mainloop()
