from tkinter import *

ventana_principal = Tk()

ventana_principal.title("Norway")

ventana_principal.geometry("800x500")

ventana_principal.resizable(0,0)

ventana_principal.config(bg="black")


frame_1 = Frame(ventana_principal)
frame_1.config(bg="red2", width=780, height=480)
frame_1.place(x=10, y=10)


frame_2 = Frame(ventana_principal)
frame_2.config(bg="white", width=100, height=480)
frame_2.place(x=200, y=10)


frame_3 = Frame(ventana_principal)
frame_3.config(bg="white", width=780, height=100)
frame_3.place(x=10, y=200)


frame_4 = Frame(ventana_principal)
frame_4.config(bg="navy", width=780, height=50)
frame_4.place(x=10, y=225)


frame_5 = Frame(ventana_principal)
frame_5.config(bg="navy", width=50, height=480)
frame_5.place(x=225, y=10)

ventana_principal.mainloop()