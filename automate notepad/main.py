#author name: Syed Hamza Ali
#python programming
##########################################################################################
import speech_recognition as sr
import pyttsx3





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine. setProperty("rate", 245)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognising....")
        query = r.recognize_google(audio, language='eng-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print(e)
        print('unable to recognise your voice')
        return "None"
    return query

def notepad():
    speak("i am ready to make your notes")
    print("i am ready to make your notes")
    speak("speak up your notes")
    writes = takeCommand()
    filename = "jarvis-note.txt"
    with open(filename, "w") as file:
        file.write(writes)
    


if __name__=='__main__':
    takeCommand()
    notepad()
