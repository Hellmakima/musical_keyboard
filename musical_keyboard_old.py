import pygame as pp
from pynput import keyboard
import random

pp.init()
pp.mixer.init()
sounds = [pp.mixer.Sound(f'keys24\\key{i:02}.mp3') for i in range(1,25)]
chosen = random.randint(0,23)

def on_key_press(key):
	global chosen
	chosen += random.randint(-2, 2)
	chosen %= 24
	sounds[chosen].play()
	if key == keyboard.Key.esc:
		return False

with keyboard.Listener(on_press=on_key_press) as listener:
	listener.join()