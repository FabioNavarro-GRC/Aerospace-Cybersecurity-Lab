import time
import board
import adafruit_dht
import requests
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from confirg import API_KEY # Importamos la clave desde tu archivo config

# Inicialización
dhtDevice = adafruit_dht.DHT22(board.D4)
SECRET_KEY = b'1234567890abcdef' # 16 bytes para AES-128

def encrypt_data(raw_data):
    cipher = AES.new(SECRET_KEY, AES.MODE_ECB)
    padded_data = pad(raw_data.encode(), 16)
    encrypted = cipher.encrypt(padded_data)
    return base64.b64encode(encrypted).decode('utf-8')

while True:
    try:
        t = dhtDevice.temperature
        h = dhtDevice.humidity
        
        if t is not None and h is not None:
            # Creamos el mensaje, lo ciframos y lo preparamos para enviar
            mensaje = f"Temp:{t},Hum:{h}"
            mensaje_cifrado = encrypt_data(mensaje)
            
            print(f"Enviando cifrado: {mensaje_cifrado}")
            
            # NOTA: ThingSpeak recibirá el texto cifrado en el campo 1
            url = f"https://api.thingspeak.com/update?api_key={API_KEY}&field1={mensaje_cifrado}"
            requests.get(url)
            
    except Exception as e:
        print(f"Error: {e}")
        
    time.sleep(20)

    time.sleep(20) # Esperamos 20 segundos

# Si el programa se detiene, liberamos el sensor correctamente
dhtDevice.exit()
