import tkinter as tk
import requests

def buscar_clima():
    ciudad = "New York City"  # Cambia la ciudad a tu gusto
    api_key = "a2b3b130836df2b29363946fccb90e93"  # Reemplaza con tu clave de API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        response = response.json()
        clima = response["weather"][0]["description"]
        temperatura = response["main"]["temp"]
        celsius = (temperatura-32)/1.8
        humedad = response["main"]["humidity"]
        presion = response["main"]["pressure"]
        viento = response["wind"]["speed"]
        
        resultado = f"Clima: {clima}\n Temperatura: {temperatura}\n Hummedad: {humedad}\n Presión: {presion}\n Viento: {viento}"
        

    else:
        resultado = "Error al obtener datos del clima."

    label_resultado.config(text=resultado, wraplength=300)

window = tk.Tk()
window.title("Busca tu pokemon")

button_buscar = tk.Button(window, text="Buscar", command= buscar_clima)
button_buscar.pack()

label_resultado = tk.Label(window, text="")
label_resultado.pack()

label_imagen = tk.Label(window)
label_imagen.pack()

window.mainloop()