from tkinter import *
from tkinter import messagebox

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

#-----------------------
# Frame entrada de datos
#-----------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="#5F5F5F", width=1300, height=200)
frame_entrada.place(x=20, y=20)  

#------------------
# Frame operaciones
#------------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="#5F5F5F", width=1300, height=700)
frame_operaciones.place(x=20, y=260)  

#------------------
# Frame resultados
#------------------

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="#6B6B6B", width=530, height=940)
frame_resultados.place(x=1350, y=20)  


# Bucle principal
ventana_principal.mainloop()


# NO SOY PRECOZ TEACHER