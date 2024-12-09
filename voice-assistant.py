import speech_recognition as sr
import keyboard
import os
import webbrowser
import time

# Inicializar el reconocimiento de voz
recognizer = sr.Recognizer()

def search_google(query):
    """Realiza una búsqueda en Google"""
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def recognize_speech():
    """Inicia el reconocimiento de voz"""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source) 
        audio = recognizer.listen(source, timeout=5)
        try:
            print("Reconociendo...")
            text = recognizer.recognize_google(audio, language="es-ES")
            print(f"Has dicho: {text}")

            # Ejecutar acciones basadas en el comando de voz
            if 'abrir explorador' in text:
                os.system('explorer')
            elif 'buscar' in text:
                query = text.replace("buscar", "").strip()
                search_google(query)
            else:
                print("No reconozco ese comando.")
        except sr.UnknownValueError:
            print("No se ha entendido bien.")
        except sr.RequestError:
            print("Error al conectar con el servicio de reconocimiento de voz.")

def main():
    print("Mantén presionada la tecla F7 para hablar.")

    while True:
        # Verifica si la tecla F7 está presionada
        if keyboard.is_pressed('F7'):
            recognize_speech()
        time.sleep(0.1)  # Esperar un poco antes de revisar nuevamente

if __name__ == "__main__":
    main()
