# Musical Keyboard Simulator

## Overview
This is a Python-based musical keyboard simulator that plays random sounds mapped to keypresses. The project dynamically manages sound playback, ensuring a smooth experience even during rapid typing.

## Features
- **Dynamic Sound Loading**: Loads MP3 files dynamically from a specified directory (`keys2/`).
- **Randomized Notes**: Each keypress triggers a random sound from the available keys.
- **Concurrency Control**: Limits the maximum number of sounds playing at once to prevent system overload.
- **Duration Management**: Each sound plays for a configurable duration (default: 1 second).
- **Stop Mechanism**: Pressing the `ESC` key exits the program.

## Requirements
- Python 3.6+
- Required libraries:
  - `pygame`
  - `pynput`

Install dependencies using:
```bash
pip install pygame pynput
```

## Usage
1. Place your sound files (`.mp3`) in the `keys2/` directory.
2. Run the program:
   ```bash
   python musical_keyboard.py
   ```
3. Press keys to play random sounds.
4. Press `ESC` to exit.

### Important Note
The MP3 files were scraped from [Online Pianist](https://assets.onlinepianist.com), and a lot of this project was developed using ChatGPT. Adjust (delete/add) files based on your preferences. The current selection is rough and may not suit everyone’s taste.

CMD used for scraping:
```bash
curl --compressed -o 65.mp3 https://assets.onlinepianist.com/player/sounds/65.mp3
```

## File Structure
```
./
├── keys2/                  # Directory containing sound files
│   ├── 24.mp3
│   ├── 29.mp3
│   ├── ...
├── musical_keyboard.py    # Main program file
├── README.md              # Project documentation
```

## Configuration
### `max_concurrent_sounds`
Defines the maximum number of sounds that can play simultaneously. Default is `8`.

### `sound_duration`
Specifies the duration (in milliseconds) for each sound to play. Default is `1000` (1 second).

To modify these values, edit the `musical_keyboard.py` file:
```python
max_concurrent_sounds = 8
sound_duration = 1000
```

## Contributing
Feel free to fork this repository and submit pull requests. Contributions are welcome!

## License
No official license. Use at your own risk.

# Huge shoutout to chatgpt-kun and please do share with me if you make a cuter verision of this.
