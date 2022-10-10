from tkinter import * 
from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk
import os
import requests
from tkinter import *
import subprocess
from tkinter import messagebox
import platform
import psutil
import time
import threading
import multiprocessing
import sys
import keyboard
import random
#Variables
URL = "https://github.com/hyperdownload/Programa/raw/main/main.exe"
root = tk.Tk()
text = tk.StringVar()
root.iconbitmap('unnamed.ico')
icono_grande = tk.PhotoImage(file="unnamed.png")
root.iconphoto(False, icono_grande)
varconsole = StringVar()
#Funciones
def infobotton():
    info = Toplevel(root) 
    info.title("Info") 
    info.config(width=400, height=400)
    Label(info,width=100, height=15, 
        text ="Informacion de las funciones del programa.\n"
        "Mantenimiento: se borran gran cantidad de archivos innecesarios y varios temporales que no son necesarios para el sistema operativo.\n"
        "Desfragmentar el disco duro: es un proceso mediante el que se reordenan los archivos dentro de un disco duro.\n"
        "conservando su posición en el sistema de archivos, pero eliminando los posibles ""huecos"" que han dejado\n"
        "archivos que has borrado y ya no se encuentran guardados en tu disco.\n"
        "Limpiar el registro de windows: Limpia todas las entradas y salidas basura del registro de windows.\n"
        "Acelerar internet: acelera la velocidad de internet borrando caches y reconfigurando la conexion.").pack() 
    info.pack(padx=20, pady=20)
