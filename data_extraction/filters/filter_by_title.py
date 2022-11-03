from data_extraction.filters.filter import BaseFilter


class TitleFilter(BaseFilter):
    def __init__(self, request_handler, title):
        super(TitleFilter, self).__init__(request_handler)
        self.title = title

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        title = " ".join(value)
        self.__title = title.lower()

    def filter_books(self, titles_dict):
        if self.title in titles_dict:
            return [self.request_handler.get_page(titles_dict[self.title])]