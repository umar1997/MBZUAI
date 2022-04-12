# https://pyttsx3.readthedocs.io/en/latest/engine.html#module-pyttsx3.voice
import pyttsx3

engine = pyttsx3.init() # object creation

# engine.say("I will speak this text")
# engine.runAndWait()

########### RATE ###########
rate = engine.getProperty('rate') # getting details of current speaking rate
print (rate) #printing current voice rate
engine.setProperty('rate', 125) # setting up new voice rate

########### VOLUME ###########
volume = engine.getProperty('volume') #getting to know current volume level (min=0 and max=1)
print (volume) #printing current volume level
engine.setProperty('volume',1.0) # setting up volume level between 0 and 1

########### VOICE ########### 
voices = engine.getProperty('voices') #getting details of current voice
# for i, v in enumerate(voices):
#     print(v[i].id)
print(pyttsx3.voice.Voice)
#engine.setProperty('voice', voices[0].id) #changing index, changes voices. 0 for male
engine.setProperty('voice', voices[1].id) #changing index, changes voices. 1 for female

# for voice in voices:
#     print (voice)
#     if voice.languages[0] == u'en_US':
#         engine.setProperty('voice', voice.id)

for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
# engine.say("Hello World!")
# engine.say('My current speaking rate is ' + str(rate))
# engine.runAndWait()
# engine.stop()

########### Saving Voice to a file ########### 
# On linux make sure that 'espeak' and 'ffmpeg' are installed
# engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()