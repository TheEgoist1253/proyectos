import os
import time

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def carro(nombre, carga, posicion):
    
    ruedas = "o" + " " * (len(nombre) + 6) + "o"
    
   
    cuerpo = "[" + nombre + " " + "#" * carga + " " * (10 - carga) + "]"
    
    
    espacio = " " * posicion
    
    return espacio + cuerpo + "\n" + espacio + ruedas

coca_carga = 0
pepsi_carga = 0
coca_pos = 0
pepsi_pos = 0

while True:
    limpiar()
    
    print("\n   SIMULACIÓN DE CARROS\n")

    # Dibujo
    print(carro("COCA", coca_carga, coca_pos))
    print()
    print(carro("PEPSI", pepsi_carga, pepsi_pos))

    
    coca_carga = (coca_carga + 1) % 11
    pepsi_carga = (pepsi_carga + 2) % 11

    coca_pos = (coca_pos + 1) % 30
    pepsi_pos = (pepsi_pos + 2) % 30

    time.sleep(0.1)