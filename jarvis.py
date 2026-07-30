import sys
import ollama
import speech_recognition as sr
import pyttsx3
import webbrowser
import os

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

def ask_jarvis(question):
    response = ollama.chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    answer = response["message"]["content"]
    return answer[:100]


speak("Hello, I am Jarvis. How can I help you?")

while True:

    command = listen()

    if command.lower() == "exit":
        speak("Goodbye")
        break
    
    if "open chrome" in command.lower():
        os.system("start chrome")
        speak("Opening Chrome")
        continue

    elif "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
        continue

    elif "open google" in command.lower():
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
        continue

    if command:
        answer = ask_jarvis(command)
        speak(answer)

# still builting
