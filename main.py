"""
@author Zero
"""
import os
import speech_recognition as sr
from config import open_ccleaner, open_chrome, open_steam, shutdown_computer, close_steam, close_ccleaner, close_chrome
import subprocess
import webbrowser
import eel
import g4f
import pyowm
import pyttsx3

tts = pyttsx3.init()    
voices = tts.getProperty('voices')
tts.setProperty('voice', 'ru') 
tts.setProperty("rate", 180)
tts.setProperty("volume", 1)

#there is u can put ur file way
ccleaner = r"C:\Program Files\CCleaner\CCleaner64.exe"
steam = r"D:\steam\steam.exe"
chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

#there is u can write ur code words
hello = {"привет":1,"приветсвую":1,"добрый день":1,"добрый вечер":1,"вечер добрый":1,"день добрый":1,"доброе утро":1,"утро доброе":1,}
goodbye = {"пока":1,"вырубайся":1,"выключайся":1,"покеда":1,"прощай":1,"выход":1,}

steam_opener = {'открой стим': 1, 'открой steam': 2, 'хочу поиграть':3}
steam_closer = {'закрой стим': 1, 'закрой steam': 2, 'не хочу поиграть':3, 'не хочу играть':3}

ccleaner_opener = {'открой ccleaner': 1, 'открой клинер': 2, 'почисти комп':3, 'почисти пк':4, 'почисти компьютер':5, 'открой player':6,'открой layer':7}
ccleaner_closer = {'закрой ccleaner': 1, 'закрой клинер': 2, 'открой player':6,'открой layer':7}

chrome_opener = {'открой chrome': 1, 'открой хром': 2, 'открой браузер':3, 'зайди в браузер':4}
chrome_closer = {'закрой хром': 1, 'закрой chrome': 2, 'закрой браузер':4}

computer_shutdown = {'выключи пока':1, 'выключи пк':1, 'выключи комп':1, 'выключи компьютер':1,}

search_google = {'найди':1,'ищи':1,'search':1,'find':1}
search_youtube = {'ютуб':1,'видео':1,'search':1,'find':1,'включи на ютуб':1,'включи видео':1,'ключи видео':1,'ключи ютуб':1,'youtube':1,'ключи на youtub':1,'найди на youtub':1,'найди на ютуб':1}

chat_gpt = {'ответь при помощи нейронки':1,'ответь при помощи нейросети':1,'ответь используя нейронку':1,"ответь используя нейросеть":1,"напиши ответ используя нейросеть":1,"напиши ответ используя нейронку":1}

tts.say('Здравствуйте')
print("Здравствуйте")

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Что прикажете сделать, хозяин:")
        tts.say('Что прикажете сделать, хозяин:')
        tts.runAndWait()
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="ru-RU").lower()#if u speak another language u can change it here
        print(f"Вы сказали: {command}")
        return command
    except sr.UnknownValueError:
        print("Извините, не удалось распознать аудио.")
        return None
    except sr.RequestError as e:
        print(f"Не удалось получить результаты от службы распознавания речи Google; {e}")
        return None

def main():
    while True:
        command = listen()
        if command is not None:
            if "саша" in command: #there is code words to start speak with assistant
                if ccleaner_opener and any(keyword in command for keyword in ccleaner_opener.keys()):
                    open_ccleaner()
                    print("Открываю")
                    tts.say("Открываю")
                elif ccleaner_closer and any(keyword in command for keyword in ccleaner_closer.keys()):
                    tts.say("Закрываю")
                    close_ccleaner()
                elif chrome_opener and any(keyword in command for keyword in chrome_opener.keys()):
                        tts.say("Открываю")
                        open_chrome()
                elif chrome_closer and any(keyword in command for keyword in chrome_closer.keys()):
                        tts.say("Закрываю")
                        close_chrome()
                elif computer_shutdown and any(keyword in command for keyword in computer_shutdown.keys()):
                        tts.say("Выключаю")
                        shutdown_computer()
                elif steam_closer and any(keyword in command for keyword in steam_closer.keys()):
                        tts.say("Закрываю")
                        close_steam()
                elif steam_opener and any(keyword in command for keyword in steam_opener.keys()):
                        tts.say("Открываю")
                        open_steam()
                elif search_google and any(keyword in command for keyword in search_google.keys()):
                        tts.say("Ищу")
                        webbrowser.open_new_tab('https://www.google.com/search?q={}'.format(command))
                elif search_youtube and any(keyword in command for keyword in search_youtube.keys()):
                        tts.say("Ищу")
                        webbrowser.open_new_tab('https://www.youtube.com/results?search_query={}'.format(command))
                elif chat_gpt and any(keyword in command for keyword in chat_gpt.keys()):
                        tts.say("Ищу ответ")
                        response = g4f.ChatCompletion.create(
                        model=g4f.models.gpt_4,
                        messages=[{"role": "user", "content": command}]) 
                        print(response)
                        tts.say(response) 
                elif hello and any(keyword in command for keyword in hello.keys()):
                    tts.say("Здравствуйте хозяин, чем я могу вам помочь?")
                    print("Здравствуйте хозяин, чем я могу вам помочь?")
                elif goodbye and any(keyword in command for keyword in goodbye.keys()):
                    tts.say("Рада была служить")
                    print("Рада была служить")
                    break
                elif command:
                    pass
        else:
            print("Комманда не была распознана")

if __name__ == "__main__":
    main()