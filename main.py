import speech_recognition as sr
import webbrowser
import pyttsx3
# pip install pocketsphinx
 

recognizer=sr.Recognizer()
engine= pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    pass

if __name__=="__main__":
    speak("Hello! How are you doing? How may I help you?")
    while True:
        # Listening for wake word 'juice'
        # obtain audio from the microphone
        r=sr.Recognizer()
        
        # recognize sppech using sphinx
        try:
            with sr.Microphone() as source:
                print('Listening....')
                audio=r.listen(source,timeout=2,phrase_time_limit=2)
            print('Recognizing....')
            word=r.recognize_google(audio)
            if(word.lower()=="juice"):
                speak("Ya")
                with sr.Microphone() as source:
                    print('Active......')
                    audio=r.listen(source)
                    command=r.recognize_google(audio)

                    processCommand()
                # listen for command
            # print(command)
        except Exception as e:
            print("Didn't catch that.Error-> ",e)
