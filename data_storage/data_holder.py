import json
import os
from book import Book
from collections import OrderedDict


DEFAULT_SORT = ["title-ascending"]


class DataHolder:
    def __init__(self):
        """
        Class constructor. Takes no arguments, but it creates an instances of
        class Book and SortingMixin, which are used to store book data and sort
        the list data struct, containing class instances for every book scraped.
        """
        self.__data_struct = []

    def add_entity(self, upc, title, genre, pr_type, price_it,
                   price_et, tax, qty, rating, description):

        self.__data_struct.append(Book(upc, title, genre, pr_type, price_it,
                                       price_et, tax, qty, rating, description))

    def sort_collection(self, sorting):
        sorting_list = DEFAULT_SORT
        if sorting:
            sorting_list = sorting
        self.__sort_collection(sorting_list)

    def export_data_to_file(self, gui=None):
        if not self.__data_struct:
            self.__write_data_to_file("Book collection is empty!")
            print("Collection is empty!")
            if gui:
                return False
        else:
            collection = self.__fill_book_collection()
            self.__write_data_to_file(collection)
            print("JSON created successfully!")
            if gui:
                return True

    def __fill_book_collection(self):
        collection = OrderedDict()
        for book in self.__data_struct:
            collection.update({book.upc: {"Title": book.title,
                                          "Genre": book.genre,
                                          "Rating": book.rating,
                                          "Price": book.price,
                                          "Available": book.available,
                                          "Type": book.product_type,
                                          "Price_excl_tax": book.price_excl_tax,
                                          "Tax": book.tax,
                                          "Description": book.description}})
        return collection

    @staticmethod
    def __write_data_to_file(books_data):
        cwd = os.getcwd()
        path = os.path.join(cwd, "output")

        try:
            os.mkdir(path)
        except OSError:
            path = "output/"

        with open(os.path.join(path, "book_collection"), "w") as writer:
            writer.write(json.dumps(books_data, indent=2))

    def __sort_collection(self, sorting_list):
        is_descending = False
        for sort in sorting_list:
            if "-" not in sort:
                continue
            argument, sort_type = sort.split("-")
            if sort_type == "descending":
                is_descending = True
            self.__data_struct.sort(key=lambda x: x[argument.capitalize()], reverse=is_descending)
