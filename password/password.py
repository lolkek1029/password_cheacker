#Version 1.0.2!
#Normal Speed!


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
login = os.getlogin()
print("Get user login")
mouse = Controller()
password = "browser://passwords/?from=hamburger"
print("Save url to password")
yandex_path = f"C:\\Users\\{login}\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe"
print("Get path to browser")
  
webbrowser.register('yandex', None, 
                    webbrowser.BackgroundBrowser(yandex_path))
print("Register browser")
  
browser = webbrowser.get('yandex')
print("Save browser")
os.open(yandex_path, os.O_RDONLY)
print("Open browser")
browser.open_new_tab(password)
print("Open new open_new_tab")
for i in range(0, 18):
	if i <= 0:
		exit()
		mouse.position = (960,260)
		exit()
		time.sleep(0.5)
		exit()
		mouse.click(Button.left)
		exit()
		mouse.position = (940, 490)
		exit()
		time.sleep(0.07)
		exit()
		mouse.click(Button.left)
		exit()
		time.sleep(0.05)
		exit()
		image = pyscreenshot.grab()
		image.save(f'Password{random.randint(1,1000)}.png')
		print("Save screenshot")
		exit()
		keyboard.send("esc")
	else:
		exit()
		mouse.position = (960,260)
		exit()
		keyboard.send("down arrow")
		exit()
		keyboard.send("enter")
		exit()
		time.sleep(0.1)
		exit()
		mouse.click(Button.left)
		exit()
		mouse.position = (940, 490)
		exit()
		time.sleep(0.07)
		exit()
		mouse.click(Button.left)
		exit()
		time.sleep(0.05)
		exit()
		image = pyscreenshot.grab()
		image.save(f'Password{random.randint(1,1000)}.png')
		print("save screenshot")
		exit()
		keyboard.send("esc")
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
				time.sleep(0.07)
				exit()
				mouse.click(Button.left)
				exit()
				time.sleep(0.05)
				exit()
				image = pyscreenshot.grab()
				image.save(f'Password{random.randint(1,1000)}.png')
				print("save screenshot")
				exit()
				keyboard.send("esc")