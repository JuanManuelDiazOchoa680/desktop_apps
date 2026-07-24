from tkinter import messagebox
import math
from tkinter import *



ventana_principal = Tk()

ventana_principal.title("app")
ventana_principal.geometry("1366x768") 
ventana_principal.config(bg="#EEEEEE")
ventana_principal.resizable(0, 0)

Frame_1 = Frame(ventana_principal, bg="#FFFFFF")
Frame_1.place(x=0, y=0, width=1366, height=170)

Frame_2 = Frame(ventana_principal, borderwidth=1, relief="solid", bg="#DADADA")
Frame_2.place(x=290, y=190, width=875, height=200)




# Titulo tipo texto
titulo = Label(ventana_principal, text="Resolvedor de ecuaciones cuadráticas",bg="#FFFFFF", fg="#000000", font=("Courier New", 30))
titulo.pack(expand=True)
titulo.place(x=300, y=20)

# ecuacion ejemplo
ecuacion_ejemplo = Label(ventana_principal, text="ax² + bx + c = 0",bg="#FFFFFF", fg="#000000", font=("Courier New", 20))
ecuacion_ejemplo.pack(expand=True)
ecuacion_ejemplo.place(x=550, y=80)

#zona de coeficientes

coeficiente = Label(ventana_principal, text="COEFICIENTES", bg="#DADADA", fg="#000000", font=("Courier New", 10))
coeficiente.place(x=300, y=180)





ventana_principal.mainloop()