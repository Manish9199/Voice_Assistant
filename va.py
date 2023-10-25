import pyttsx3
import webbrowser
import speech_recognition as sr
import time
import pyjokes
import os
import pygame

music_directory = r'C:\Users\DELL\Documents\VS_Code\PYTHON\Music player in python\Music\music_file'

def play_music(filename):
    pygame.mixer.init()
    music_file = os.path.join(music_directory, filename)
    if os.path.exists(music_file):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
    else:
        print("File not found: " + filename)

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        command = ""
        try:
            command = r.recognize_google(audio)
            print("You said: " + command)
        except sr.UnknownValueError:
            pass
        return command.lower()

def tell_joke():
    joke = pyjokes.get_joke()
    print("Assistant: " + joke)
    speak(joke)

def assistant():
    while True:
        command = listen()
        
        if "hey peter" in command:
            speak("Hello! How can I assist you?")
            current_time = time.strftime("%H:%M:%S")
            print(f"The current time is {current_time}")
            speak(f"The current time is {current_time}")
        
        if "tell me a joke" in command:
            tell_joke()

        if "open browser" in command:
            speak("Opening the browser")
            webbrowser.open("https://www.google.com")
        elif "open YouTube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        elif "open Google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif "play music" in command:
            play_music('my_music_file.mp3')
        elif "exit" in command:
            speak("Goodbye!")
            exit()

        time.sleep(1)  

assistant()
