import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
voices = engine.getProperty('voices')

def guySpeak():
    engine.setProperty('voice', voices[0].id)

def girlSpeak():
    engine.setProperty('voice', voices[1].id)

girlSpeak()
engine.setProperty('volume',0.6)
engine.setProperty('rate', 100)
engine.say('So Class, What do we know about World War 2?')


engine.setProperty('volume',1.0)
engine.setProperty('rate', 120)
engine.say('What are you doing Henry?')

guySpeak()
engine.setProperty('volume',0.7)
engine.setProperty('rate', 110)
engine.say('Nothing Miss, Some birds were pecking at the window.')


girlSpeak()
engine.setProperty('volume',1.0)
engine.setProperty('rate', 130)
engine.say('Stop looking at the window. And pay attention to whats being taught in class.')


guySpeak()
engine.setProperty('volume',0.7)
engine.setProperty('rate', 110)
engine.say('Sorry Miss, I will try and be more attentive from now on.')

girlSpeak()
engine.setProperty('volume',0.6)
engine.setProperty('rate', 110)
engine.say('Okay so where were we?')
engine.say('Right! World War 2')

engine.runAndWait()