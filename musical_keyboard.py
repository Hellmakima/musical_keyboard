import pygame as p
from pynput import keyboard
import random
import os
import time

print('press `Esc` to kill this program. or try Ctrl+c very fast')

# Initialize pygame mixer
p.init()
p.mixer.init()

# Path to the new keys
keys_path = 'keys2/'

# Load all sound files dynamically from keys2/
sound_files = [f for f in os.listdir(keys_path) if f.endswith('.mp3')]
sounds = [p.mixer.Sound(os.path.join(keys_path, sound)) for sound in sorted(sound_files)]

# Configuration
max_concurrent_sounds = 8  # Maximum number of sounds playing at once
sound_duration = 1000  # Duration for each sound in milliseconds

# Playing sounds queue
playing_sounds = []

def on_key_press(key):
    global playing_sounds

    # Choose a random sound
    chosen = random.randint(0, len(sounds) - 1)

    # Stop the oldest sound if the limit is reached
    if len(playing_sounds) >= max_concurrent_sounds:
        oldest_sound = playing_sounds.pop(0)
        oldest_sound['sound'].stop()

    # Play the chosen sound and add it to the playing queue
    sound = sounds[chosen]
    sound.play(maxtime=sound_duration)  # Play for a maximum of sound_duration
    playing_sounds.append({'sound': sound, 'start_time': time.time()})

    # Stop the listener when the Escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Start the keyboard listener
with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()