def growinternet():
    progressbar['value']=1
    process = subprocess.Popen("ipconfig /release", stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    varconsole.set(output)
    progressbar['value']=20
    process = subprocess.Popen("ipconfig /renew", stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    varconsole.set(output)
    progressbar['value']=40
    process = subprocess.Popen("ipconfig /flushdns", stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    varconsole.set(output)
    progressbar['value']=60
    process = subprocess.Popen("netsh winsock reset", stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    varconsole.set(output)
    progressbar['value']=80
    process = subprocess.Popen("netsh advfirewall firewall add rule name=""StopThrottling"" dir=in action=block remoteip=173.194.55.0/24,206.111.0.0/16 enable=yes", stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    varconsole.set(output)
    progressbar['value']=100
    messagebox.showinfo(message="La app se cerrara para aplicar los cambios", title="Atencion!")
    root.destroy()
    sys.exit()
def cleanregister():
    progressbar['value']=1
    process = subprocess.Popen("Sfc/ Scannow", stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    varconsole.set(output)
    progressbar['value']=20
    process = subprocess.Popen("DISM /Online /Cleanup-Image /RestoreHealth ", stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    varconsole.set(output)
    progressbar['value']=60
    process = subprocess.Popen("DISM.exe /Online /Cleanup-image /Restorehealth", stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    varconsole.set(output)
    progressbar['value']=100
    text.set("Registro limpiado con exito!")
    messagebox.showinfo(message="La app se cerrara para aplicar los cambios", title="Atencion!")
    root.destroy()
    sys.exit()
def cleanrecycle():
    progressbar['value']=1
    #Proceso a ejecutar
    process = subprocess.Popen("rd /q /s G:\$Recycle.Bin", stdout=subprocess.PIPE, stderr=None, shell=True)
    progressbar['value']=100
    #Obtener salida de consola
    output = process.communicate()
    varconsole.set(output)
    messagebox.showinfo(message="La app se cerrara para aplicar los cambios", title="Atencion!")
    root.destroy()
    sys.exit()
def console():
    def getTextInput():
        #Verificar entrada de texto
        command=textExample.get()
        #Proceso a ejecutar
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
        #Obtener salida de consola
        output = process.communicate()
        #Actualizar label 
        varconsole.set(output)
    while True:
        if keyboard.read_key() == "p":
            time.sleep(0.2)
            #Ventana de la consola
            consolev = Toplevel(root) 
            consolev.title("Console") 
            consolev.config(width=400, height=400)
            consolev.iconbitmap('unnamed.ico')
            console=Label(consolev, textvariable=varconsole,width=100)
            console.pack(padx=20, pady=20)
            #Entrada de texto
            textconsole=Entry(consolev, width=100)
            textconsole.pack(padx=10, pady=10)
            #Boton de subida
            bottonread=ttk.Button(consolev,text="Entry", command=getTextInput)
            bottonread.place(x=100, y=125)
def desfragmentar():
    resultado = MessageBox.askquestion("Advertencia", 
    "Esta opcion es para discos duros mecanicos y no es funcional para los de estado solido, desea continuar?")

    if resultado == "yes":
        text.set("Desfragmentando disco...")
        subprocess.Popen("defrag c: -u")
        text.set("Disco desfragmentado!")
    messagebox.showinfo(message="La app se cerrara para aplicar los cambios", title="Atencion!")
    root.destroy()
    sys.exit()
def clean():
    progressbar['value']=1
    subprocess.Popen("RD /S /Q C:\\Users\\%USERPROFILE%\\AppData\\Local\\Temp")
    progressbar['value']=10
    subprocess.Popen("RD /S /Q C:\\Windows\\Temp")
    progressbar['value']=20
    subprocess.Popen("RD /S /Q C:\\Users\\%USERPROFILE%\\AppData\\Local\\Temp")
    progressbar['value']=30
    subprocess.Popen("RD /S /Q C:\\Windows\\%Temp%")
    progressbar['value']=40
    subprocess.Popen("RD /S /Q C:\\Users\\%USERPROFILE%\\AppData\\Local\\Temp")
    progressbar['value']=50
    subprocess.Popen("RD /S /Q C:\\Windows\\Prefetch")
    progressbar['value']=60
    subprocess.Popen("DISM /online /cleanup-image /scanHealth")
    progressbar['value']=70
    subprocess.Popen("powershell.exe -file Disablecortana.ps1")
    progressbar['value']=80
    subprocess.Popen("powershell.exe -file Onedrive.ps1")
    progressbar['value']=90
    subprocess.Popen("powershell.exe -file Privacidad.ps1")
    progressbar['value']=100
    text.set("Exito!")
    messagebox.showinfo(message="La app se cerrara para aplicar los cambios", title="Atencion!")
    root.destroy()
    sys.exit()
def descarga():
    porcentaje=0
    file = requests.get(URL, stream = True)
    with open("Installer.exe","wb") as pdf:
        text.set("Descargando...")
        for chunk in file.iter_content(chunk_size=1024):
            porcentaje=porcentaje+1/100
            varconsole.set(porcentaje)
            progressbar['value']=porcentaje
            downloadporcentaje = round(porcentaje, 2)
            if chunk:
                pdf.write(chunk)
    os.popen("Installer.exe")
    text.set("Exito!")
    messagebox.showinfo(message="La app se cerrara para actualizar", title="Atencion!")
    root.destroy()
    sys.exit()
#Novedades y version del programa
Label(root,width=100, height=15, 
        text ="Version de programa:1.7\n"
        "+Consola de comandos agregada\n"
        "+Barra de progreso mejorada\n"
        "+Limpieza de papelera agregada\n"
        "+Aumentar rendimiento de internet agregado\n"
        "+Limpieza de registro de windows agregada\n"
        "+Bugs solucionados").pack() 
#Indicador de accion terminada
Lower_left = tk.Label(root,textvariable=text)
#Configuracion de label de la parte inferior izquierda
Lower_left.place(relx = 0.35, 
                            rely = 1.0, 
                            anchor ='sw')
#hilos
hiloclean = threading.Thread(target=clean, daemon=True)
hilodesfrag = threading.Thread(target=desfragmentar, daemon=True)
update = threading.Thread(target=descarga, daemon=True)
recycleclean = threading.Thread(target=cleanrecycle, daemon=True)
registerclean=threading.Thread(target=cleanregister, daemon=True)
net=threading.Thread(target=growinternet, daemon=True)
consola = threading.Thread(target=console, daemon=True)
consola.start()
#Root
root.config(width=640, height=480)
root.title("SelfCleaner")
#Botones
clean = ttk.Button(text="Realizar mantenimiento", command=hiloclean.start)
clean.place(x=25, y=25)
descarga = ttk.Button(text="Actualizar programa", command=update.start)
descarga.place(x=25, y=50)
desfrag=ttk.Button(text="Desfragmentar disco", command=hilodesfrag.start)
desfrag.place(x=25, y=75)
recycleclean=ttk.Button(text="Vaciar papelera de reciclaje", command=recycleclean.start)
recycleclean.place(x=25, y=100)
registerclean=ttk.Button(text="Limpiar el registro de windows", command=registerclean.start)
registerclean.place(x=25, y=125)
netglow=ttk.Button(text="Acelerar internet", command=net.start)
netglow.place(x=25, y=150)
infoleft=ttk.Button(text="Info.", command=infobotton)
infoleft.place(x=600, y=200)
#Barra de progreso
progressbar = Progressbar(orient=HORIZONTAL,mode='determinate')
progressbar.place(x=25, y=200, width=200)
#Iniciar app
root.mainloop()