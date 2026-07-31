import sys
import speech_recognition as sr
import pyttsx3
from commands.browser import run_command

sys.stdout.reconfigure(encoding='utf-8')
# Voice engine

def speak(text):
    text = text.encode("ascii", "ignore").decode()
    print("Jarvis:", text)

    engine = pyttsx3.init()

    engine.setProperty('rate', 170)     # speed
    engine.setProperty('volume', 1.0)   # volume

    engine.say(text)
    engine.runAndWait()

    engine.stop()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command

    except:
        print("Could not understand")
        return ""

speak("Hello, I am Jarvis.")

while True:

    command = listen()

    if command.lower() == "bye":
        speak("Goodbye")
        break

    result = run_command(command)

    if result:
        speak("Opening " + result.replace("open ", ""))
        continue
