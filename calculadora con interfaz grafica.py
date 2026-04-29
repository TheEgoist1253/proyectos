import tkinter as tk
from tkinter import ttk

def convertir():
    try:
        valor = float(entrada.get())
        tipo = combo_tipo.get()
        unidad = combo_unidad.get()

        if tipo == "Longitud":
            if unidad == "Km a M":
                resultado = valor * 1000
                texto = "M"
            elif unidad == "M a Cm":
                resultado = valor * 100
                texto = "Cm"
            elif unidad == "Cm a Mm":
                resultado = valor * 10
                texto = "Mm"

        elif tipo == "Temperatura":
            if unidad == "°C a °F":
                resultado = (valor * 1.8) + 32
                texto = "°F"
            elif unidad == "°F a K":
                resultado = ((valor - 32) / 1.8) + 273.15
                texto = "K"

        elif tipo == "Masa":
            if unidad == "Tn a Kg":
                resultado = valor * 1000
                texto = "Kg"
            elif unidad == "Kg a G":
                resultado = valor * 1000
                texto = "G"
            elif unidad == "G a Mg":
                resultado = valor * 1000
                texto = "Mg"

        elif tipo == "Tiempo":
            if unidad == "Días a Horas":
                resultado = valor * 24
                texto = "h"
            elif unidad == "Horas a Minutos":
                resultado = valor * 60
                texto = "min"
            elif unidad == "Minutos a Segundos":
                resultado = valor * 60
                texto = "s"

        elif tipo == "Área":
            if unidad == "Km2 a M2":
                resultado = valor * 1_000_000
                texto = "M2"
            elif unidad == "M2 a Cm2":
                resultado = valor * 10_000
                texto = "Cm2"

        elif tipo == "Velocidad":
            if unidad == "Km/h a M/s":
                resultado = valor / 3.6
                texto = "M/s"
            elif unidad == "M/s a Cm/s":
                resultado = valor * 100
                texto = "Cm/s"

        etiqueta_resultado.config(text=f"Resultado: {resultado} {texto}")

    except:
        etiqueta_resultado.config(text="Ingrese un número válido")


def actualizar_unidades(event):
    tipo = combo_tipo.get()

    if tipo == "Longitud":
        combo_unidad["values"] = ["Km a M", "M a Cm", "Cm a Mm"]
    elif tipo == "Temperatura":
        combo_unidad["values"] = ["°C a °F", "°F a K"]
    elif tipo == "Masa":
        combo_unidad["values"] = ["Tn a Kg", "Kg a G", "G a Mg"]
    elif tipo == "Tiempo":
        combo_unidad["values"] = ["Días a Horas", "Horas a Minutos", "Minutos a Segundos"]
    elif tipo == "Área":
        combo_unidad["values"] = ["Km2 a M2", "M2 a Cm2"]
    elif tipo == "Velocidad":
        combo_unidad["values"] = ["Km/h a M/s", "M/s a Cm/s"]

    combo_unidad.current(0)



ventana = tk.Tk()
ventana.title("Conversor de Unidades")
ventana.geometry("400x300")

tk.Label(ventana, text="Conversor de Unidades", font=("Arial", 16)).pack(pady=10)


tk.Label(ventana, text="Seleccione tipo:").pack()
combo_tipo = ttk.Combobox(ventana, values=[
    "Longitud", "Temperatura", "Masa", "Tiempo", "Área", "Velocidad"
])
combo_tipo.pack()
combo_tipo.bind("<<ComboboxSelected>>", actualizar_unidades)


tk.Label(ventana, text="Seleccione conversión:").pack()
combo_unidad = ttk.Combobox(ventana)
combo_unidad.pack()


tk.Label(ventana, text="Ingrese valor:").pack()
entrada = tk.Entry(ventana)
entrada.pack()


tk.Button(ventana, text="Convertir", command=convertir).pack(pady=10)


etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12))
etiqueta_resultado.pack()

ventana.mainloop()



