from msilib.schema import Error
import tkinter
from typing import Text
from sympy import public
from encriptar import Encriptar
from numeros_letras import Verificar
import webbrowser as web
from time import sleep
import pyautogui

mensaje = ""

def GetText():
    cadena = TextoOriginal.get()
    cadena_encriptada = Encriptar(cadena)
    TextoEncriptado.insert(0, cadena_encriptada)

def Enviar():
    if not TextoEncriptado.get():
        ErrorLblVtn["text"] = "No se ha encriptado nada."
    else:
        mensaje = TextoEncriptado.get()
        ErrorLblVtn["text"] = ""

        def GetNumero():
            numero = NumeroTxt.get()
            bandera = Verificar(numero)

            if(bandera == False):
                contador = 0
                for i in numero:
                    contador = contador + 1
                if(contador == 10):
                    ErrorLbl["text"] = "" 
                    web.open("https://web.whatsapp.com/send?phone=#+52"+numero+"#")
                    sleep(5)
                    for i in mensaje:
                        pyautogui.typewrite(str(i))
                    pyautogui.press("enter")
                else:
                    ErrorLbl["text"] = "Numero invalido" 
            else:
                ErrorLbl["text"] = "Numero no encontrado"
            
        enviar = tkinter.Tk()
        enviar.geometry("500x100")
        enviar.title("Generador de Criptogramas")
        enviar.iconbitmap('C:\\Users\\alien\\OneDrive\\Documentos\\Programacion\\CRIPTOGRAMA-INTERFAZ\\img\\ico.ico')
        
        NumeroLbl = tkinter.Label(enviar, text = "Digite el numero a enviar por whatsapp:")
        NumeroLbl.grid(row = 0, column = 0)
        ErrorLbl = tkinter.Label(enviar)
        ErrorLbl.grid(row = 0, column = 1)
        NumeroTxt = tkinter.Entry(enviar)
        NumeroTxt.grid(row = 1, column = 0)
        EnviarBtn2 = tkinter.Button(enviar, text = "Confirmar", command = lambda: GetNumero())
        EnviarBtn2.grid(row = 2, column = 1)

        enviar.mainloop()

ventana = tkinter.Tk()
ventana.geometry("600x150")
ventana.title("Generador de Criptogramas")
ventana.iconbitmap('C:\\Users\\alien\\OneDrive\\Documentos\\Programacion\\CRIPTOGRAMA-INTERFAZ\\img\\ico.ico')

Lbl1 = tkinter.Label(ventana, text = "Coloca el texto a encriptar:")
Lbl1.grid(row = 0, column = 0)

TextoOriginal = tkinter.Entry(ventana)
TextoOriginal.grid(row = 1, column = 0)

Lbl2 = tkinter.Label(ventana, text = "Texto encriptado:")
Lbl2.grid(row = 0, column = 2, padx = 200)

TextoEncriptado = tkinter.Entry(ventana)
TextoEncriptado.grid(row = 1, column = 2)

ErrorLblVtn = tkinter.Label(ventana)
ErrorLblVtn.place(x = 200, y = 120)

EncriptarBtn = tkinter.Button(ventana, text = "Encriptar", command = lambda: GetText())
EncriptarBtn.grid(row = 2, column = 1, pady = 50, padx = 20)
EncriptarBtn.place(x = 210, y = 70)

EnviarBtn = tkinter.Button(ventana, text = "Enviar", command = lambda: Enviar())
EnviarBtn.grid(row = 2, column = 1)
EnviarBtn.place(x = 320, y = 70)

ventana.mainloop()