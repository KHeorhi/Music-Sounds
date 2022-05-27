from tkinter import * 
from PIL import Image, ImageTk

class App(Tk):

    def __init__(self, name_title, path_iconbitmap, size_geometry, *args, **kwargs):
        super().__init__()
        self.title(name_title)
        self.iconbitmap(path_iconbitmap)
        self.geometry(size_geometry)
        self.create_gui()

    def create_gui(self):
        
        self.label_top = Label(text='Label top', justify='center')
        self.label_top.grid(columnspan=5, row=1)

        self.image = Image.open('D:/программирование/Tkinter/music_app/image/label_music_image_256.png')
        self.image_bk = ImageTk.PhotoImage(self.image)
        self.label_middel = Label(image=self.image_bk)
        self.label_middel.grid(columnspan=5, row=2)

        self.label_bottom = Label(text='Bottom label')
        self.label_bottom.grid(columnspan=5, row=3)
        
