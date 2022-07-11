import re 
from numeros_letras import convert, Verificar

def Encriptar(palabra):
    bandera = Verificar(palabra)

    palabra_cod = palabra
    cod = []
    cod_bien = []
    palabra_cod = palabra_cod.upper()
    numero = 0

    if(bandera == True):
        for x in palabra_cod:
            try:
                if(x == ' '):
                    caracter = '#'
                    cod.append(caracter)
                else:
                    agregar = ord(x)-64
                    if(agregar <= 0):
                        x = int(x)
                        numero = x - (x * 2)
                        cod.append(numero)
                    elif(agregar > 26):
                        cod.append(str(x))
                    else:
                        cod.append(agregar)
            except:
                cod.append(str(x))
        #print(cod)

        for i in cod:
            try:
                if(i == '#'):
                    cod_bien.append(i)
                else:
                    i = int(i)
                    num = i + 2
                    if(i <= 0):
                        cod_bien.append(i)
                    else:
                        if(num == 27 or num == 28):
                            num = num - 26  
                            cod_bien.append(num)
                        else:
                            cod_bien.append(num)
            except:
                cod_bien.append(str(i))

        #print(cod_bien)
        cod_transformado = convert(cod_bien)
        palabra_final = ""

        for j in cod_transformado:
            if(j == '#'):
                palabra_final = palabra_final + ' '
            else:
                palabra_final = str(palabra_final) + str(j)
        
        return palabra_final

    else:
        return "Lo siento! La cadena no es válida."

