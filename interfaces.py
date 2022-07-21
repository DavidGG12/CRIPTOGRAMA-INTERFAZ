import tkinter
from typing import Text
from sympy import public
from encriptar import Encriptar, Desencriptar
from numeros_letras import Verificar
import webbrowser as web
from time import sleep
import pyautogui
  
def encriptar_interface():
    #VARIABLES PARA USAR
    mensaje = ""

    #MÉTODOS DEL MENÚ
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
            TextoEncriptado.delete(0, 3000)
            enviar_interface(mensaje)
    
    def Back():
        ventana.destroy()
        #main()

    ventana = tkinter.Tk()
    ventana.geometry("600x200")
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
    EncriptarBtn.place(x = 210, y = 70)

    EnviarBtn = tkinter.Button(ventana, text = "Enviar", command = lambda: Enviar())
    EnviarBtn.place(x = 320, y = 70)

    Regresar = tkinter.Button(ventana, text = "Regresar")
    Regresar.place(x = 250, y = 150)

    ventana.mainloop()

def enviar_interface(mensaje):
    #MÉTODO PARA OBTENER EL NÚMERO Y ENVIARLO
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
                    enviar.destroy()
                    sleep(10)
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

def desencriptar_interface():
    #VARIABLES PARA USAR
    mensaje = ""

    #MÉTODOS DEL MENÚ
    def GetText():
        cadena = TextoEncriptado.get()
        cadena_encriptada = Desencriptar(cadena)
        TextoDesencriptado.insert(0, cadena_encriptada) 
    

    desencriptar = tkinter.Tk()
    desencriptar.geometry("650x200")
    desencriptar.title("Generador de Criptogramas")
    desencriptar.iconbitmap('C:\\Users\\alien\\OneDrive\\Documentos\\Programacion\\CRIPTOGRAMA-INTERFAZ\\img\\ico.ico')

    Lbl1 = tkinter.Label(desencriptar, text = "Coloca el texto a desencriptar:")
    Lbl1.grid(row = 0, column = 0)

    TextoEncriptado = tkinter.Entry(desencriptar)
    TextoEncriptado.grid(row = 1, column = 0)

    Lbl2 = tkinter.Label(desencriptar, text = "Texto desencriptado:")
    Lbl2.grid(row = 0, column = 2, padx = 200)

    TextoDesencriptado = tkinter.Entry(desencriptar)
    TextoDesencriptado.grid(row = 1, column = 2)

    ErrorLblVtn = tkinter.Label(desencriptar)
    ErrorLblVtn.place(x = 200, y = 120)

    DesencriptarBtn = tkinter.Button(desencriptar, text = "Desencriptar", command = lambda: GetText())
    DesencriptarBtn.place(x = 210, y = 70)

    Regresar = tkinter.Button(desencriptar, text = "Regresar")
    Regresar.place(x = 350, y = 70)

    desencriptar.mainloop()
