import re
import constants
from collections import OrderedDict


class PageDataExtractor(object):
    """
    The PageDataExtractor class is initialized with HTML text
    and provides functions that returns extracted data from a given page text.
    Attributes:
        html_text:
            Contains html-text that has been processed with BeautifulSoup
    """
    def __init__(self, text):
        self.html_text = text

    @property
    def html_text(self):
        return self.__html_text

    @html_text.setter
    def html_text(self, value):
        if not value:
            raise ValueError("Page is empty!")
        self.__html_text = value

    def get_books_per_page(self):
        """
        Returns the number of books on the page
        :return int:
        """
        lines = self.html_text.find_all("form", class_="form-horizontal")
        try:
            paging = lines.pop().find_all("strong")
        except IndexError:
            print("Books count not found!")
            return constants.DEFAULT_VALUE

        if len(paging) == 1:
            return int(paging.pop().text)

        to_book = int(paging.pop().text)
        from_book = int(paging.pop().text)
        return to_book - from_book + constants.BOOKS_CALC_CONST

    def get_next_page(self):
        """
        Returns the next page extension from the current page
        :return str:
        """
        next_form = self.html_text.find("li", class_="next")
        if not next_form:
            return None
        return next_form.a["href"]

    @staticmethod
    def __collect_genres(categories):
        genres = {}
        start = constants.GENRES_START_INDEX
        end = constants.GENRES_END_INDEX
        for category in categories[start:end]:
            url_extension = str(category).split('"')[constants.GENRES_INDEX]
            name = re.findall(r"(?:[A-Za-z]+\s)?[A-Za-z]+", category.text)
            genres[str.join(" ", name).lower()] = str(url_extension).replace(
                "index.html", ""
            )
        return genres

    def get_books_categories(self):
        """
        Returns a dictionary with all existing genres
        key: genre name, value: genre url
        :return dict:
        """
        categories = self.html_text.find_all("li")
        if not categories:
            return {}
        return self.__collect_genres(categories)

    def get_titles_from_collection_page(self, count):
        """
        Returns a dictionary with all book titles on the page
        key: book title, value: book url
        :return dict:
        """
        titles_list = self.html_text.find_all("img")
        urls_list = self.html_text.find_all("h3")
        if not titles_list or not urls_list:
            print("Titles or titles URLs not found!")
            return {}
        return self.__collect_titles(titles_list, urls_list, count)

    @staticmethod
    def __collect_titles(titles_list, urls_list, count):
        titles_dict = OrderedDict()
        for index, line in enumerate(titles_list[:count]):
            title = line["alt"].lower()
            url = urls_list[index]
            url = url.find("a")["href"]
            titles_dict[title] = url
        return titles_dict
