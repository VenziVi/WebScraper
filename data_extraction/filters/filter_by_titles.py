import json
import os
from data_extraction.filters.filter import BaseFilter


class TitlesFilter(BaseFilter):
    def __init__(self, request_handler, file_path):
        super(TitlesFilter, self).__init__(request_handler)
        self.__titles_list = self.__read_titles_from_file(file_path)
        self.__book_url_list = []


    @property
    def titles_list(self):
        """Returns titles list"""
        return self.__titles_list

    @staticmethod
    def is_file_empty(file_path):
        """Check if fail exists and is not empty"""
        return False if os.path.isfile(file_path) else True

    def __read_titles_from_file(self, file_path):
        """
        Read the file from a given file path.
        If file is empty or does not exist return None.
        Save all books titles in the titles list
        :param file_path:
        :return list:
        """
        titles = []
        if self.is_file_empty(file_path):
            print("File is empty!")
            return titles
        try:
            with open(os.path.join(file_path), "r") as input_data:
                data = json.load(input_data)
                if "titles" in data:
                    titles.extend(data["titles"])
        except ValueError as err:
            print(err)
        return titles

    def __match_books_with_titles(self, titles_dict):
        """
        Search for all given titles in titles_dict.
        If the title exists, add the title url to the titles_url_list.
        :param titles_dict:
        :return:
        """
        for title in self.titles_list:
            if title.lower() in titles_dict:
                self.__book_url_list.append(titles_dict[title.lower()])
            else:
                print("Book: '{0}' doesn't exist!".format(title))

    def filter_books(self, books_dict):
        """
        Returns a list of book URLs that match the titles in titles_list
        :param titles_dict:
        :return list:
        """
        self.__match_books_with_titles(books_dict)
        return self.request_handler.get_pages_text_async(self.__book_url_list)