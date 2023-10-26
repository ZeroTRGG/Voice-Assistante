import os
import speech_recognition as sr
import config
import subprocess

ccleaner = r"C:\Program Files\CCleaner\CCleaner64.exe"
steam = r"D:\steam\steam.exe"
chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def open_ccleaner():
    try:
        os.startfile(ccleaner)
        print(f"Открыт файл: {steam}")
    except Exception as e:
        print(f"Ошибка при открытии файла: {e}")

def close_ccleaner():
    try:
        subprocess.call("TASKKILL /F /IM CCleaner64.exe", shell=True)
        print(f"Приложение клинер закрыто")
    except Exception as e:
        print(f"Ошибка при закрытии файла: {e}")

def open_steam():
    try:
        os.startfile(steam)
        print(f"Открыт файл: {minecraft}")
    except Exception as e:
        print(f"Ошибка при открытии файла: {e}")

def close_chrome():
    try:
        subprocess.call("TASKKILL /F /IM chrome.exe", shell=True)
        print(f"Приложение хром закрыто")
    except Exception as e:
        print(f"Ошибка при закрытии файла: {e}")

def open_chrome():
    try:
        os.startfile(chrome)
        print(f"Открыт файл: {chrome}")
    except Exception as e:
        print(f"Ошибка при открытии файла: {e}")

def shutdown_computer():
    try:
        os.system("shutdown /s /t 1")  
        print("Выключение пк.")
    except Exception as e:
        print(f"Ошибка выключения пк: {e}")

def close_steam():
    try:
        subprocess.call("TASKKILL /F /IM steam.exe", shell=True)
        print(f"Приложение Стим закрыто")
    except Exception as e:
        print(f"Ошибка при закрытии файла: {e}")
