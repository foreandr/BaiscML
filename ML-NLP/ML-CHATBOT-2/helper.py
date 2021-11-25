import speech_recognition as sr
from gtts import gTTS
import transformers
import os
import datetime

'''
USING GUIDE
    main:
    ai = helper.ChatBot(name="DevBot")
    # while True:
    #    ai.speech_to_text()


    nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
    input_text = "hello!"
    nlp(transformers.Conversation(input_text), pad_token_id=50256)

    chat = nlp(transformers.Conversation(ai.text), pad_token_id=50256)
    res = str(chat)
    res = res[res.find("bot >> ") + 6:].strip()

'''
class ChatBot():
    def __init__(self, name):
        print("----- starting up", name, "-----")
        self.name = name

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("listening...")
            audio = recognizer.listen(mic)
        try:
            self.text = recognizer.recognize_google(audio)
            print("me --> ", self.text)
        except:
            print("me -->  ERROR")

    def wake_up(self, text):
        return True if self.name in text.lower() else False

    @staticmethod
    def text_to_speech(text):
        print("AI --> ", text)
        speaker = gTTS(text=text, lang="en", slow=False)
        speaker.save("res.mp3")
        os.system("start res.mp3")  # if you have a macbook->afplay or for windows use->start
        os.remove("res.mp3")

    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')

