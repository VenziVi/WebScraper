import Tkinter as tk
from dropdown import DropdownMenu


class RadioButton(DropdownMenu):
    def __init__(self):
        DropdownMenu.__init__(self)
        self.sortPrice = tk.StringVar()
        self.priceAscButton = tk.Radiobutton(self.root, text="ascending", variable=self.sortPrice, value="ascending",
                                             bg="#e5e8e9")
        self.priceAscButtonWindow = self.canvas1.create_window(440, 210, window=self.priceAscButton)
        self.priceDescButton = tk.Radiobutton(self.root, text="descending", variable=self.sortPrice, value="descending",
                                              bg="#e5e8e9")
        self.priceDescButtonWindow = self.canvas1.create_window(444, 230, window=self.priceDescButton)
        self.sortRating = tk.StringVar()
        self.ratingAscButton = tk.Radiobutton(self.root, text="ascending", variable=self.sortRating, value="ascending",
                                              bg="#d7dddb")
        self.ratingAscButtonWindow = self.canvas1.create_window(140, 250, window=self.ratingAscButton)
        self.ratingDescButton = tk.Radiobutton(self.root, text="descending", variable=self.sortRating,
                                               value="descending", bg="#d7dddb")
        self.ratingDescButtonWindow = self.canvas1.create_window(144, 270, window=self.ratingDescButton)

    def get_sort_price(self):
        return self.sortPrice.get()

    def get_sort_rating(self):
        return self.sortRating.get()

    def get_titles_path(self):
        return self.fileDirEntry.get()
