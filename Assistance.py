import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data.lower()  # Convert the recognized text to lowercase for easier comparisons
        except sr.UnknownValueError:
            print("Not Understand")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 120)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    while True:
        data1 = sptext().lower()
        if "what is your name" in data1:
            name = "my name is ishu how can i help you"
            speechtx(name)
        elif "how old are you" in data1:
            age = "I am one day old"
            speechtx(age)
        elif "time " in data1:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speechtx(time)
        elif "open web" in data1:
            webbrowser.open("https://www.linkedin.com/in/akash-deep-srivastava-06a819212/")
        elif "open youtube" in data1:
            webbrowser.open("https://www.youtube.com/")
        elif "open Github" in data1:
            webbrowser.open("https://github.com/AkashDeepSri01/Data-science-course")
        elif "tell me some joke" in data1:
            joke_1 = pyjokes.get_joke(language="en", category="neutral")
            speechtx(joke_1)
        elif 'play a song' in data1:
            add = r'D:\New folder\mp4'# You need to add code here to handle playing specific songs
            listsong = os.listdir(add)
            print(listsong)
            os.startfile(os.path.join(add, listsong[0]))
        elif "exit" in data1:
            speechtx("Thank you")
            break
