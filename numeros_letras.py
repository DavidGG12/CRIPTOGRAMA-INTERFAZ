def Verificar(palabra):
    palabra_bien = palabra
    try:
        palabra=int(palabra)
        bandera = False
    except:
        #palabra = "Chanchito Feliz"
        bandera = True
    return bandera

def convert(palabra = []):
    bandera = Verificar(palabra)
    cod = []

    if(bandera == True):
        for i in palabra:
            try:
                if(i == '#'):
                    cod.append(i)
                else:
                    i = int(i)
                    if(i == 1):
                        cod.append("A")
                    elif(i == 2):
                        cod.append("B")
                    elif(i == 3):
                        cod.append("C")
                    elif(i == 4):
                        cod.append("D")
                    elif(i == 5):
                        cod.append("E")
                    elif(i == 6):
                        cod.append("F")
                    elif(i == 7):
                        cod.append("G")
                    elif(i == 8):
                        cod.append("H")
                    elif(i == 9):
                        cod.append("I")
                    elif(i == 10):
                        cod.append("J")
                    elif(i == 11):
                        cod.append("K")
                    elif(i == 12):
                        cod.append("L")
                    elif(i == 13):
                        cod.append("M")
                    elif(i == 14):
                        cod.append("N")
                    elif(i == 15):
                        cod.append("O")
                    elif(i == 16):
                        cod.append("P")
                    elif(i == 17):
                        cod.append("Q")
                    elif(i == 18):
                        cod.append("R")
                    elif(i == 19):
                        cod.append("S")
                    elif(i == 20):
                        cod.append("T")
                    elif(i == 21):
                        cod.append("U")
                    elif(i == 22):
                        cod.append("V")
                    elif(i == 23):
                        cod.append("W")
                    elif(i == 24):
                        cod.append("X")
                    elif(i == 25):
                        cod.append("Y")
                    elif(i == 26):
                        cod.append("Z")
                    elif(i <= 0):
                        i = int(i)
                        numero = i - (i*2)
                        cod.append(numero)
            except:
                cod.append(str(i))
        return cod   
    else:
        return "Error en la conversión."