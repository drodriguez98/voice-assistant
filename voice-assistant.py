import speech_recognition as sr

# Crear un objeto de reconocimiento de voz
recognizer = sr.Recognizer()

# Iniciar el micrófono
with sr.Microphone() as source:
    print("Ajustando el ruido ambiental...")
    # Ajustar el ruido ambiental
    recognizer.adjust_for_ambient_noise(source)
    print("Listo para escuchar. Di algo...")

    while True:
        try:
            # Escuchar el audio
            audio = recognizer.listen(source)
            print("Reconociendo...")

            # Intentar reconocer el audio con Google Speech Recognition
            text = recognizer.recognize_google(audio, language="es-ES")
            print(f"Lo que dijiste: {text}")

            # Si se dice "adiós", salir del bucle y terminar el programa
            if "adiós" in text.lower():
                print("¡Hasta luego!")
                break
        
        except sr.UnknownValueError:
            # Si no se puede entender lo que se dijo
            print("No se pudo entender lo que dijiste.")
        
        except sr.RequestError:
            # Si hay un problema con la conexión a Google
            print("Error con el servicio de reconocimiento de voz.")
