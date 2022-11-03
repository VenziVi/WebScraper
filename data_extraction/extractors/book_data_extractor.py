import re
import unicodedata


UPC_INDEX = 0
TYPE_INDEX = 1
PRICE_EX_INDEX = 2
PRICE_INC_INDEX = 3
TAX_INDEX = 4
QUANTITY_INDEX = 5
DESCRIPTION_INDEX = 3
GENRE_INDEX = 2
RATING_INDEX = 2
DEFAULT_FLOAT = 0.0


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
        try:
            result = self.html_text.find_all("td")
            return result[UPC_INDEX].text
        except IndexError:
            print("Book UPC does not exist on this webpage!")
            return None

    def get_title(self):
        """
        Returns title of the book as a string
        :return str:
        """
        title = self.html_text.find("h1").text
        encoded_title = unicodedata.normalize("NFKD", title).encode("latin-1", "ignore")
        return encoded_title

    def get_genre(self):
        """
        Returns book genre as a string
        :return str:
        """
        line = self.html_text.find_all("li")
        return line[GENRE_INDEX].text.strip()

    def get_product_type(self):
        """
        Returns product type as a string
        :return str:
        """
        result = self.html_text.find_all("td")
        try:
            return result[TYPE_INDEX].text
        except IndexError:
            print("Product type does not exist on this webpage!")
            return None

    def get_price_incl_tax(self):
        """
        Returns book price as a float
        :return float:
        """
        result = self.html_text.find_all("td")
        try:
            price = re.findall(r"(\d+.\d+)", result[PRICE_INC_INDEX].text).pop()
        except IndexError:
            print("Book price does not exist on this webpage!")
            return DEFAULT_FLOAT
        return float(price)

    def get_price_excl_tax(self):
        """
        Returns book price exclusive tax as a float
        :return float:
        """
        result = self.html_text.find_all("td")
        try:
            price = re.findall(r"(\d+.\d+)", result[PRICE_EX_INDEX].text).pop()
        except IndexError:
            print("Book price does not exist on this webpage!")
            return DEFAULT_FLOAT
        return float(price)

    def get_tax(self):
        """
        Returns book price tax as a float
        :return float:
        """
        result = self.html_text.find_all("td")
        try:
            tax = re.findall(r"(\d+.\d+)", result[TAX_INDEX].text).pop()
        except IndexError:
            print("Book tax does not exist on this webpage!")
            return DEFAULT_FLOAT
        return float(tax)

    def get_quantity(self):
        """
        Returns book availability as integer
        :return int:
        """
        result = self.html_text.find_all("td")
        try:
            line = result[QUANTITY_INDEX].text
        except IndexError:
            print("Book quantity does not exist on this webpage!")
            return None

        quantity_line = re.findall(r"(\d+)", line)
        quantity = quantity_line.pop()
        return int(quantity)

    def get_rating(self):
        """
        Returns book rating as int
        :return int:
        """
        result = self.html_text.find_all("p")
        search_pattern = r"([a-z]{4})-([a-z]{6})\W{1}([A-Z][a-z]+)"
        match = re.findall(search_pattern, str(result))
        rating_list = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5,
            "Zero": 0,
        }
        for item in match:
            rating = item[RATING_INDEX]
            return rating_list[rating]

    def get_description(self):
        """
        Returns the description of the book as a string
        :return str:
        """
        try:
            article = self.html_text.find("article", class_="product_page")
            paragraphs = article.find_all("p")
        except AttributeError:
            print("Book description does not exist on this webpage!")
            return None
        description = paragraphs[DESCRIPTION_INDEX].text.encode("utf-8").strip()
        return description
