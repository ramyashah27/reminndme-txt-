import speech_recognition as s 
import pyttsx3
import time
clock= time.ctime()
engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[1].id)
def speak(audio):

    engine.say(audio) 
    engine.runAndWait()

speak('ehat u  want me to remind')
print('ehat u  want me to remind')
print("I AM LISTING,HOW MAY I HELP U please TELL")

sr=s.Recognizer()
with s.Microphone() as m:
    audio=sr.listen(m)
    query=sr.recognize_google(audio,language='eng-in')
    # querytt=(query,"at", clock)
    querytt=(f"you told me to remind {query} at {clock}")
    querytt=str(querytt)
    print(query)
with open("remindme.txt" ,"w") as f:
    f.write(querytt)
time.sleep(5)
with open("remindme.txt") as rem:
    talk= rem.read()

speak(talk)


# with s.Microphone() as m:
#     audio=sr.listen(m)
#     query=sr.recognize_google(audio,language='eng-in')
#     print(query)