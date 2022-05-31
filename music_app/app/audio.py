import pygame

class Audio():

    def __init__(self) -> object:
        pygame.mixer.pre_init(frequency=44100, 
                              size=-16,
                              channels=2,
                              buffer=4096)
        pygame.mixer.init()

    def play_sound(self):
        self.dowloand_song = pygame.mixer.Sound(filename='D:\программирование\Tkinter\music_app\audio\the_xx_intro.mp3')
        pygame.mixer.Sound.play(self.dowloand_song)