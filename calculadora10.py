def suma(a, b):
    return a + b

def sumaTest():
    resultado = suma(1, 1)
    if(int(resultado) == 2):
        print("test correcto 1+1=2")
    else:
        print("test incorrecto 1+1=2 resultado "+resultado)

    resultado = suma(1, 0)
    if(int(resultado) == 1):
        print("test correcto 1+0=1")
    else:
        print("test incorrecto 1+0=1 resultado "+resultado)

    resultado = suma(-1, 1)
    if(int(resultado) == 0):
        print("test correcto -1+1=0")
    else:
        print("test incorrecto -1+1=0 resultado "+resultado)