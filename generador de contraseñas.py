import random
import string as s

def generar_contraseña(longitud):
    caracteres= s.ascii_letters + s.digits + s.punctuation
    contraseña= "".join(random.choice(caracteres) for i in range(longitud))
    return contraseña

longitud= int(input("coloque de que longitud requiere la contraseña"))
psw= generar_contraseña(longitud)
print("Contraseña: ", psw)



