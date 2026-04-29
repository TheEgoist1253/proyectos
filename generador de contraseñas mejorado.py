import secrets
import string

def generar_contraseña(longitud, usar_mayus=True, usar_numeros=True, usar_simbolos=True):
    if longitud < 4:
        return "La longitud debe ser al menos 4"

    caracteres = string.ascii_lowercase
    contraseña = []

    if usar_mayus:
        caracteres += string.ascii_uppercase
        contraseña.append(secrets.choice(string.ascii_uppercase))

    if usar_numeros:
        caracteres += string.digits
        contraseña.append(secrets.choice(string.digits))

    if usar_simbolos:
        caracteres += string.punctuation
        contraseña.append(secrets.choice(string.punctuation))

    # completar el resto
    while len(contraseña) < longitud:
        contraseña.append(secrets.choice(caracteres))

    # mezclar
    secrets.SystemRandom().shuffle(contraseña)

    return "".join(contraseña)


try:
    longitud = int(input("Longitud de la contraseña: "))
    psw = generar_contraseña(longitud)
    print("Contraseña:", psw)
except:
    print("Debes ingresar un número válido")