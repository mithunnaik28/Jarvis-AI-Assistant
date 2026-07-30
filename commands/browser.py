import os
import webbrowser

commands = {
    "open youtube": lambda: webbrowser.open("https://www.youtube.com"),

    "open DSA playlist": lambda: webbrowser.open("https://www.youtube.com/watch?v=rga_q2N7vU8&list=PLfqMhTWNBTe137I_EPQd34TsgV6IO55pt&index=4"),
    
    "open github": lambda: webbrowser.open("https://github.com/"),

    "open chrome": lambda: os.system("start chrome"),
    "close chrome": lambda: os.system("taskkill /f /im chrome.exe"),

    "open calculator": lambda: os.system("calc"),
    "close calculator": lambda: os.system("taskkill /f /im calc.exe"),

    "open notepad": lambda: os.system("notepad"),

    "open whatsapp": lambda: os.system("start whatsapp:"),
    "close whatsapp": lambda: os.system("taskkill /f /im WhatsApp:.exe"),
}

def run_command(command):
    for key, action in commands.items():
        if key in command.lower():
            action()
            return key

    return None
