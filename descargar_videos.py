from pytube import YouTube
import os
from tkinter import *
from tkinter import messagebox as MessageBox

print(os.getcwd())

def accion():
    enlace=videos.get()     
    video = YouTube(enlace)  
    descarga = video.streams.get_highest_resolution()
    descarga.download()

def popup():
    MessageBox.showinfo("escribe el link del video")

 
root = Tk()
root.config(bd=15)
root.title("descargador")



menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)


menubar.add_cascade(label="Para más información", menu=helpmenu)


menubar.add_command(label="Salir", command=root.destroy)


instrucciones = Label(root, text="descargar videos de youtube")
instrucciones.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

boton = Button(root, text="Descargar", command=accion)
boton.grid(row=2, column=1)

root.mainloop()