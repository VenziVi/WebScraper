import argparse


FILTERS_LIST = ["rating>", "rating=", "rating<",
                "price>", "price=", "price<",
                "available>", "available=", "available<"]
SORTING_LIST = ["rating-ascending", "price-ascending", "genre-ascending", "quantity-ascending",
                "rating-descending", "price-descending", "genre-descending", "quantity-descending",
                "default-ascending", "default-descending"]


class ArgumentParser(object):
    """
    The ArgumentParser class reads and converts command line arguments.
    """
    def __init__(self):
        self._parser = argparse.ArgumentParser(
            description="""The following arguments can be used:
                b - number of books
                g - list of genres to search through
                s - list of sorting (for the output, ascending or descending)
                f - list of priority filters for which books to exclude from the scrape
                d - list of keywords to be searched from the description
                t - title of a book to search for 
                F - list of book titles to search for (from given json)
                X - GUI """,
            formatter_class=argparse.RawTextHelpFormatter,
        )
        self._parser.add_argument("-b", "--books", nargs="?", type=int, choices=range(1, 1001), metavar="[1-1000]")
        self._parser.add_argument("-g", "--genres", nargs="+", type=str)
        self._parser.add_argument("-s", "--sorting", nargs="+", choices=SORTING_LIST, metavar="sorting list")
        self._parser.add_argument("-f", "--filters", nargs="+", type=self.validate_filter)
        self._parser.add_argument("-d", "--keywords", nargs="+", type=str)
        self._parser.add_argument("-t", "--title", nargs="+", type=str)
        self._parser.add_argument("-F", "--titles_json", type=str)
        self._parser.add_argument("-X", "--gui", action="store_true")

    def parse_arguments(self):
        """ Returns parsed arguments."""
        return self._parser.parse_args()

    @staticmethod
    def validate_filter(current_filter):
        """
        Validate input filter.
        The filter must start with one of the prefixes in FILTERS_LIST
        :param current_filter:
        :return:
        """
        for prefixes in FILTERS_LIST:
            if current_filter.startswith(prefixes):
                return current_filter
        print("Incorrect fiter: '{0}'!".format(current_filter))
        print("Possible filters: '{0}'.".format(", ".join(FILTERS_LIST)))
