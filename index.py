import tkinter
from typing import Text
from sympy import public
from interfaces import encriptar_interface, desencriptar_interface
from encriptar import Encriptar, Desencriptar
from numeros_letras import Verificar
import webbrowser as web
from time import sleep
import pyautogui
class index:
    def main():
        def VtnEncriptar():
            encriptar_interface()
        
        def VtnDesencriptar():
            desencriptar_interface()

        main = tkinter.Tk()
        main.geometry("300x300")
        main.title("Inicio")
        main.iconbitmap('C:\\Users\\alien\\OneDrive\\Documentos\\Programacion\\CRIPTOGRAMA-INTERFAZ\\img\\ico.ico')

        #EncriptarBtn_Design = ttk.Style()
        #EncriptarBtn_Design.configure("Encriptar_Design", background = "white")
        Encriptar = tkinter.Button(main, text = "Encriptar", command = lambda: VtnEncriptar())
        Encriptar.place(x = 110, y = 30)

        Desencriptar = tkinter.Button(main, text = "Desencriptar", command = lambda: VtnDesencriptar())
        Desencriptar.place(x = 95, y = 120)

        main.mainloop()
    main()

