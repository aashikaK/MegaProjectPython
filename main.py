import webbrowser
# # pip install pocketsphinx
import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print("Command received:", c)

if __name__ == "__main__":
    speak("Hello. How may I help you?")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            word = recognizer.recognize_google(audio)
            print("Heard:", word)

            if "fan" in word.lower():
                speak("Ya")

                with sr.Microphone() as source:
                    print("Active mode...")
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                print("Command:", command)

                processCommand(command)

        except Exception as e:
            print("Error:", e)