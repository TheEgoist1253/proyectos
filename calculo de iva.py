def impuesto_iva(producto,Iva):
    if not isinstance(producto,(float,int)):
        return "producto debe ser un numero"
    if not isinstance(Iva,(float,int)):
        return "Iva debe ser un numero porcentaje"

    return producto * (Iva/100)
    

try:
    producto = float(input("coloque precio del producto a calcular Iva: "))
    Iva = float(input("coloque Iva: "))
except:
    print("Debes ingresar valores numéricos")
    exit()


impuesto = impuesto_iva(producto, Iva)

if isinstance(impuesto, str):
    print(impuesto)
    exit()

print("IVA calculado:", impuesto , "$")

precio_mas_impuesto=input("Quiere sumar el Iva al producto?, (S)i-(N)o ").lower()

if precio_mas_impuesto == "s":
    precio_absoluto= producto + impuesto
    print("El precio total seria: " , str(round(precio_absoluto,2)) , "$")
elif precio_mas_impuesto == "n":
    print("Operancion finalizada")
else:
    print("opcion no valida")     



    


