import pyttsx3
import webbrowser as wb

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',rate-40)
volume = engine.getProperty('volume')
engine.setProperty('volume',volume + 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

while True:
    
    text = input("")
    if(text == 'open facebook'):
        wb.get('windows-default').open('https://www.facebook.com/')
        engine.say("Your Facebook Account is Accessed")
        engine.runAndWait();
