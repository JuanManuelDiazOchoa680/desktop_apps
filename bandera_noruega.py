from tkinter import *

ventana = Tk()
ventana.title("Bandera de Noruega")
ventana.geometry("962x700")
ventana.config(bg="#FFFFFF")
ventana.resizable(0, 0)
# piezas bamndera

frame_rojo_1=Frame(ventana)
frame_rojo_1.config(bg="#BA0C2F", width=250, height=250)
frame_rojo_1.place(x=0, y=0)

frame_rojo_2=Frame(ventana)
frame_rojo_2.config(bg="#BA0C2F", width=250, height=250)
frame_rojo_2.place(x=0, y=450)

frame_rojo_3=Frame(ventana)
frame_rojo_3.config(bg="#BA0C2F", width=512, height=250)
frame_rojo_3.place(x=450, y=0)

frame_rojo_4=Frame(ventana)
frame_rojo_4.config(bg="#BA0C2F", width=512, height=250)
frame_rojo_4.place(x=450, y=450)

frame_rojo_3=Frame(ventana)
frame_rojo_3.config(bg="#00205B", width=962, height=100)
frame_rojo_3.place(x=0, y=300)

frame_rojo_4=Frame(ventana)
frame_rojo_4.config(bg="#00205B", width=100, height=700)
frame_rojo_4.place(x=300, y=0)


ventana.mainloop()