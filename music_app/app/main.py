from tkinter import *
from app import App

def main():
    music_player = App(name_title='Music Sounds' 
                    ,path_iconbitmap = 'image/mp3_ico.ico'
                    ,size_geometry='300x330')

    music_player.mainloop()

if __name__ == '__main__':
    main()