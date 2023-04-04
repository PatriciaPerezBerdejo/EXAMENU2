import tkinter as tk

def iniciar_sesion():
    usuario = nombre_usuario.get()
    contrasena = contrasena_usuario.get()
    if usuario == "ADMI" and contrasena == "0123":
        resultado.config(text="Iniciaste Sesion Correctamente")
    else:
        resultado.config(text="Nombre de usuario o contraseña incorrectos")

#Define el tamaño y el color de la ventana 
ventana = tk.Tk()
ventana.title("INICIA SESION_ADMINISTRADOR")
ventana.configure(padx=130)
ventana.configure(bg="Pink")

# Crear campos de entrada para el nombre de usuario y la contraseña
nombre_usuario = tk.Entry(ventana)
nombre_usuario.pack(pady=40)
contrasena_usuario = tk.Entry(ventana, show="·")
contrasena_usuario.pack()

# Crear botones para iniciar sesión y salir
iniciar_sesion = tk.Button(ventana, text="INICIAR", command=iniciar_sesion, bg="Fuchsia")
iniciar_sesion.pack(padx=40, pady=40)
Exit = tk.Button(ventana, text="SALIR", command=ventana.quit, bg="Fuchsia")
Exit.pack()

# Crear un widget de etiqueta para mostrar el resultado del inicio de sesión
resultado = tk.Label(ventana, text="")
resultado.pack(pady=70)
ventana.mainloop()


from tkinter import *
from tkinter import colorchooser as colorchooser 

root=Tk()
root.title("Iniciar sesion_Trabajador") 
root.geometry("500x500")
root.config(bg="teal")

nombre = tk.Entry(root)
nombre.pack(pady=40)
folio = tk.Entry(root, show="*")
folio.pack()

iniciar = tk.Button(root, text="ENTAR", command=iniciar_sesion, bg="green")
iniciar.pack(padx=40, pady=40)
Exit = tk.Button(root, text="CERRAR", command=root.quit, bg="green")
Exit.pack()

poot=Tk()
poot.title("Tus Horarios") 
poot.geometry("500x500")
poot.config(bg="Black")
iniciar_sesion=poot.title
resultado = tk.Label(poot, text="Horario")
resultado.pack(pady=70)

root.mainloop()
poot.mainloop()