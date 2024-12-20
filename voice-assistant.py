# Librerías necesarias: pyttsx3, keyboard, os, webbrowser, time, datetime, requests, speech_recognition
import pyttsx3
import keyboard
import webbrowser
import time
from datetime import datetime
import speech_recognition as sr
# import os
# import requests

# Función para configurar e inicializar el motor de voz
def inicializar_voz():
    """Configura el motor de síntesis de voz."""
    motor = pyttsx3.init()
    motor.setProperty('rate', 125)  # Velocidad del habla
    motor.setProperty('volume', 0.85)  # Volumen
    return motor

# Función para convertir texto a voz
def hablar(motor, texto):
    """Convierte texto a voz."""
    motor.say(texto)
    motor.runAndWait()

# Función para realizar una búsqueda en Google
def realizar_busqueda(consulta):
    """Abre el navegador para realizar una búsqueda en Google."""
    url = f"https://www.google.com/search?q={consulta}"
    webbrowser.open(url)
    return f"Buscando {consulta} en Google."

# Función para reconocer el comando de voz del usuario
def reconocer_voz():
    """Reconoce el comando de voz del usuario."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
    try:
        comando = recognizer.recognize_google(audio, language="es-ES")
        print(f"Tú: {comando}")
        return comando.lower()
    except sr.UnknownValueError:
        return "No entendí lo que dijiste."
    except sr.RequestError:
        return "Error al conectar con el servicio de reconocimiento de voz."

def main():
    # Inicializar el motor de voz
    motor = inicializar_voz()
    # Saludo inicial
    hablar(motor, "Hola, estoy listo para ayudarte.")
    print("Mantén presionada la tecla F7 para hablar.")
    hablar(motor, "Mantén presionada la tecla F7 para hablar.")
    # Bucle infinito hasta que el usuario diga "salir" o "adiós"
    while True:
        # Usar la tecla F7 para activar el asistente de voz
        if keyboard.is_pressed('F7'):
            hablar(motor, "¿Qué deseas hacer?")
            comando = reconocer_voz()
            # Cerrar el asistente
            if "salir" in comando or "adiós" in comando:
                hablar(motor, "Hasta luego.")
                break
            # Hacer búsquedas en Google
            elif "buscar" in comando:
                hablar(motor, "¿Qué deseas buscar?")
                consulta = reconocer_voz()
                resultado_busqueda = realizar_busqueda(consulta)
                hablar(motor, resultado_busqueda)
            # Cambiar volumen de habla del asistente de voz
            elif "sube el volumen" in comando:
                volumen_actual = motor.getProperty('volume')
                if volumen_actual < 1.0:
                    motor.setProperty('volume', min(volumen_actual + 0.1, 1.0))
                    hablar(motor, "El volumen ha sido aumentado.")
            elif "baja el volumen" in comando:
                volumen_actual = motor.getProperty('volume')
                if volumen_actual > 0.0:
                    motor.setProperty('volume', max(volumen_actual - 0.1, 0.0))
                    hablar(motor, "El volumen ha sido reducido.")
            # Cambiar velocidad de habla del asistente de voz
            elif "más rápido" in comando:
                velocidad_actual = motor.getProperty('rate')
                motor.setProperty('rate', velocidad_actual + 10)
                hablar(motor, "He aumentado la velocidad de habla.")
            elif "más lento" in comando:
                velocidad_actual = motor.getProperty('rate')
                motor.setProperty('rate', max(velocidad_actual - 10, 50))
                hablar(motor, "He reducido la velocidad de habla.")
            # Comandos no reconocidos
            else:
                hablar(motor, "No reconozco ese comando.")
        time.sleep(0.1)

if __name__ == "__main__":
    main()