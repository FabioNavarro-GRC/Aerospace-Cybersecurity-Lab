import serial
import struct
from Crypto.Cipher import AES
import time

# --- CONFIGURACIÓN ---
KEY = bytes([your key here])

# Asegúrate de usar ttyAMA0 que es el puerto físico UART de la RPi 4
SERIAL_PORT = '/dev/ttyAMA0'
BAUD_RATE = 9600

def decrypt_data(encrypted_data):
    cipher = AES.new(KEY, AES.MODE_ECB)
    decrypted = cipher.decrypt(encrypted_data)
    # 'ff' indica dos números float (4 bytes cada uno)
    h, t = struct.unpack('ff', decrypted[:8])
    return h, t

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    ser.reset_input_buffer() # Limpiar basura al iniciar
    print(f"Escuchando en {SERIAL_PORT}...")
except Exception as e:
    print(f"Error al abrir el puerto: {e}")
    exit()

try:
    while True:
        # Esperar a tener al menos 16 bytes (el tamaño de tu bloque AES)
        if ser.inWaiting() >= 16:
            raw_data = ser.read(16)
            
            # --- DIAGNÓSTICO ---
            print(f"Bytes recibidos (hex): {raw_data.hex()}")
            
            try:
                humidity, temp = decrypt_data(raw_data)
                print(f"--> Humedad: {humidity:.2f}% | Temperatura: {temp:.2f}°C")
            except Exception as e:
                print(f"Error al descifrar (posible desalineación): {e}")
                ser.reset_input_buffer() # Forzar sincronización si hay error
        
        time.sleep(0.1) # Pequeña pausa para no saturar la CPU

except KeyboardInterrupt:
    print("\nDeteniendo escucha...")
finally:
    ser.close()
