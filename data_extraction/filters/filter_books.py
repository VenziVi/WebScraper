from data_extraction.extractors.book_data_extractor import BookDataExtractor
from data_extraction.filters.filter import BaseFilter


class FilterBooks(BaseFilter):
    def __init__(self, request_handler, filters_list, keywords):
        super(FilterBooks, self).__init__(request_handler)
        self.__content_extractor = None
        self.__filters = filters_list
        self.__keywords = keywords
        self.__filtered_soups = []

    @staticmethod
    def __parse_filter(current_filter):
        """
        Takes a current_filter argument "price>20"
        Search for the current operator and split a string by operator
        argument "price", operator ">" and value "20"
        :param current_filter:
        :return str, str, str:
        """
        operator = ""
        if "<" in current_filter:
            operator = "<"
        elif ">" in current_filter:
            operator = ">"
        elif "=" in current_filter:
            operator = "="
        try:
            argument, value = current_filter.split(operator)
        except ValueError:
            return None
        return argument, operator, value

    @staticmethod
    def __book_match(book_value, operator, value):
        """
        Compares book_value and value with the given comparison operator
        :param book_value:
        :param operator:
        :param value:
        :return bool:
        """
        if operator == "<":
            return book_value < value
        if operator == ">":
            return book_value > value
        if operator == "=":
            return book_value == value
        return None

    def __set_content_extractor(self, value):
        """
        Set content_extractor. If content_extractor is None, creates an instance.
        If content_extractor is all ready created, sets new value.
        :param value:
        :return:
        """
        try:
            if self.__content_extractor:
                self.__content_extractor.html_text = value
            else:
                self.__content_extractor = BookDataExtractor(value)
        except ValueError as ve:
            print(ve)
            self.__content_extractor = None

    def __filter_book(self):
        """
        Takes books filters list and for each filter compares the current book value
        with the value in the current filter string.
        If one doesn't match return False, else return True
        :return bool:
        """
        book_value = ""
        for curr_filter in self.__filters:
            if not curr_filter:
                continue
            argument, operator, value = self.__parse_filter(curr_filter)
            if argument.lower() == "price":
                book_value = self.__content_extractor.get_price_incl_tax()
                value = float(value)
            elif argument.lower() == "rating":
                book_value = self.__content_extractor.get_rating()
                value = int(value)
            elif argument.lower() == "available":
                book_value = self.__content_extractor.get_quantity()
                value = int(value)
            if not self.__book_match(book_value, operator, value):
                return False
        return True

    def __search_for_keywords(self):
        """
        Search for all self._keywords in the book description.
        All keywords must be present in the description.
        If one of keywords does not exist, returns False.
        :return Bool:
        """
        for word in self.__keywords:
            book_description = self.__content_extractor.get_description().lower()
            if not word.lower() in book_description:
                return False
        return True

    def __filter_by_filters_and_keywords(self, soup_list):
        """
        Applies the filters to a given list of soups
        :param soup_list:
        :return:
        """
        for soup in soup_list:
            is_match = True
            self.__set_content_extractor(soup)
            if not self.__content_extractor:
                continue
            if self.__filters:
                is_match = self.__filter_book()
            if is_match and self.__keywords:
                is_match = self.__search_for_keywords()
            if is_match:
                self.__filtered_soups.append(soup)

    def filter_books(self, books_dict):
        soup_list = self.request_handler.get_pages_text_async(books_dict.values())
        self.__filter_by_filters_and_keywords(soup_list)
        return self.__filtered_soups
