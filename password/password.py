#Version one!
#Not fast!


import os
import webbrowser
import pyscreenshot
import time
import random
import keyboard
from pynput.mouse import Button, Controller
i = -1
mouse = Controller()
keyboardf = Controller()
password = "browser://passwords/?from=hamburger"
yandex_path = r"C:\Users\Администратор\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
  
webbrowser.register('yandex', None, 
                    webbrowser.BackgroundBrowser(yandex_path))
  
browser = webbrowser.get('yandex')
os.open(yandex_path, os.O_RDONLY)
browser.open_new_tab(password)
for i in range(0, 18):
	if i <= 0:
		mouse.position = (960,260)
		time.sleep(2.5)
		mouse.click(Button.left)
		mouse.position = (940, 490)
		time.sleep(0.5)
		mouse.click(Button.left)
		time.sleep(0.5)
		image = pyscreenshot.grab()
		image.save(f'Password{random.randint(1,1000)}.png')
		mouse.position = (940, 737)
		time.sleep(0.5)
		mouse.click(Button.left)
		print(i)
	else:
		mouse.position = (960,260)
		mouse.move(0, (33 * i))
		time.sleep(0.3)
		mouse.click(Button.left)
		mouse.position = (940, 490)
		time.sleep(1)
		mouse.click(Button.left)
		time.sleep(0.5)
		image = pyscreenshot.grab()
		image.save(f'Password{random.randint(1,1000)}.png')
		time.sleep(0.1)
		mouse.position = (940, 737)
		mouse.click(Button.left)
		if i == 17:
			while True:
				time.sleep(0.5)
				mouse.position = (960,260)
				keyboard.send("down arrow")
				keyboard.send("enter")
				mouse.position = (940, 490)
				time.sleep(1)
				mouse.click(Button.left)
				time.sleep(0.5)
				image = pyscreenshot.grab()
				image.save(f'Password{random.randint(1,1000)}.png')
				time.sleep(0.1)
				mouse.position = (940, 737)
				mouse.click(Button.left)

		print(i)
