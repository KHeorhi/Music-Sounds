from tkinter import *

class Speder:

    def __init__(self,root, width, height, num_column, num_row,
                 x1, y1, x12, y12, x2, y2, x22, y22, outline_one, outline_two,
                 x3, y3, x31, y31, fill_color, form_speder='oval') -> object :
        self.root = root
        self.width = width
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.grid(column=num_column, row=num_row)
        self.road_behind = self.canvas.create_rectangle(x1, y1, x12, y12, outline=outline_one)
        self.road_after = self.canvas.create_rectangle(x2, y2, x22, y22, outline=outline_two)
        if form_speder == 'oval':
            self.speder = self.canvas.create_oval(x3, y3, x31, y31, fill=fill_color)
        elif form_speder == 'rectangle':
            self.speder = self.canvas.create_rectangle(x3, y3, x31, y31, width=1, fill=fill_color, outline='black')
        #self.canvas.bind('<Button-1>', self.speder)

    def move(self, event):
        self.canvas.bind(event, self.speeder_move)



    def speeder_move(self, event):
        coord_list = self.canvas.coords(self.speder)
        if (coord_list[0] + coord_list[0]) / 2 <=self.width:
            self.canvas.coords(self.speder, event.x-3.5, 6.5, event.x+3.5, 13.5)
            print(self.canvas.coords(self.speder))