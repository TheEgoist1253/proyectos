print("Bienvenido a conversor de unidades")

while True:
    opcion = input(
    "1. Conversor de longitudes\n"
    "2. Conversor de temperaturas\n"
    "3. Conversor de Masa\n"
    "4. Conversor de tiempo\n"
    "5. Conversor de Area\n"
    "6. Conversor de Velocidad\n"
    "0. Salir del programa\n"
    "Seleccione: "
)
    if opcion == "1":
        unidades= input("1. Km a M" " 2. M a Cm" " 3. Cm a Mm: ")
        if unidades == "1":
            try:
                n1=float(input("Coloque Km a convertir en M: "))
                resultado= n1 * 1000
                print("Resultado: ", str(resultado)+"M")
            except:
                print("Debe colocar un valor numerico")
        elif unidades == "2":
            try:
                n1=float(input("Coloque M a convertir en Cm: "))
                resultado= n1*100
                print("Resultado: ", str(resultado)+ "Cm")
            except:
                print("Debe colocar un valor numerico")
        elif unidades == "3":
            try:
                n1=float(input("Coloque Cm a convertir en mm: "))
                resultado= n1*10
                print("Resultado: ", str(resultado)+ "Mm")
            except:
                print("Debe colocar un valor numerico")
        else:
            print("Debe ingresar una opcion numerica")
    elif opcion == "2":
        unidades= input("1.Celsius (°C) a Fahrenheit (°F)" " 2.Fahrenheit (°F) a Kelvin (K): ")
        if unidades == "1":
            try:
                n1=float(input("Coloque Celsius (°C) a convertir en Fahrenheit (°F): "))
                resultado = (n1 * 1.8) + 32
                print("Resultado: ", str(resultado)+ "°F")
            except:
                print("Debe colocar un valor numerico")
        elif unidades == "2":
            try:
                n1=float(input("Coloque Fahrenheit (°F) a convertir en Kelvin (K): "))
                resultado= ((n1-32) / 1.8) + 273.15
                print("Resultado: ", str(resultado)+ "K")
            except:
                print("Debe colocar un valor numerico")
        else:
            print("Debe ingresar una opcion numerica")
    elif opcion == "3":
        unidades= input("1.Tn a Kg" " 2.Kg a G" " 3. G a Mg: ")
        if unidades == "1":
            try:
                n1= float(input("Coloque Tn a convertir en Kg: "))
                resultado= n1 *1000
                print("Resultado: ", str(resultado) + "Kg")
            except:
                print("Debe colocar un valor numerico")
        elif unidades =="2":
            try:
                n1= float(input("Coloque Kg a convertir en G: "))
                resultado= n1 *1000
                print("Resultado: ", str(resultado) + "G")
            except:
                print("Debe colocar un valor numerico")
        elif unidades == "3":
            try:
                n1= float(input("Coloque G a convertir en Mg: "))
                resultado= n1 *1000
                print("Resultado: ", str(resultado)+ "Mg")
            except:
                print("Debe colocar un valor numerico")
        else:
            print("Debe ingresar una opcion numerica")
    elif opcion == "4":
        unidades= input("1. Dias a Horas" " 2.Horas a Minutos" " 3.Minutos a Segundos: ")
        if unidades == "1":
            try:
                n1=float(input("Coloque cantidas de dias a convertir en horas: "))
                resultado= n1 *24
                print("Resultado: ", str(resultado) +"h")
            except:
                print("Debe colocar un valor numerico")
        elif unidades == "2":
            try:
                n1=float(input("Coloque cantidas de horas a convertir en minutos: "))
                resultado= n1 *60
                print("Resultado: ", str(resultado) + "min")
            except:
                print("Debe colocar un valor numerico")
        elif unidades == "3":
            try:
                n1=float(input("Coloque cantidas de minutos a convertir en segundos: "))
                resultado= n1 *60
                print("Resultado: ", str(resultado) +"s")
            except:
                print("Debe colocar un valor numerico")    
        else:
            print("Debe ingresar una opcion numerica")
    elif opcion == "5":
        unidades = input("1.Km2 a M2" " 2.M2 a Cm2: ")
        if unidades == "1":
            try:
                n1= float(input("Coloque Km2 que desee convertir a M2: "))
                resultado= n1 *1000000
                print("Resultado: ", str(resultado) +"M2")
            except:
                print("Debe colocar un valor numerico")
        elif unidades == "2":
            try:
                n1= float(input("Coloque M2 que desee convertir a Cm2: "))
                resultado= n1 *10000
                print("Resultado: ", str(resultado) +"Cm2")
            except:
                print("Debe colocar un valor numerico")
        else:
            print("Debe ingresar una opcion numerica")
    elif opcion == "6":
        unidades = input("1.Km/h a M/s" " 2.M/s a Cm/s: ")
        if unidades == "1":
            try:
                n1= float(input("Coloque Km/h que desee convertir a M/s: "))
                resultado= n1 / 3.6
                print("Resultado: ", str(resultado) +"M/s")
            except:
                print("Debe colocar un valor numerico")
        elif unidades == "2":
            try:
                n1= float(input("Coloque M/s que desee convertir a Cm/s: "))
                resultado= n1 * 100
                print("Resultado: ", str(resultado) +"Cm/s")
            except:
                print("Debe colocar un valor numerico")
        else:
            print("Debe ingresar una opcion numerica")
    if opcion == "0":
        print("Saliendo...")
        break                


                


                                



                    









                            
   


    

