def sumar (num1, num2):
    return num1 + num2

def restar (num1, num2):
    return num1 - num2

def multiplicar (num1, num2):
    return num1 * num2

def menu_principal():
    try:
        operacion = int(input("Ingrese el numero de operacion"))
        valor1 = int(input("Ingrese el primer valor"))
        valor2 = int(input("Ingrese el segundo valor"))
    except ValueError:
        print("No se ingreso un numero")
        return

    match operacion:
        case 1:
            resultado = sumar(valor1, valor2)
        case 2:
            resultado = restar(valor1, valor2)
        case 3:
            resultado = multiplicar(valor1, valor2)
        case 4: 
            resultado = dividir(valor1, valor2)
        case 5:
            resultado = potencia(valor1, valor2)
        case 6:
            resultado = raiz(valor1, valor2)
        case _:
            resultado = "Operacion invalida"

    print(resultado)

menu_principal()