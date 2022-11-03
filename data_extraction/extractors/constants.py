from enum import Enum


class Indexes(Enum):
    UPC = 0
    TYPE = 1
    PRICE_EX = 2
    PRICE_INC = 3
    TAX = 4
    QUANTITY = 5
    GENRE = 2
    RATING = 2
    DESCRIPTION = 3


RATING_DICT = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Zero": 0}

DEFAULT_FLOAT = 0.0
DEFAULT_VALUE = 0

BOOKS_CALC_CONST = 1
GENRES_INDEX = 1
GENRES_START_INDEX = 3
GENRES_END_INDEX = 53
