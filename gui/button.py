import Tkinter as tk
from os import environ
from PIL import ImageTk, Image
import tkFileDialog as filedialog
from radiobutton import RadioButton
from popup_window import PopUpWindowSuccess, PopUpWindowFailure

from data_extraction.collect_data import CollectData

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


class Button(RadioButton):
    def __init__(self, request_handler, url_collector, data_holder):
        RadioButton.__init__(self)
        self.clearAllButton = tk.Button(self.root, text="Clear all", command=self.clear)
        self.clearAllButtonWindow = self.canvas1.create_window(70, 460, window=self.clearAllButton)
        self.goButton = tk.Button(self.root, text="GO!", command=self.get_data, height=2, width=9, bg="#52595D",
                                  fg="white")
        self.goButtonWindow = self.canvas1.create_window(440, 460, window=self.goButton)
        self.musicButton = tk.Button(self.root, text="Play music", command=self.play_music())
        self.muteButtonImage = ImageTk.PhotoImage(Image.open("gui/media/mute.png"))
        self.volumeButtonImage = ImageTk.PhotoImage(Image.open("gui/media/volume.png"))
        self.volumeButton = tk.Button(self.root, image=self.volumeButtonImage, command=self.mute_music)
        self.volumeButtonWindow = self.canvas1.create_window(780, 480, window=self.volumeButton)
        self.muted = False
        self.folder_path = tk.StringVar()
        self.browseButton = tk.Button(text="Get titles from a file", command=self.browse_button)
        self.browseButtonWindow = self.canvas1.create_window(100, 350, window=self.browseButton)

        self.request_handler = request_handler
        self.url_collector = url_collector
        self.data_holder = data_holder

        self.root.mainloop()

    @staticmethod
    def play_music():
        pygame.mixer.music.load("gui/media/Gnossienne.mp3")
        pygame.mixer.music.play(loops=20)

    def mute_music(self):
        if self.muted:
            pygame.mixer.music.set_volume(0.7)
            self.volumeButton.configure(image=self.volumeButtonImage)
            self.muted = False
        else:
            pygame.mixer.music.set_volume(0)
            self.volumeButton.configure(image=self.muteButtonImage)
            self.muted = True

    def browse_button(self):
        filename = filedialog.askopenfilename(initialdir="scraper", title="Select a file",
                                              filetypes=[("json", "*.json")])
        self.clear()
        self.fileDirEntry.insert(0, filename)

    def clear(self):
        self.titleEntry.delete(0, 'end')
        self.quantityEntry.delete(0, 'end')
        self.numOfBooksEntry.delete(0, 'end')
        self.maxPriceEntry.delete(0, 'end')
        self.minPriceEntry.delete(0, 'end')
        self.categoriesMenu.set(self.category_list[0])
        self.ratingMenu.set(self.ratingList[0])
        self.ratingAscButton.deselect()
        self.ratingDescButton.deselect()
        self.priceAscButton.deselect()
        self.priceDescButton.deselect()
        self.fileDirEntry.delete(0, 'end')

    def get_data(self):
        books_count = self.get_number_of_books()
        genres = self.set_genres()
        title = self.set_title()
        sorting = self.set_sorting()
        filters = self.set_filters()
        titles_path = self.set_titles_path()
        keywords = None
        collector = CollectData(books_count, genres, filters, keywords, title, titles_path,
                                self.request_handler, self.url_collector, self.data_holder)
        collector.collect_books_data()
        collector.collection.sort_collection(sorting)
        self.display_popup(collector.collection.export_data_to_file(True))

    def display_popup(self, value):
        if value:
            PopUpWindowSuccess()
        else:
            PopUpWindowFailure()

    def set_filters(self):
        filters = []
        rating = self.get_rating()
        quantity = self.get_quantity()
        min_price = self.get_min_price()
        max_price = self.get_max_price()
        if rating:
            filters.append("rating={0}".format(rating))
        if quantity:
            filters.append("available>{0}".format(quantity))
        if min_price:
            filters.append("price>{0}".format(min_price))
        if max_price:
            filters.append("price<{0}".format(max_price))
        return filters

    def set_sorting(self):
        sorting = []
        price_sort = self.get_sort_price()
        rating_sort = self.get_sort_rating()
        if price_sort:
            sorting.append("price-{0}".format(price_sort))
        if rating_sort:
            sorting.append("rating-{0}".format(rating_sort))
        return sorting

    def set_title(self):
        title = self.get_title()
        if title:
            title = str(title).split(" ")
        return title

    def set_titles_path(self):
        titles_path = self.get_titles_path()
        if titles_path:
            return titles_path

    def set_genres(self):
        genres = self.get_category()
        if genres:
            genres = [self.get_category()]
        return genres
