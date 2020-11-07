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

def resta(a, b):
    return a - b

def restaTest():
    resultado = resta(1, 1)
    if(int(resultado) == 0):
        print("test correcto 1-1=0")
    else:
        print("test incorrecto 1-1=0 resultado "+str(resultado))

    resultado = resta(3, 2)
    if(int(resultado) == 1):
        print("test correcto 3-2=1")
    else:
        print("test incorrecto 3-2=1 resultado "+str(resultado))

    resultado = resta(-1, 1)
    if(int(resultado) == -2):
        print("test correcto -1-1=-2")
    else:
        print("test incorrecto -1-1=-2 resultado "+str(resultado))

def division(a, b):
    if(int(b) == 0):
        return "Error"
    return a / b

def divisionTest():
    resultado = division(2, 2)
    if(int(resultado) == 1):
        print("test correcto 2/2=1")
    else:
        print("test incorrecto 2/2=1 resultado "+str(resultado))

    resultado = division(1, 0)
    if(resultado == "Error"):
        print("test correcto 1/0 Error")
    else:
        print("test incorrecto 1/0 resultado "+str(resultado))

    resultado = division(8, 4)
    if(int(resultado) == 2):
        print("test correcto 8/4=2")
    else:
        print("test incorrecto 8/4=2 resultado "+str(resultado))

def multiplicacion(a, b):
    return a * b

def multiplicacionTest():
    resultado = multiplicacion(1, 1)
    if(int(resultado) == 1):
        print("test correcto 1*1=1")
    else:
        print("test incorrecto 1*1=1 resultado "+str(resultado))

    resultado = multiplicacion(2, 2)
    if(int(resultado) == 4):
        print("test correcto 2*2=4")
    else:
        print("test incorrecto 2*2=4 resultado "+str(resultado))

    resultado = multiplicacion(2, 0)
    if(int(resultado) == 0):
        print("test correcto 2*0=0")
    else:
        print("test incorrecto 2*0=0 resultado "+str(resultado))