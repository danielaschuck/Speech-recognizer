import speech_recognition as sr


rec=sr.Recognizer()
with sr.Microphone(0) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("pode começar")
    audio=rec.listen(mic)
    text=rec.recognize_google(audio,language="pt-BR")
    print(text)

