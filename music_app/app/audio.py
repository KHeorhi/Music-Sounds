from email.mime import audio
import pygame

class Audio():

    def __init__(self) -> object:
        pygame.mixer.pre_init(frequency=44100, 
                              size=-16,
                              channels=2,
                              buffer=512)
        pygame.mixer.init()

    def play_sound(self):
        self.dowloand_song = pygame.mixer.Sound(file='D:/программирование/Tkinter/music_app/audio/the_xx_intro.mp3')
        pygame.mixer.Sound.set_volume(self.dowloand_song, max(0.0, 1.0))
        pygame.mixer.Sound.play(self.dowloand_song)
        


sounds = Audio()