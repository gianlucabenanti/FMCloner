try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from config import files
import os
import subprocess

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

#PROCEDURA PER CLONARE UNO O PIU FILES
def Clona():
    #MEMORIZZO I COMANDI DA UTILIZZARE
    cmd1 = "fmsadmin BACKUP "
    cmd2 = " --clone -u sandezaserver -p s4nd3z4"

    #ESEGUO I COMANDI SU OGNI FILE SELEZIONATO
    for x in lb.curselection():
        os.system(cmd1+lb.get(x)+cmd2)

    #MOSTRO LA CARTELLA BACKUP IN BASE AL SISTEMA OPERATIVO IN CUI MI TROVO
    if os.name == "nt":
        subprocess.call("explorer C:\\Program Files\\FileMaker\\FileMaker Server\\Data\\Backups")
    else:
        subprocess.call(["open", "-R", "/Library/FileMaker Server/Data/Backups"])

    #ANNULLO LA SELEZIONE
    lb.selection_clear(0, END)

#CREO IL BOTTONE
b = Button(top, text = "Clona", command = Clona)

#DISEGNO TUTTI GLI OGGETTI
lb.place(anchor = NW, x = 20, y = 40, height = 450, width = 230)
l.place(anchor = NW, x = 20, y = 20)
b.place(anchor = NW, x = 270, y = 40)

#LOOP PER MOSTRARE LA FINESTRA
top.mainloop()