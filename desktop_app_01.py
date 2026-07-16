from tkinter import *


# ventana
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Sistemas Guanenta")

# tamaño de la ventana
ventana_principal.geometry("1920x1080")   

# color de fondo (hexadecimal)
ventana_principal.config(bg="#000000")

# quitar tamaño grande predefinido en ventana
ventana_principal.resizable(0, 0)


# imagenes importadas
image = PhotoImage(file="among_us.png")

image_import = Label(ventana_principal, image=image, bg="#000000")
image_import.pack()

escudo_colegio = PhotoImage(file="escudoColegio.png")
escudo_colegio_import = Label(ventana_principal, image=escudo_colegio, bg="#000000")
escudo_colegio_import.pack()

# mover imagen con teclas WASD manteniendo presionada la tecla
def mover_imagen(event):
    if event.keysym == "w":
        image_import.place(y=image_import.winfo_y() - 15)
    elif event.keysym == "s":
        image_import.place(y=image_import.winfo_y() + 15)
    elif event.keysym == "a":
        image_import.place(x=image_import.winfo_x() - 15)
    elif event.keysym == "d":
        image_import.place(x=image_import.winfo_x() + 15)

ventana_principal.bind("<Key>", mover_imagen)
image_import.place(x=750, y=500)
escudo_colegio_import.place(x=10, y=10)


# Bucle principal
ventana_principal.mainloop()


# NO SOY PRECOZ TEACHER