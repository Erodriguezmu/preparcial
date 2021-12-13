
"""
    Reproducir un archivo de audio
    con Python 3 
"""
from pygame import mixer # Load the required library

mixer.init()
mixer.music.load(r'C:\Users\paula\Music\Adele-Hello.mp3')
mixer.music.play()
