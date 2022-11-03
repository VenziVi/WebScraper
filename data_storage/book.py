import random
import string


class Book(object):
    def __init__(self, upc, title, genre, product_type, price_with_tax,
                 price_excl_tax, tax, qty, rating, description):
        self.upc = upc
        self.title = title
        self.genre = genre
        self.product_type = product_type
        self.price = price_with_tax
        self.price_excl_tax = price_excl_tax
        self.tax = tax
        self.available = qty
        self.rating = rating
        self.description = description

    @property
    def upc(self):
        return self.__upc

    @upc.setter
    def upc(self, value):
        if not value:
            self.__upc = "N/A" + " -{0}".format(self.__upc_generator())
        else:
            self.__upc = value
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not value:
            self.__title = "N/A"
        else:
            self.__title = value

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        if not value:
            self.__genre = "N/A"
        else:
            self.__genre = value

    @property
    def product_type(self):
        return self.__product_type

    @product_type.setter
    def product_type(self, value):
        if not value:
            self.__product_type= "N/A"
        else:
            self.__product_type = value

    @property
    def price(self):
        return self.__price_with_tax

    @price.setter
    def price(self, value):
        if not value or value == 0.0:
            self.__price_with_tax = "N/A"
        else:
            self.__price_with_tax = value

    @property
    def price_excl_tax(self):
        return self.__price_excl_tax

    @price_excl_tax.setter
    def price_excl_tax(self, value):
        if not value or value == 0.0:
            self.__price_excl_tax = "N/A"
        else:
            self.__price_excl_tax = value

    @property
    def tax(self):
        return self.__tax

    @tax.setter
    def tax(self, value):
        if not value or value <= 0.0:
            self.__tax = "N/A"
        else:
            self.__tax = value

    @property
    def available(self):
        return self.__qty

    @available.setter
    def available(self, value):
        if not value or value < 0:
            self.__qty = "N/A"
        else:
            self.__qty = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if not value or value < 0:
            self.__rating = "N/A"
        else:
            self.__rating = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if not value:
            self.__description = "N/A"
        else:
            self.__description = value

    def __getitem__(self, item):
        return getattr(self, item.lower())

    @staticmethod
    def __upc_generator():
        f_part = str(random.randint(1000, 10000))
        letter = random.choice(string.ascii_letters)
        s_part = str(random.randint(10, 1000))
        return f_part + letter + s_part
