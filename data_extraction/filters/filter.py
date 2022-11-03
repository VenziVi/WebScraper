class BaseFilter(object):
    def __init__(self, request_handler):
        if type(self) is BaseFilter:
            raise TypeError("BaseFilter is an abstract class and cannot be instantiated directly!")
        self.request_handler = request_handler

    def filter_books(self, books_dict):
        NotImplementedError("Subclasses must override filter_books method!")