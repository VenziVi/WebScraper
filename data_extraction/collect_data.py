from data_extraction.extractors.book_data_extractor import BookDataExtractor
from data_extraction.filters.filter_books import FilterBooks
from data_extraction.filters.filter_by_title import TitleFilter
from data_extraction.filters.filter_by_titles import TitlesFilter


class CollectData(object):
    """
    The Collect Data class collects book data according to given criteria and filters
    """
    def __init__(self, books_count, genres, filters, keywords, title, file_path,
                 request_handler, url_collector, collection):
        self.__collection = collection
        self.__url_collector = url_collector
        self.__request_handler = request_handler
        self.__content_extractor = None
        self.__books_count = books_count
        self.__genres = genres
        self.__filters = filters
        self.__keywords = keywords
        self.__title = title
        self.__file_path = file_path

    @property
    def collection(self):
        return self.__collection

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

    def __add_book_to_collection(self):
        self.__collection.add_entity(
            self.__content_extractor.get_upc(),
            self.__content_extractor.get_title(),
            self.__content_extractor.get_genre(),
            self.__content_extractor.get_product_type(),
            self.__content_extractor.get_price_incl_tax(),
            self.__content_extractor.get_price_excl_tax(),
            self.__content_extractor.get_tax(),
            self.__content_extractor.get_quantity(),
            self.__content_extractor.get_rating(),
            self.__content_extractor.get_description()
        )

    def __get_books_soups(self):
        """
        Select the type of filter to apply
        :return:
        """
        filter = None
        if self.__file_path:
            filter = TitlesFilter(self.__request_handler, self.__file_path)
            if not filter.titles_list:
                return
        elif self.__title:
            filter = TitleFilter(self.__request_handler, self.__title)
        elif self.__filters or self.__keywords:
            filter = FilterBooks(self.__request_handler, self.__filters, self.__keywords)

        titles_dict = self.__url_collector.collect_books_urls(self.__books_count, self.__genres)

        if filter:
            return filter.filter_books(titles_dict)
        else:
            return self.__request_handler.get_pages_text_async(titles_dict.values())

    def collect_books_data(self):
        """
        Collect a list of soups according to set criteria and filters.
        Collect data for all books in the soup list.
        :return:
        """
        print("Scraping books data...")
        soup_list = self.__get_books_soups()
        if not soup_list:
            return
        for soup in soup_list:
            self.__set_content_extractor(soup)
            if self.__content_extractor:
                self.__add_book_to_collection()
