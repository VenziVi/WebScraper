from data_extraction.extractors.page_data_extractor import PageDataExtractor


EXT_TO_REMOVE = "../../../"
MAX_BOOKS_COUNT = 1000
CATALOGUE_EXT = "catalogue/"


class UrlCollector(object):
    """
    UrlCollector class is initialize with home page url.
    Collect books titles and urls in a dictionary _books_dict
    """
    def __init__(self, request_handler):
        self.__request_handler = request_handler
        self.__books_count = MAX_BOOKS_COUNT
        self.__needed_books = MAX_BOOKS_COUNT
        self.__page_extractor = None
        self.__genres_urls = []
        self.__books_dict = {}

    @staticmethod
    def __set_extension(url):
        """
        Construct correct url.
        Removes unnecessary extension if any,
        or add required extensions.
        :param url:
        :return str:
        """
        if EXT_TO_REMOVE in url:
            url = str(url).replace(EXT_TO_REMOVE, "")
            return CATALOGUE_EXT + url
        if CATALOGUE_EXT in url:
            return url
        return CATALOGUE_EXT + url

    def __set_page_extractor(self, value):
        """
        Set page_extractor. If page_extractor is None, creates an instance.
        If page_extractor is all ready created, sets new value.
        :param value:
        :return:
        """
        try:
            if self.__page_extractor:
                self.__page_extractor.html_text = value
            else:
                self.__page_extractor = PageDataExtractor(value)
        except ValueError as ve:
            print(ve)
            self.__page_extractor = None

    def __set_books_count(self, value):
        """
        Sets value to books_count and needed_books.
        :param value:
        :return:
        """
        self.__books_count = value
        self.__needed_books = value

    def __set_urls_extensions(self):
        """
        Passes all books urls tru set_extension function
        :return:
        """
        for book in self.__books_dict:
            self.__books_dict[book] = self.__set_extension(self.__books_dict[book])

    def __calculate_books_to_take(self):
        """
        Calculates the required number of books.
        If needed_books are less than books per page
        returns needed_books
        else returns count of all books on the page
        :return int:
        """
        books_on_page = self.__page_extractor.get_books_per_page()
        books_to_take = books_on_page
        if books_on_page > self.__needed_books:
            books_to_take = self.__needed_books
        self.__needed_books -= books_to_take
        return books_to_take

    def __extract_books_urls(self):
        """
        Validates request handler.
        If genres_urls is not empty, calls get_books_urls for each page of the current genre.
        Else calls get_books_urls for all genres
        :return:
        """
        if self.__genres_urls:
            for genre_url in self.__genres_urls:
                if not genre_url:
                    continue
                self.__get_books_urls(genre_url)
        else:
            self.__get_books_urls()

    def __get_books_urls(self, genre_url=""):
        """
        Takes books titles and urls and add them to books_dict
        until it collects required books count
        or next page is None.
        Calculate required books from each page and extracts next page url extension
        returns if page_text or next_page is None
        :param genre_url:
        :return:
        """
        page_text = self.__request_handler.get_page(genre_url)
        self.__set_page_extractor(page_text)
        if not self.__page_extractor:
            return
        next_page = self.__page_extractor.get_next_page()

        while self.__needed_books > 0:
            books_to_take = self.__calculate_books_to_take()
            self.__books_dict.update(self.__page_extractor.get_titles_from_collection_page(books_to_take))
            if not next_page:
                break
            extension = self.__set_extension(next_page)
            if genre_url:
                extension = genre_url + next_page
            page_text = self.__request_handler.get_page(extension)
            self.__set_page_extractor(page_text)
            if not self.__page_extractor:
                return
            next_page = self.__page_extractor.get_next_page()

    def __set_genres_urls(self, books_genres):
        """
        Takes list of books genres.
        Calls get_books_categories which  returns a dictionary of all existing books genres,
        key: genre, value: genre url extension.
        Search in genres dict if genre exists.
        If exists sets the genre url to genres_urls.
        If it doesn't exist, append None.
        :param books_genres:
        :return:
        """
        page_as_text = self.__request_handler.get_page()
        self.__set_page_extractor(page_as_text)
        if not self.__page_extractor:
            return
        genres = self.__page_extractor.get_books_categories()
        for genre in books_genres:
            if "-" in genre:
                genre = " ".join(genre.split("-"))
            if genre.lower() in genres.keys():
                self.__genres_urls.append(genres[genre.lower()])
            else:
                print("Genre: '{0}' doesn't exist!".format(genre))
                self.__genres_urls.append(None)

    def get_all_genres(self):
        """
        Returns list of all existing genres.
        :return list:
        """
        homepage = self.__request_handler.get_page()
        self.__set_page_extractor(homepage)
        if not self.__page_extractor:
            return
        genres = self.__page_extractor.get_books_categories()
        genre_list = list(genres.keys())
        return genre_list

    def collect_books_urls(self, books_count=None, genres_list=None):
        """
        Collect books titles and urls for a given books_count and genres_list.
        If none of them, collect all books
        :param books_count:
        :param genres_list:
        :return dict:
        """
        if books_count:
            self.__set_books_count(books_count)
        if genres_list:
            self.__set_genres_urls(genres_list)
        self.__extract_books_urls()
        self.__set_urls_extensions()
        return self.__books_dict
