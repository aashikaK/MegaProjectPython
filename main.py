import speech_recognition as sr
import webbrowser
import pyttsx3
import subprocess
import musicLibrary
import requests
from gtts import gTTS
from openai import OpenAI
import pygame
import os
# pip install pocketsphinx
 

r=sr.Recognizer()
engine= pyttsx3.init()
newsapi="NEWS API KEY"


client = OpenAI(api_key='your's openAI api key')

def ask_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
             {"role": "system", "content": "You are a helpful voice assistant.You give short responses"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content



def speak_old(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()
#     # subprocess.run(
#     #     ["powershell", "-Command", f'Add-Type -AssemblyName System.Speech; '
#     #      f'$s = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
#     #      f'$s.Speak("{text}")'],
#     #     check=True
#     # )



def speak(text):
    tts=gTTS(text)
    tts.save('temp.mp3')

    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()

# keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove('temp.mp3')
    
def processCommand(c):
    # print("Command:", c)
    # input("Press Enter to continue...")
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")

    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r= requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        # if r.status_code==200:
        data = r.json()

        headlines = [article["title"] for article in data["articles"][:5]]

        for i in range(0, len(headlines), 2):   # 2 at a time
            chunk = ". ".join(headlines[i:i+2])
            print(chunk)
            speak(chunk)
    else:
        # let openAi handle the requests
        output=ask_ai(c)
        speak(output)


if __name__=="__main__":
    speak("Hello!How may I help you?")
    
    while True:
        # Listening for wake word 'moon'
        # obtain audio from the microphone
        
        # recognize speech using sphinx
        try:
            with sr.Microphone() as source:
                print('Listening....')
                audio=r.listen(source,timeout=5,phrase_time_limit=2)
            
            word=r.recognize_google(audio)
            if "moon" in word.lower():
                speak("yeah")
                with sr.Microphone() as source:
                    print('Active......')
                    audio=r.listen(source)
                    command= r.recognize_google(audio)

                processCommand(command)
                
        except Exception as e:
            print("Didn't catch that.Error-> ",e)  
