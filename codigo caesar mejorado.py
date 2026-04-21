def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = -shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    return text.translate(translation_table)


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


#usuario
text = input("Ingrese el texto: ")

try:
    shift = int(input("Ingrese el valor de shift (1-25): "))
except:
    print("El shift debe ser un número.")
    exit()

mode = input("¿Quieres (e)ncriptar o (d)esencriptar?: ").lower()

if mode == "e":
    result = encrypt(text, shift)
    print("Texto codificado:", result)
elif mode == "d":
    result = decrypt(text, shift)
    print("Texto decodificado:", result)
else:
    print("Opción no válida")