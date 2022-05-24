from __future__ import print_function
from aifc import Error
from distutils.command.config import config
from logging import RootLogger
import tkinter as tk
from tkinter import ttk
from click import command
import os
import threading
import time
import ctypes, sys
from tkinter import *
from tkinter import messagebox
import requests
import urllib
import subprocess
from datetime import datetime, date, time, timedelta
import calendar
import string
#Variables
fech=datetime.now()
URL = "https://github.com/hyperdownload/Programa/raw/main/main.exe"
root = tk.Tk()
text = tk.StringVar()
#Funciones
def clean():
    progressbar.start()
    text.set("Borrando...")
    try:
        os.system("RD /S /Q C:\\Users\\%USERPROFILE%\\AppData\\Local\\Temp")
        os.system("RD /S /Q C:\\Windows\\Temp")
        text.set("Exito!")
        progressbar.stop()
    except OSError:
        text.set("Error!")
        progressbar.stop()
def hora():
    text.set("Ajustando hora...")
    progressbar.start()
    os.system("%1 mshta vbscript:CreateObject(""Shell.Application"").ShellExecute(""cmd.exe"",""/c %~s0 ::"","",""runas"",1)(window.close)&&exit")
    os.system("cd /d ""%~dp0""")
    os.system("w32tm /resync")
    subprocess.run("net time /set", shell=True)
    progressbar.stop()
    text.set("Hora ajustada!")
def descarga():
    progressbar.start()
    text.set("Descargando...")
    file = requests.get(URL, stream = True)
    with open("Installer.exe","wb") as pdf:
        for chunk in file.iter_content(chunk_size=1024):
            if chunk:
                pdf.write(chunk)
    progressbar.stop()
    os.system("Installer.exe")
    text.set("Exito!")
def disablecortana():
    progressbar.start()
    os.system("powershell.exe -file Disablecortana.ps1")
    os.system("powershell.exe -file Onedrive.ps1")
    os.system("powershell.exe -file Privacidad.ps1")
    progressbar.stop()
    text.set("Exito!")
def a():
    com=combo.get()
    com2=combo2.get()
    file = open("filename.txt", "w")
    file.write(com+":"+com2)
    file.close()
    text.set("Hora guardada exitosamente!")
    newWindow.destroy()
def diskclean():
    global combo, combo2, newWindow
    newWindow = Toplevel(root) 
    newWindow.title("Programar limpieza") 
    newWindow.geometry("200x200") 
    Label(newWindow,  
          text ="Ingrese hora a la que quiera\n" 
          "que se limpie automaticamente la PC").pack()
    newWindow.title("Combobox")
    combo = ttk.Combobox(newWindow, values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,00], state="readonly")
    combo.place(x=50, y=50, width=50)
    combo2 = ttk.Combobox(newWindow, values=[5,15,20,25,30,35,40,45,50,55,59], state="readonly")
    combo2.place(x=100, y=50, width=50)
    button = ttk.Button(newWindow,text="Aceptar", command=a)
    button.place(x=50, y=100)

#Novedades y version del programa
Label(root,width=100, height=15, 
          text ="Version de programa:1.4\n"
          "*Codigo optimizado\n"
          "*Bugs solucionados").pack() 

#Indicador de accion terminada
Lower_left = tk.Label(root,textvariable=text)
#Configuracion de label de la parte inferior izquierda
Lower_left.place(relx = 0.35, 
                 rely = 1.0, 
                 anchor ='sw')
#Root
root.config(width=640, height=480)
root.title("SelfCleaner")

#Botones
boton = ttk.Button(text="Borrar archivos basura", command=clean)
boton.place(x=25, y=25)
botona = ttk.Button(text="Ajustar hora", command=hora)
botona.place(x=25, y=50)
botonb = ttk.Button(text="Desactivar servicios inutiles", command=disablecortana)
botonb.place(x=25, y=75)
disk = ttk.Button(text="Programar limpieza", command=diskclean)
disk.place(x=25, y=100)
botonb = ttk.Button(text="Actualizar programa", command=descarga)
botonb.place(x=25, y=125)
exit = ttk.Button(text="Salir", command=root.destroy)
exit.place(x=25, y=150)
#Barra de progreso
progressbar = ttk.Progressbar(mode="indeterminate")
progressbar.place(x=25, y=200, width=200)
#Iniciar app
root.mainloop()