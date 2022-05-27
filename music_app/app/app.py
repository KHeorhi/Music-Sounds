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
        
        menubar = Menu(self)
        self.config(menu=menubar)
        list_menubar = ['File', 'View']
        list_file_Menu = ['New playlist', 'Open playlist', 'Save', 'Save As' ,'Exit']
        for item_list_menubar in list_menubar: 
            if item_list_menubar == 'File':
                fileMenu = Menu(menubar)
                for item_list_file_Menu in list_file_Menu:
                    fileMenu.add_command(label=item_list_file_Menu)   
                menubar.add_cascade(label=item_list_menubar, menu=fileMenu)
            else:
                menubar.add_cascade(label=item_list_menubar)

        self.image = Image.open('image/label_music_image_256.png')
        self.image_bk = ImageTk.PhotoImage(self.image)
        self.label_middel = Label(image=self.image_bk)
        self.label_middel.grid(columnspan=5, row=2)

        self.label_bottom = Label(text='Bottom label')
        self.label_bottom.grid(columnspan=5, row=3)
    
