import gtts
import playsound
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
while True:
    speak.Speak("enter you want to speak")
    text = input("enter you want to speak: \n : ")
    if "q" in text:
        speak.Speak("Good bye, see you again Dear")
        break
    speak.Speak("you want to language en/fr/hi etc")
    language = input("you want to language en/fr/hi etc:  ")
    language=language.lower()
    speak.Speak("enter the name you want to save with extension")
    saving = input("enter the name you want to save with extension: \n :")
    sound = gtts.gTTS(text,lang=f"{language}")
    saving = saving + ".mp3"
    sound.save(saving)
    playsound.playsound(saving)