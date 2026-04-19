import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer=sr.Recognizer()
engine= pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


if __name__=="__main__":
    speak("Hello! How are you doing? How may I help you?")
    while True:
        # Listening for wake word 'juice'
        # obtain audio from the microphone
        r=sr.Recognizer()
        with sr.Microphone()

        # recognize sppech using sphinx
        try:
            print
