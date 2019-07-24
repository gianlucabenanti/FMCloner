from tkinter import *
import tkinter as tk
from config import files
import os

#CREO LA FINESTRA
top = tk.Tk()

#IMPOSTO IL TITOLO E LA DIMENSIONE
top.title("FM Cloner")
top.resizable(width=FALSE, height=FALSE)
top.geometry("500x500")

#CREO LA LABEL
l = Label(top, text = "SELEZIONA I FILES:")

#CREO LA LISTA DEI FILES
lb = Listbox(top, selectmode = "multiple")

for file in files:
    lb.insert(files.index(file),file)

def messaggio():
    msg = Message(top, text=lb.curselection())
    msg.place(anchor = NW, x = 300, y = 80)
    #command = os.popen("dir").read()

    for x in lb.curselection():
        print(lb.get(x))

    lb.selection_clear(0, END)

#CREO IL BOTTONE
b = Button(top, text = "Clona", command = messaggio)

#MOSTRO TUTTI GLI OGGETTI
lb.place(anchor = NW, x = 20, y = 40, height = 450, width = 230)
l.place(anchor = NW, x = 20, y = 20)
b.place(anchor = NW, x = 270, y = 40)


top.mainloop()