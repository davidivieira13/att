import time
from turtle import onrelease
import pyautogui as py
import pygetwindow
from movimentos import Bot
import sys
import os
from interval import Interval
from pynput import keyboard
import threading
import pywinauto
import time
import win32gui
import webbrowser

py.FAILSAFE = False
sys.setrecursionlimit(10**9)
var_reload = 0
Start_Bot = Bot()
#Start_Bot.ArrumaBoteCmd()


def fMain(): 

    sites = ['youtube kids','coquinhos', 'monkey', 'moto x3m', 'subway surfers', 'drive mad', 'crazy cars', 'go kart', 'dreadhead parkour', 'moto', 'carro', 'car', 'cars']
    navegadores = ['chrome.exe','brave.exe','mozzila.exe']
    while True:
        time.sleep(5)
        var_bloqueio = False
        janela_atual = win32gui.GetForegroundWindow()
        texto_janela_atual = win32gui.GetWindowText(janela_atual) 
        time.sleep(1)
        print(texto_janela_atual)
        
        for site in sites:
            print('-' *50)
            if site in texto_janela_atual.lower():
                print(f" {site} liberado aberto na janela atual.")   
                var_bloqueio = True
                break
            else:
                print(f" site bloqueado aberto na janela atual.")    
                
        
        print(f'var_bloqueio - {var_bloqueio}')
        if var_bloqueio == False:
            print('fechando todas paginas e abrindo as liberadas')
            time.sleep(1)
            for navegador in navegadores:
                os.system(f"taskkill /f /im {navegador}")
                time.sleep(1)
            webbrowser.open('https://www.coquinhos.com/category/jogos-para-criancas-4-anos/')
            time.sleep(1)
            webbrowser.open('https://www.youtubekids.com/search?q=numberblocks&hl=pt')            

        time.sleep(5)
       









def fVerificaKeyPress(): 
   while True:
       with keyboard.Events() as events:
           for event in events: 
               if event.key == keyboard.Key.esc:
                   os._exit(0)

threading.Thread(target=fVerificaKeyPress).start()
fMain()
