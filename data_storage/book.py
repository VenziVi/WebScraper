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
