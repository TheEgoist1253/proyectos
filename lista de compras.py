lista = []

while True:
    producto = input("AGREGUE PRODUCTO: ").strip()

    if producto == "":
        print("Error: el producto no puede estar vacío")
        continue
    while True:
            entrada = input("Coloque precio esperado del producto: ")
            entrada = entrada.replace(",", ".")

            try:
                precio = float(entrada)

                if precio < 0:
                    print("Error: el precio no puede ser negativo")
                    continue

                break
            except ValueError:
                print("Error: debe ingresar un número válido")
    
    lista.append((producto, precio))  

    print("\nLISTA DE COMPRAS:")
    for p, pr in lista:
        print(p, "-", pr, "$")

    continuar = input("¿Quiere agregar más productos?, (S/N): ").upper()
    
    if continuar != "S":
        print("\nLISTA FINAL DE COMPRAS:")
        for p, pr in lista:
            print(f"{p} - {pr} $")
        break
    

Suma_precio= input("Quiere sumar todos los precios?, (S)i o (N)o): ").upper()
if Suma_precio == "S":
    total = 0
    for p, pr in lista:
        total += pr
    print("TOTAL:", total, "$")



guardar = input("¿Quiere guardar la lista en un archivo? (S/N): ").upper()

if guardar == "S":
    with open("lista_compras.txt", "w") as archivo:
        archivo.write("LISTA DE COMPRAS:\n")

        for p, pr in lista:
            archivo.write(f"{p} - {pr} $\n")

        total = sum(pr for _, pr in lista)
        archivo.write(f"\nTOTAL: {total} $\n")

    print("Archivo guardado como 'lista_compras.txt'")

elif Suma_precio == "N":
    print("Hasta luego usuario")




        



