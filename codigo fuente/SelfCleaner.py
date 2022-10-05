import tkinter as tk
from tkinter import ttk
import os
import requests
from tkinter import *
import subprocess
from tkinter import messagebox as MessageBox
import platform
import psutil
import time
import threading
import multiprocessing
import sys
#Variables
URL = "https://github.com/hyperdownload/Programa/raw/main/main.exe"
root = tk.Tk()
text = tk.StringVar()
#Funciones
def desfragmentar():
    resultado = MessageBox.askquestion("Advertencia", 
    "Esta opcion es para discos duros mecanicos y no es funcional para los de estado solido, desea continuar?")

    if resultado == "yes":
        text.set("Desfragmentando disco...")
        subprocess.Popen("defrag c: -u")
        text.set("Disco desfragmentado!")
    messagebox.showinfo(message="La app se cerrara para aplicar los cambios", title="Atencion!")
def clean():
    progressbar.step(1)
    subprocess.Popen("RD /S /Q C:\\Users\\%USERPROFILE%\\AppData\\Local\\Temp")
    subprocess.Popen("RD /S /Q C:\\Windows\\Temp")
    subprocess.Popen("RD /S /Q C:\\Users\\%USERPROFILE%\\AppData\\Local\\Temp")
    subprocess.Popen("RD /S /Q C:\\Windows\\%Temp%")
    subprocess.Popen("RD /S /Q C:\\Users\\%USERPROFILE%\\AppData\\Local\\Temp")
    subprocess.Popen("RD /S /Q C:\\Windows\\Prefetch")
    subprocess.Popen("DISM /online /cleanup-image /scanHealth")
    progressbar.step(50)
    subprocess.Popen("powershell.exe -file Disablecortana.ps1")
    subprocess.Popen("powershell.exe -file Onedrive.ps1")
    subprocess.Popen("powershell.exe -file Privacidad.ps1")
    progressbar.step(99.9)
    text.set("Exito!")
    messagebox.showinfo(message="La app se cerrara para aplicar los cambios", title="Atencion!")
def descarga():
    progressbar.step(1)
    text.set("Descargando...")
    file = requests.get(URL, stream = True)
    progressbar.step(50)
    with open("Installer.exe","wb") as pdf:
        for chunk in file.iter_content(chunk_size=1024):
            if chunk:
                pdf.write(chunk)
    progressbar.step(100)
    os.popen("Installer.exe")
    text.set("Exito!")
    messagebox.showinfo(message="La app se cerrara para actualizar", title="Atencion!")
#Novedades y version del programa
Label(root,width=100, height=15, 
        text ="Version de programa:1.6\n"
        "*Codigo reescrito y optimizado\n"
        "*Bugs solucionados").pack() 
#Indicador de accion terminada
Lower_left = tk.Label(root,textvariable=text)
#Configuracion de label de la parte inferior izquierda
Lower_left.place(relx = 0.35, 
                            rely = 1.0, 
                            anchor ='sw')
#hilos
hiloclean = threading.Thread(target=clean, daemon=True)
hilodesfrag = threading.Thread(target=desfragmentar, daemon=True)
barra = threading.Thread(target=barra, daemon=True)
update = threading.Thread(target=descargando, daemon=True)
#Root
root.config(width=640, height=480)
root.title("SelfCleaner")
#Botones
clean = ttk.Button(text="Realizar mantenimiento", command=hiloclean.start)
clean.place(x=25, y=25)
descarga = ttk.Button(text="Actualizar programa", command=update)
descarga.place(x=25, y=50)
desfrag=ttk.Button(text="Desfragmentar disco", command=hilodesfrag.start)
desfrag.place(x=25, y=75)
desfra=ttk.Button(text="barra", command=barra.start)
desfra.place(x=25, y=100)
#Barra de progreso
progress = tk.IntVar()
variable=progress
progressbar = ttk.Progressbar(maximum=101)
progressbar.place(x=25, y=200, width=200)
#Iniciar app
root.mainloop()