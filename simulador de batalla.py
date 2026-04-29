#Simulador de combate

Personaje = "Edrick"
vidaHeroe = 500
atqheroe = 240
defensaheroe = 5
esquiveheroe = 0.2
aciertoheroe = 0.8

Enemigo = "Esqueleto"
vidaenemigo = 1200
atqenemigo = 50
defensaenemigo = 8
esquiveenemigo = 0.3
aciertoenemigo = 0.5

print("Bienvenido a simulador de batalla\n")
import random

while True:
    lanzamiento_dado = input("¿Lanzas dado? (S/N): ").upper()

    if lanzamiento_dado == "S":
        dado = random.randint(1, 6)
        print("Salió:", dado)

        if dado < 4:
            print(f"Ataca {Personaje}")

            prob_final = max(0, aciertoheroe - esquiveenemigo)
            if random.random() < prob_final:
                daño = max(0, atqheroe - defensaenemigo)
                vidaenemigo -= daño
                print(f"💥 Golpea e inflige {daño} de daño")
                print(f"Vida restante de {Enemigo}: {vidaenemigo}")
            else:
                print("💨 Esquivado")

        else:
            print(f"Ataca {Enemigo}")

            prob_final = max(0, aciertoenemigo - esquiveheroe)
            if random.random() < prob_final:
                daño = max(0, atqenemigo - defensaheroe)
                vidaHeroe -= daño
                print(f"💥 Golpea e inflige {daño} de daño")
                print(f"Vida restante de {Personaje}: {vidaHeroe}")
            else:
                print("💨 Esquivado")

        
        if vidaenemigo <= 0:
            print(f"🏆 {Personaje} ganó!")
            break
        elif vidaHeroe <= 0:
            print(f"💀 {Enemigo} ganó!")
            break

    elif lanzamiento_dado == "N":
        print("Héroe se escapa...")
        break

    else:
        print("Opción inválida")


        


