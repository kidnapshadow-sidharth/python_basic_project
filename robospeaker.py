import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
print("Welcome to RoboSpeaker 2.2 Created by kidnapshadow")

while True:
    text = input("Enter what you want to speak \n : ")
    if text =="exit":
        break
    speak.Speak(text)
  
