from tkinter import messagebox
import math
from tkinter import *
import tkinter as tk



ventana_principal = Tk()

ventana_principal.title("app")
ventana_principal.geometry("1366x768") 
ventana_principal.config(bg="#EEEEEE")
ventana_principal.resizable(0, 0)

#----------------
# zona de Frame's
#----------------

Frame_1 = Frame(ventana_principal, bg="#FFFFFF")
Frame_1.place(x=0, y=0, width=1366, height=170)

Frame_2 = Frame(ventana_principal, borderwidth=1, relief="solid", bg="#F3F3F3")
Frame_2.place(x=60, y=190, width=400, height=300)

Frame_2 = Frame(ventana_principal, borderwidth=1, relief="solid", bg="#F3F3F3")
Frame_2.place(x=500, y=190, width=800, height=550)


#----------------
# zona de Entry's
#----------------

coeficiente_a = Entry(ventana_principal, justify=tk.CENTER, bg="#FFFFFF", fg="#000000", font=("Courier New", 12), highlightthickness=0)
coeficiente_a.place(x=270, y=230, width=150, height=50)

coeficiente_b = Entry(ventana_principal, justify=tk.CENTER, bg="#FFFFFF", fg="#000000", font=("Courier New", 12), highlightthickness=0)
coeficiente_b.place(x=270, y=310, width=150, height=50)

coeficiente_c = Entry(ventana_principal, justify=tk.CENTER, bg="#FFFFFF", fg="#000000", font=("Courier New", 12), highlightthickness=0)
coeficiente_c.place(x=270, y=390, width=150, height=50)

#----------------
# zona de Label's
#----------------

# Titulo tipo texto
titulo = Label(ventana_principal, text="Resolución de ecuaciones cuadráticas",bg="#FFFFFF", fg="#000000", font=("Courier New", 30))
titulo.pack(expand=True)
titulo.place(x=250, y=20)

# ecuacion ejemplo
ecuacion_ejemplo = Label(ventana_principal, text="ax² + bx + c = 0",bg="#FFFFFF", fg="#000000", font=("Courier New", 20))
ecuacion_ejemplo.pack(expand=True)
ecuacion_ejemplo.place(x=550, y=80)

#zona de coeficientes
coeficiente = Label(ventana_principal, borderwidth=1, relief="solid", text="COEFICIENTES", bg="#F3F3F3", fg="#000000", font=("Courier New", 10))
coeficiente.place(x=75, y=180)

#coeficiente a, b, c texto
coeficiente_a_text = Label(ventana_principal, text="Coeficiente A:", bg="#F3F3F3", fg="#000000", font=("Courier New", 13))
coeficiente_a_text.place(x=100, y=240)

coeficiente_b_text = Label(ventana_principal, text="Coeficiente B:", bg="#F3F3F3", fg="#000000", font=("Courier New", 13))
coeficiente_b_text.place(x=100, y=320)

coeficiente_c_text = Label(ventana_principal, text="Coeficiente C:", bg="#F3F3F3", fg="#000000", font=("Courier New", 13))
coeficiente_c_text.place(x=100, y=400)

# zona de resultados
resultados = Label(ventana_principal, borderwidth=1, relief="solid", text="RESULTADOS", bg="#F3F3F3", fg="#000000", font=("Courier New", 10))
resultados.place(x=515, y=180)

#-----------------
# zona de Button's
#-----------------

def calcular_raices():
	try:
		a = float(coeficiente_a.get())
		b = float(coeficiente_b.get())
		c = float(coeficiente_c.get())
	except ValueError:
		messagebox.showerror("Error", "Ingrese valores numéricos para a, b, c")
		return
	if a == 0:
		messagebox.showerror("Error", "El coeficiente 'a' no puede ser 0")
		return
	d = b*b - 4*a*c
	if d > 0:
		r1 = (-b + math.sqrt(d)) / (2*a)
		r2 = (-b - math.sqrt(d)) / (2*a)
		message = f"Raíces reales y distintas:\nR1 = {r1}\nR2 = {r2}"
	elif d == 0:
		r = -b / (2*a)
		message = f"Raíz real doble:\nR = {r}"
	else:
		# raíces complejas
		real = -b / (2*a)
		imag = math.sqrt(abs(d)) / (2*a)
		message = f"Raíces complejas:\nR1 = {real} + {imag}i\nR2 = {real} - {imag}i"
	messagebox.showinfo("Resultados", message)

calcular_raiz = Button(ventana_principal, text="Calcular raíces", command=calcular_raices, bg="#2483FF", fg="#FFFFFF", font=("Courier New", 17))
calcular_raiz.place(x=60, y=500, width=400, height=110)

#-----------------------------
# RESULTADOS VARIABLES X1 Y X2
#-----------------------------



ventana_principal.mainloop()