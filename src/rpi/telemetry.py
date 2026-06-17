import time
import board
import adafruit_dht
import requests
import sys

# Inicializamos el sensor UNA VEZ fuera del bucle
dhtDevice = adafruit_dht.DHT22(board.D4)
API_KEY = "5M5FSWPCOTFQAGK9"

print("Sistema de telemetría iniciado. Presiona Ctrl+C para salir.")

while True:
    try:
        # Intentamos leer
        t = dhtDevice.temperature
        h = dhtDevice.humidity
        
        if t is not None and h is not None:
            print(f"Enviando... Temp: {t}C, Hum: {h}%")
            url = f"https://api.thingspeak.com/update?api_key={API_KEY}&field1={t}&field2={h}"
            requests.get(url)
        
    except RuntimeError as error:
        # Los errores de lectura son normales en el DHT22, simplemente ignoramos y reintentamos
        print(f"Error de lectura (normal): {error.args[0]}")
    except Exception as e:
        print(f"Error inesperado: {e}")
        break

    time.sleep(20) # Esperamos 20 segundos

# Si el programa se detiene, liberamos el sensor correctamente
dhtDevice.exit()
