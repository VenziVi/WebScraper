import Tkinter as tk
from text import Text


class Entry(Text):
    def __init__(self):
        Text.__init__(self)
        self.titleEntry = tk.Entry(self.root, width=20, bg="#D3D3D3")
        self.titleEntryWindow = self.canvas1.create_window(420, 40, window=self.titleEntry)
        self.quantityEntry = tk.Entry(self.root, width=2, bg="#D3D3D3")
        self.quantityEntryWindow = self.canvas1.create_window(505, 70, window=self.quantityEntry)
        self.numOfBooksEntry = tk.Entry(self.root, width=3, bg="#D3D3D3")
        self.numOfBooksEntryWindow = self.canvas1.create_window(215, 40, window=self.numOfBooksEntry)
        self.minPriceEntry = tk.Entry(self.root, width=3, bg="#D3D3D3")
        self.minPriceEntryWindow = self.canvas1.create_window(410, 150, window=self.minPriceEntry)
        self.maxPriceEntry = tk.Entry(self.root, width=3, bg="#D3D3D3")
        self.maxPriceEntryWindow = self.canvas1.create_window(470, 150, window=self.maxPriceEntry)
        self.fileDirEntry = tk.Entry(self.root, width=50, bg="#D3D3D3")
        self.fileDirEntryWindow = self.canvas1.create_window(224, 380, window=self.fileDirEntry)

    def get_title(self):
        return self.titleEntry.get()

    def get_quantity(self):
        quantity = self.quantityEntry.get()
        try:
            quantity = int(quantity)
        except ValueError:
            if quantity == '':
                quantity = None
            else:
                print("Invalid input for minimum quantity. Value set to 1.")
                quantity = None
        return quantity

    def get_number_of_books(self):
        num_of_books = self.numOfBooksEntry.get()
        try:
            num_of_books = int(num_of_books)
        except ValueError:
            if num_of_books == '':
                num_of_books = 1000
            else:
                print("Invalid input for number of books. Value set to 1000.")
                num_of_books = 1000
        return num_of_books

    def get_min_price(self):
        min_price = self.minPriceEntry.get()
        try:
            min_price = int(min_price)
        except ValueError:
            if min_price == '':
                min_price = None
            else:
                print("Invalid input for minimum price. Value set to None.")
                min_price = None
        return min_price

    def get_max_price(self):
        max_price = self.maxPriceEntry.get()
        try:
            max_price = int(max_price)
        except ValueError:
            if max_price == '':
                max_price = None
            else:
                print("Invalid input for maximum price. Value set to None.")
                max_price = None
        return max_price
