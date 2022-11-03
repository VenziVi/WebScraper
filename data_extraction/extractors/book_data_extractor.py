import re
import unicodedata
from constants import Indexes, DEFAULT_FLOAT, DEFAULT_VALUE, RATING_DICT


class BookDataExtractor(object):
    """
    The BookDataExtractor class is initialized with HTML text
    and provides functions that return extracted data from a given page text.
    Attributes:
        html_text:
            Contains html-text that has been processed with Beautiful Soup
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

    def get_upc(self):
        """
        Returns UPC of the book as a string
        :return str:
        """
        upc = None
        result = self.html_text.find_all("td")
        try:
            upc = result[Indexes.UPC].text
        except IndexError:
            print("Book UPC not found!")
        return upc

    def get_title(self):
        """
        Returns title of the book as a string
        :return str:
        """
        encoded_title = None
        title = self.html_text.find("h1")
        try:
            encoded_title = unicodedata.normalize("NFKD", title.text)\
                            .encode("latin-1", "ignore")
        except AttributeError:
            print("Title not found!")
        return encoded_title

    def get_genre(self):
        """
        Returns book genre as a string
        :return str:
        """
        genre = None
        line = self.html_text.find_all("li")
        try:
            genre = line[Indexes.GENRE].text.strip()
        except IndexError:
            print("Genre not found!")
        return genre

    def get_product_type(self):
        """
        Returns product type as a string
        :return str:
        """
        product_type = None
        result = self.html_text.find_all("td")
        try:
            product_type = result[Indexes.TYPE].text
        except IndexError:
            print("Product type not found!")
        return product_type

    def get_price_incl_tax(self):
        """
        Returns book price as a float
        :return float:
        """
        price = DEFAULT_FLOAT
        result = self.html_text.find_all("td")
        try:
            price = re.findall(r"(\d+.\d+)", result[Indexes.PRICE_INC].text).pop()
        except IndexError:
            print("Book price not found!")
        return float(price)

    def get_price_excl_tax(self):
        """
        Returns book price exclusive tax as a float
        :return float:
        """
        price = DEFAULT_FLOAT
        result = self.html_text.find_all("td")
        try:
            price = re.findall(r"(\d+.\d+)", result[Indexes.PRICE_EX].text).pop()
        except IndexError:
            print("Book price excl. tax not found!")
        return float(price)

    def get_tax(self):
        """
        Returns book price tax as a float
        :return float:
        """
        tax = DEFAULT_FLOAT
        result = self.html_text.find_all("td")
        try:
            tax = re.findall(r"(\d+.\d+)", result[Indexes.TAX].text).pop()
        except IndexError:
            print("Book tax not found!")
        return float(tax)

    def get_quantity(self):
        """
        Returns book availability as integer
        :return int:
        """
        qty = DEFAULT_VALUE
        result = self.html_text.find_all("td")
        try:
            line = result[Indexes.QUANTITY].text
            qty = re.findall(r"(\d+)", line).pop()
        except IndexError:
            print("Book quantity not found!")
        return int(qty)

    def get_rating(self):
        """
        Returns book rating as int
        :return int:
        """
        rating = "Zero"
        result = self.html_text.find_all("p")
        search_pattern = r"([a-z]{4})-([a-z]{6})\W{1}([A-Z][a-z]+)"
        match = re.findall(search_pattern, str(result))
        try:
            item = match.pop(DEFAULT_VALUE)
            rating = item[Indexes.RATING]
        except IndexError:
            print("Book rating not found!")
        return RATING_DICT[rating]

    def get_description(self):
        """
        Returns the description of the book as a string
        :return str:
        """
        encoded_description = None
        article = self.html_text.find("article", class_="product_page")
        try:
            paragraphs = article.find_all("p")
            description = paragraphs[Indexes.DESCRIPTION].text.strip()
            encoded_description = unicodedata.normalize("NFKD", description).encode("latin-1", "ignore")
        except AttributeError:
            print("Book description not found!")
        return encoded_description
