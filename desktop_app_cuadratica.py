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

Frame_1 = tk.Frame(ventana_principal, bg="#FFFFFF")
Frame_1.place(x=0, y=0, width=1366, height=170)

Frame_2 = tk.Frame(ventana_principal, borderwidth=1, relief="solid", bg="#F3F3F3")
Frame_2.place(x=60, y=190, width=400, height=300)

Frame_3 = tk.Frame(ventana_principal, borderwidth=1, relief="solid", bg="#F3F3F3")
Frame_3.place(x=500, y=190, width=800, height=550)

imagen_cuadratica = tk.PhotoImage(file="cuadratica.png")
label_imagen = tk.Label(Frame_3, image=imagen_cuadratica, bg="#F3F3F3")
label_imagen.image = imagen_cuadratica
label_imagen.place(x=0, y=0, width=457, height=457)


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

# Labels para desplegar x1 y x2 en la pantalla
lbl_tipo_raiz = Label(ventana_principal, text="", bg="#F3F3F3", fg="#000000", font=("Courier New", 10, "bold"), anchor="w")
lbl_tipo_raiz.place(x=540, y=700, width=720)

lbl_x1 = Label(ventana_principal, text="x1 = ", bg="#F3F3F3", fg="#000000", font=("Courier New", 13), anchor="w")
lbl_x1.place(x=1000, y=630, width=200)

lbl_x2 = Label(ventana_principal, text="x2 = ", bg="#F3F3F3", fg="#000000", font=("Courier New", 13), anchor="w")
lbl_x2.place(x=1000, y=670, width=200)

#-----------------
# zona de Button's
#-----------------

def calcular_raices():
	global x1, x2
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
		x1 = (-b + math.sqrt(d)) / (2*a)
		x2 = (-b - math.sqrt(d)) / (2*a)
		
		lbl_tipo_raiz.config(text="Tipo: Raíces reales y distintas")
		lbl_x1.config(text=f"x1 = {round(x1, 4)}")
		lbl_x2.config(text=f"x2 = {round(x2, 4)}")
		
	elif d == 0:
		x1 = -b / (2*a)
		x2 = x1
		
		lbl_tipo_raiz.config(text="Tipo: Raíz real única (doble)")
		lbl_x1.config(text=f"x1 = {round(x1, 4)}")
		lbl_x2.config(text=f"x2 = {round(x2, 4)}")
		
	else:
		# raíces complejas
		real = -b / (2*a)
		imag = math.sqrt(abs(d)) / (2*a)
		x1 = complex(real, imag)
		x2 = complex(real, -imag)
		
		lbl_tipo_raiz.config(text="Tipo: Raíces complejas")
		lbl_x1.config(text=f"x1 = {round(real, 4)} + {round(imag, 4)}i")
		lbl_x2.config(text=f"x2 = {round(real, 4)} - {round(imag, 4)}i")

calcular_raiz = Button(ventana_principal, text="Calcular raíces", command=calcular_raices, bg="#2483FF", fg="#FFFFFF", font=("Courier New", 17))
calcular_raiz.place(x=60, y=500, width=400, height=110)

ventana_principal.mainloop()