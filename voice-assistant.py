import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen():

    with sr.Microphone() as source:
        print("Diga algo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Reconociendo...")
        query = recognizer.recognize_google(audio, language='es-ES')
        print(f"Tú: {query}")
        return query
    
    except sr.UnknownValueError:
        return "No te entendí"
    
    except sr.RequestError:
        return "Lo siento, no pude acceder al servicio de reconocimiento de voz"

def speak(text):

    engine.say(text)
    engine.runAndWait()

def main():

    speak("Hola, soy tu asistente de voz. ¿En qué puedo ayudarte?")
    
    while True:
        query = listen().lower()
        
        if 'detener' in query or 'salir' in query:
            speak("Adiós, hasta luego")
            break

        if 'nombre' in query:
            speak("Mi nombre es Asistente de Voz")

if __name__ == "__main__":
    main()
