print("Bienvenido a calculadora")

while True:
    print("\nQue desea calcular?:")
    eleccion= input("1.Sumar." " 2.Restar" " 3.Multiplicar" " 4.Dividir" " 5.Potenciar" " 6.Raiz " " 7.Salir: ")

    if eleccion == "1":
        try:
            primernumero= float(input("Coloque el primer numero: "))
            segundonumero= float(input("Coloque el segundo numero: "))
            resultadoalfa=primernumero+segundonumero
            print("Resultado: ",resultadoalfa)
        except:
            print("Debe colocar valores numericos")    
    elif eleccion == "2":
        try:
            primernumero= float(input("Coloque el primer numero: "))
            segundonumero= float(input("Coloque el segundo numero: "))
            resultadoalfa=primernumero-(-segundonumero)
            print("Resultado: ",resultadoalfa)
        except:
            print("Debe colocar valores numericos")    
    elif eleccion == "3":
        try:
            primernumero= float(input("Coloque el primer numero a multiplicar: "))
            segundonumero= float(input("Coloque el segundo numero a multiplicar: "))
            resultadoalfa=primernumero*segundonumero
            print("Resultado: ",resultadoalfa)
        except:
            print("Debe colocar un valor numerico")    
    elif eleccion == "4":
        try:
            primernumero = float(input("Coloque el primer numero a dividir: "))
            segundonumero = float(input("Coloque el segundo numero a dividir: "))
            resultadoalfa = primernumero / segundonumero
            print("Resultado:", resultadoalfa)
        except ValueError:
            print("Debe colocar un valor numérico")
        except ZeroDivisionError:
            print("No se puede dividir por cero") 
    elif eleccion == "5":
        try:
            primernumero= float(input("Coloque el primer numero: "))
            segundonumero= float(input("Coloque potencia: "))
            resultadoalfa=primernumero**segundonumero
            print("Resultado: ",resultadoalfa)
        except:
            print("Debe colocar un valor numerico")    
    elif eleccion == "6":
        def calcular_raiz(numero, indice):
            if indice == 0:
                return "El índice no puede ser 0"
            if numero < 0 and indice % 2 == 0:
                return "No se puede raíz par de un número negativo"
            return numero ** (1 / indice)
        try:
            numero = float(input("Ingrese el número al que aplicarle raiz: "))
            indice = int(input("Ingrese el índice de la raíz: "))
    
        except:
            print("Error: debes ingresar números válidos")
            exit()
        resultado = calcular_raiz(numero, indice)

        print("Resultado:", resultado)
    elif eleccion == "7":
        print("Saliendo de la calculadora...")
        break    

        





