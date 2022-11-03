import re
import grequests
from bs4 import BeautifulSoup
import requests


URL_REGEX = (
    r"[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\."
    r"[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
)


class RequestHandler(object):
    """
    Used to create request and return lxml text using BeautifulSoup modul.
    RequestHandler class is initialized with base url.
    its functions accept extension that they concatenate with base url.
    Arguments:
        base_url:
            Main url of the web application. Used to get lxml text from the home page.
            It can be concatenated with extensions in order to get other pages lxml text.
    """
    def __init__(self, base_url):
        self.__base_url = base_url

    @classmethod
    def create_request_handler(cls, base_url):
        """
        Check that the given URL is in a valid format.
        If valid returns instance of RequestHandler class,
        else raise ValueError
        :param base_url:
        :return:
        """
        if not re.match(URL_REGEX, base_url):
            raise ValueError("Invalid URL format '{0}'!".format(base_url))
        return cls(base_url)

    def __get_page_text(self, url_extension=""):
        """
        Accepts url extension, concatenate base url with extension if any.
        Try to get response.
        If success returns lxml text using BeautifulSoup
        :param extension:
        :return str:
        """
        content = requests.get(self.__base_url + url_extension)
        content.raise_for_status()
        text = BeautifulSoup(content.text.encode("latin-1"), "lxml")
        return text

    def get_page(self, url_extension=""):
        """
        Accepts url extension.
        Try to get text from get page text.
        If no errors occur, returns page text, else print error and return None
        :param extension:
        :return:
        """
        try:
            page_text = self.__get_page_text(url_extension)
        except requests.exceptions.RequestException as ex:
            print(ex)
            return None
        return page_text

    def get_pages_text_async(self, url_list):
        """
        Accepts a list of extensions and concatenates them with base url.
        Send an asynchronous request using the grequests module.
        For each response, get lxml text using BeautifulSoup.
        Returns list of soups
        :param url_list:
        :return list:
        """
        soup_list = []
        try:
            async_requests = [grequests.get(self.__base_url + url) for url in url_list]
        except TypeError:
            return soup_list

        content = grequests.map(async_requests)
        for book in content:
            if not book:
                continue
            soup = BeautifulSoup(book.text.encode("latin-1"), "lxml")
            soup_list.append(soup)
        return soup_list
