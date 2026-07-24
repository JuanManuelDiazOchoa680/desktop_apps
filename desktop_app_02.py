from tkinter import *
from tkinter import messagebox
import tkinter as tk
import math

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


def salir():
    messagebox.showinfo("Salir", "VIVA AVERNUS")
    ventana_principal.destroy()


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

#
# botones suma, resta, multiplicacion......
#

boton_suma = Button(frame_operaciones, text="+", bg="#303030", fg="#FFFFFF", font=("Arial", 20))
boton_suma.place(x=50, y=50, width=100, height=100)

boton_resta = Button(frame_operaciones, text="-", bg="#303030", fg="#FFFFFF", font=("Arial", 20))
boton_resta.place(x=200, y=50, width=100, height=100)

boton_multiplicacion = Button(frame_operaciones, text="x", bg="#303030", fg="#FFFFFF", font=("Arial", 20))
boton_multiplicacion.place(x=350, y=50, width=100, height=100)

boton_division = Button(frame_operaciones, text="/", bg="#303030", fg="#FFFFFF", font=("Arial", 20))
boton_division.place(x=500, y=50, width=100, height=100)

boton_potencia = Button(frame_operaciones, text="^", bg="#303030", fg="#FFFFFF", font=("Arial", 20))
boton_potencia.place(x=650, y=50, width=100, height=100)

boton_raiz = Button(frame_operaciones, text="√", bg="#303030", fg="#FFFFFF", font=("Arial", 20))
boton_raiz.place(x=800, y=50, width=100, height=100)

boton_factorial = Button(frame_operaciones, text="!", bg="#303030", fg="#FFFFFF", font=("Arial", 20))
boton_factorial.place(x=950, y=50, width=100, height=100)  

boton_enter = Button(frame_operaciones, text="Enter", bg="#303030", fg="#FFFFFF", font=("Arial", 20))
boton_enter.place(x=1100, y=50, width=150, height=250)

#------------
# boton salir
#------------

boton_salir = Button(ventana_principal, text="Salir", command=salir, bg="#FF0000", fg="#FFFFFF", font=("Arial", 20))
boton_salir.place(x=1800, y=20, width=100, height=50)

#-----------------------------------------
# escribir en el frame de entrada de datos
#-----------------------------------------

label_numero_1 = Label(frame_entrada, text="", bg="#5F5F5F", fg="#FFFFFF", font=("Arial", 30))
label_numero_1.place(x=50, y=50)

entry_numeros = tk.Entry(
    ventana_principal, 
    bg="#FFFFFF",           # Mismo color de la ventana
    fg="black",             # Color de la letra
    font=("Arial", 30),     # Tamaño de fuente amplio
    bd=0,                   # Elimina el borde clásico
    highlightthickness=0    # Elimina el borde de enfoque al hacer clic
)
entry_numeros.place(x=60, y=100, width=1200, height=100)

#
# LOGICA DE BOTONES DE OPERACIONES.... SUMA.... RESTA.... MULTIPLICACION.... DIVISION.... POTENCIA.... RAIZ.... LOGARITMO.... SENO.... COSENO.... TANGENTE.... COTANGENTE.... SECANTE.... COSECANTE.... FACTORIAL   
#

logica_operaciones = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "x": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else "Error: División por cero",
    "^": lambda x, y: x ** y,
    "√": lambda x: x ** 0.5,
    "!": lambda x: math.factorial(int(x)) if x >= 0 and int(x) == x else "Error: Factorial de número negativo o no entero"
}

#
# colocar símbolos de botones en la entrada de datos
#

boton_suma.config(command=lambda: entry_numeros.insert(tk.END, "+"))
boton_resta.config(command=lambda: entry_numeros.insert(tk.END, "-"))
boton_multiplicacion.config(command=lambda: entry_numeros.insert(tk.END, "x"))
boton_division.config(command=lambda: entry_numeros.insert(tk.END, "/"))
boton_potencia.config(command=lambda: entry_numeros.insert(tk.END, "^"))
boton_raiz.config(command=lambda: entry_numeros.insert(tk.END, "√"))
boton_factorial.config(command=lambda: entry_numeros.insert(tk.END, "!"))


#--------------------------------------------------------------------------------------------------------------------------------------------
# funcionalidad boton enter y si despues del enter se teclea una nueva operacion o numero, se quita el texto error y se puede seguir operando
#--------------------------------------------------------------------------------------------------------------------------------------------

import re

def calcular_y_mostrar(event=None):
    expresion = entry_numeros.get()
    try:
        expresion_procesada = expresion.replace("x", "*")
        expresion_procesada = expresion_procesada.replace("^", "**")
        expresion_procesada = re.sub(r'√(\d+(\.\d+)?)', r'math.sqrt(\1)', expresion_procesada)
        expresion_procesada = re.sub(r'√\(([^)]+)\)', r'math.sqrt(\1)', expresion_procesada)
        expresion_procesada = re.sub(r'(\d+)\!', r'math.factorial(\1)', expresion_procesada)

        resultado = eval(expresion_procesada, {"__builtins__": None, "math": math}, logica_operaciones)
        
        if isinstance(resultado, (int, float)):
            resultado_str = f"{resultado:.10f}".rstrip('0').rstrip('.')
        else:
            resultado_str = str(resultado)
            
        zona_resultados.config(text=resultado_str, fg="#000000")
        
    except Exception as e:
        zona_resultados.config(text="Error", fg="#000000")

#-------------------------------------------------------------------
# zona DE RESULTADOS, donde se mostrara el resultado de la operacion
#-------------------------------------------------------------------

zona_resultados = Label(frame_resultados, text="", bg="#FFFFFF", fg="#000000", font=("Arial", 30))
zona_resultados.place(x=50, y=50, width=400, height=100)

def actualizar_resultado():
    resultado = label_numero_1.cget("text")
    zona_resultados.config(text=resultado)


#--------------------------------------------------
# conectar el boton enter con la zona de resultados
#--------------------------------------------------

boton_enter.config(command=calcular_y_mostrar)

#-------------------------------------------------------------------------------------------------
# Conectar la tecla ENTER del teclado físico para que funcione directamente en la entrada de datos
#-------------------------------------------------------------------------------------------------

entry_numeros.bind("<Return>", calcular_y_mostrar)

# Bucle principal
ventana_principal.mainloop()


# NO SOY PRECOZ TEACHER