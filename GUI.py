from cProfile import label
from cgitb import text
import tkinter
from tkinter import *
import tkinter as tk
# UI-Elemente
ui_elements = []
player_names = []
# Methoden


def ui_cleanup():
    global ui_elements
    for e in ui_elements:
        e.destroy()
    ui_elements = []


def menue():
    ui_cleanup()
    label_uberschrift = Label(fenster, text="POW-Karaoke",)
    label_uberschrift.place(x=120, y=20, width=250, height=100)
    # Button erstellen
    start_button = Button(fenster, text="Start", command=vorstart)
    start_button.place(x=180, y=115, width=100, height=100)
    exit_button = Button(fenster, text="Beenden", command=fenster.quit)
    exit_button.place(x=180, y=300, width=100, height=100)
    # extend = Eine Liste erweitern, append
    ui_elements.extend([label_uberschrift, start_button, exit_button])
    fenster.mainloop()

def playeradd(name,player_var):
    print(name)
    player_names.append(name)
    player_var.set(player_var.get() + name + "\n")



def vorstart():
    ui_cleanup()
    label = Label(fenster,text="Geben sie die Namen des Spielers ein")
    player_var = tk.StringVar()
    player_list = Label(fenster,textvariable= player_var)
    
    eingabefeld = Entry(fenster, bd=10, width=60)
    aczept = Button(fenster, text="Hinzufügen", command= lambda: playeradd(eingabefeld.get(),player_var)) #lambda = neue Funktion, was hinter ":" ist der Inhalt
    zurueck = Button(fenster, text="Zurück", command=menue)
    eingabefeld.pack()
    label.pack()
    aczept.pack()
    zurueck.pack()
    player_list.pack()
    eingabefeld.get()
    ui_elements.extend([eingabefeld, aczept, zurueck])


# Fenster erstellen
fenster = tk.Tk()
# Fenster Icon
fenster.tk.call('wm', 'iconphoto', fenster._w, tk.PhotoImage(file='./Kira.png'))
# Fenster Titel
fenster.title("Kira du Hund")
# Fenster Größe
fenster.geometry("500x450")
menue()
# Komponenten in der gewünschten Reihenfolge hinzufügen
"""Mehrzeiliger Kommentar
anweisungs_label.pack()
change_button.pack()  
info_label.pack()
exit_button.pack()
"""
# In der Ereignisschleife des Benutzers warten
fenster.mainloop()
