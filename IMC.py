import tkinter as tk

def calcular_imc():
    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())
        imc = peso / (altura ** 2)
        resultado = f"Tu IMC es: {imc:.2f}\n"

        if imc < 18.5:
            resultado += "Estás por debajo del peso normal."
        elif 18.5 <= imc and imc < 25:
            resultado += "¡Estás en un peso saludable! 🟢"
        elif 25 <= imc and imc < 30:
            resultado += "Tienes sobrepeso. ⚠️"
        else:
            resultado += "Tienes obesidad. 🔴"

        etiqueta_resultado.config(text=resultado)
    except ValueError:
        etiqueta_resultado.config(text="Por favor ingresá números válidos.")

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de IMC")
ventana.geometry("400x400")

# Etiquetas y entradas
tk.Label(ventana, text="Peso (kg):").pack(pady=15)
entrada_peso = tk.Entry(ventana)
entrada_peso.pack()

tk.Label(ventana, text="Altura (m):").pack(pady=15)
entrada_altura = tk.Entry(ventana)
entrada_altura.pack()

# Botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular IMC", command=calcular_imc)
boton_calcular.pack(pady=15)

# Resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12))
etiqueta_resultado.pack(pady=10)

# Ejecutar
ventana.mainloop()