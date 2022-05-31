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
        
        #create menubar
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

        #create Frame
        self.frame_top = Frame()
        self.frame_top.pack()
        self.frame_bottom = Frame()
        self.frame_bottom.pack()
        
        #download picture
        self.image = Image.open('image/label_music_image_256.png')
        self.image_bk = ImageTk.PhotoImage(self.image)
        
        #add picture to top Frame
        self.label_middel = Label(self.frame_top, image=self.image_bk)
        self.label_middel.grid(columnspan=5, row=2)

        #add buttons to bottom Frame

        self.volume_button =  Button(self.frame_bottom, text='Volumes')
        self.play_button = Button(self.frame_bottom, text='Play')
        self.stop_button = Button(self.frame_bottom, text='Stop')

        self.volume_button.grid(column=1, row=2)
        self.play_button.grid(column=2, row=2)
        self.stop_button.grid(column=3, row=2)

        #create music_road and add to bottom Frame
        
        self.music_canvas = Canvas(self.frame_bottom, width=290, height=11, bg='aquamarine')
        self.music_canvas.grid(columnspan=5, row=1)
        self.track_road = self.music_canvas.create_rectangle(2, 5, 150, 5, outline='green')
        self.track_road = self.music_canvas.create_rectangle(150, 5, 290, 5, outline='red')
        self.music_speeder = self.music_canvas.create_rectangle(4, 4, 10, 11, width=1, fill='orangered', outline='black')
    
    def create_button(self):
        pass