#Version 1.0.1!
#Not fast!


import os
import webbrowser
import pyscreenshot
import time
import random
import keyboard
from pynput.mouse import Button, Controller
def exit():
	if keyboard.is_pressed('q'):
		quit()
i = -1
mouse = Controller()
password = "browser://passwords/?from=hamburger"
yandex_path = r"C:\Users\Администратор\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
  
webbrowser.register('yandex', None, 
                    webbrowser.BackgroundBrowser(yandex_path))
  
browser = webbrowser.get('yandex')
os.open(yandex_path, os.O_RDONLY)
browser.open_new_tab(password)
for i in range(0, 18):
	if i <= 0:
		exit()
		mouse.position = (960,260)
		exit()
		time.sleep(1.5)
		exit()
		mouse.click(Button.left)
		exit()
		mouse.position = (940, 490)
		exit()
		time.sleep(0.1)
		exit()
		mouse.click(Button.left)
		exit()
		time.sleep(0.1)
		exit()
		image = pyscreenshot.grab()
		image.save(f'Password{random.randint(1,1000)}.png')
		exit()
		mouse.position = (940, 737)
		exit()
		time.sleep(0.3)
		exit()
		mouse.click(Button.left)
		exit()
	else:
		exit()
		mouse.position = (960,260)
		exit()
		keyboard.send("down arrow")
		exit()
		keyboard.send("enter")
		exit()
		time.sleep(0.2)
		exit()
		mouse.click(Button.left)
		exit()
		mouse.position = (940, 490)
		exit()
		time.sleep(0.2)
		exit()
		mouse.click(Button.left)
		exit()
		time.sleep(0.2)
		exit()
		image = pyscreenshot.grab()
		image.save(f'Password{random.randint(1,1000)}.png')
		exit()
		time.sleep(0.1)
		exit()
		mouse.position = (940, 737)
		exit()
		mouse.click(Button.left)
		if i == 17:
			while True:
				exit()
				time.sleep(0.2)
				exit()
				mouse.position = (960,260)
				exit()
				keyboard.send("down arrow")
				keyboard.send("enter")
				exit()
				mouse.position = (940, 490)
				exit()
				time.sleep(0.2)
				exit()
				mouse.click(Button.left)
				exit()
				time.sleep(0.1)
				exit()
				image = pyscreenshot.grab()
				image.save(f'Password{random.randint(1,1000)}.png')
				time.sleep(0.1)
				exit()
				mouse.position = (940, 737)
				exit()
				mouse.click(Button.left)
				exit()
