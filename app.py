from tkinter import *
#from Player import MUSIC, Plays
from play_config import Audio
from PIL import ImageTk, Image

MUSIC = Audio(file_name='music/the_xx_intro.mp3')

class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.title('Music Player')
        self.geometry('300x300')
        self.iconbitmap('images/mp3_ico.ico')
        #self.create_button()
        self.create_main_label()

    def create_main_label(self):

        self.label_middle = Label(self)
        self.label_middle['image'] = self.load_image('D:\программирование\Tkinter\images\label_music_image_256.png')
        self.label_middle.grid(columnspan=5, row=0)
        self.label_middle['justify'] = 'center'

        self.label_bottom = Label(self)
        self.label_bottom['command'] = self.create_bottom_button()
        self.label_bottom.grid(row=1)
    
    def create_bottom_button(self):
        self.play_button = Button(self)
        self.play_button['text'] = 'Play'
        self.play_button['command'] = MUSIC.play_audio()
        self.play_button.grid(column=1, row=1)

        self.stop_button = Button(self)
        self.stop_button['text'] = 'Stop'
        self.stop_button['command'] = MUSIC.stop_audio
        self.stop_button.grid(column=2, row=1)

        self.volumn_button_up = Button(self)
        self.volumn_button_up['text'] = '+'
        self.volumn_button_up['command'] = MUSIC.volume_up
        if MUSIC.volume <= 0.95:
            self.volumn_button_up['state'] = 'active'
        if 0.95 < MUSIC.volume <= 1:
            self.volumn_button_up['state'] = 'disabled'
        self.volumn_button_up.grid(column=3, row=1)

        self.volumn_value = Label(self)
        self.volumn_value['text'] = 'Volume'
        self.volumn_value.grid(column=4, row=1)

        self.volumn_button_down = Button(self)
        self.volumn_button_down['text'] = '-'
        self.volumn_button_down['command'] = MUSIC.volume_down
        self.volumn_button_down.grid(column=5, row=1)

    def load_image(self, file_path:str):
        self.image = ImageTk.PhotoImage(Image.open(file_path))
        return self.image
