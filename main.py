import speech_recognition as sr
import webbrowser
import pyttsx3
import subprocess
# pip install pocketsphinx
 

recognizer=sr.Recognizer()
engine= pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    # subprocess.run(
    #     ["powershell", "-Command", f'Add-Type -AssemblyName System.Speech; '
    #      f'$s = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
    #      f'$s.Speak("{text}")'],
    #     check=True
    # )

def processCommand(c):
    print("Command:", c)
    input("Press Enter to continue...")

if __name__=="__main__":
    speak("Hello!How may I help you?")
    
    while True:
        # Listening for wake word 'fan'
        # obtain audio from the microphone
        r=sr.Recognizer()
        # recognize speech using sphinx
        try:
            with sr.Microphone() as source:
                print('Listening....')
                audio=r.listen(source,timeout=2,phrase_time_limit=2)
            
            word=r.recognize_google(audio)
            if "fan" in word.lower():
                speak("Ya")
                with sr.Microphone() as source:
                    print('Active......')
                    audio=r.listen(source)
                    command= r.recognize_google(audio)
                    print("Command:", command)

                processCommand(command)
                
        except Exception as e:
            print("Didn't catch that.Error-> ",e)  