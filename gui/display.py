from PIL import ImageTk, Image
import Tkinter as tk
from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


class Display:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Welcome to S03-Py-team-2 book scraping project!")
        self.root.minsize(800, 500)
        self.root.maxsize(800, 500)

        self.canvas1 = tk.Canvas(self.root, width=880, height=500)
        self.bg = ImageTk.PhotoImage(Image.open('gui/media/background.png'))
        self.canvas1.create_image(0, 0, image=self.bg, anchor="nw")
        self.canvas1.pack(fill="both", expand=True)

        pygame.mixer.init()

