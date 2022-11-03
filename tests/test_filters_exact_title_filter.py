import unittest
from data_extraction.filters.exact_title_filter import ExactTitleFilter
import variables_helper as vh


class TestExactTitleFilter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.title_filter = ExactTitleFilter("a light in the attic")

    #  title
    def test__title__set_given_title_and_make_it_lower_case__success(self):
        expected = "a light in the attic"
        actual = self.title_filter.title
        self.assertEqual(expected, actual)

    # search_book_by_exact_title
    def test__search_book_by_exact_title__success(self):
        self.title_filter.title = ["a light in the attic"]
        expected = "catalogue/a-light-in-the-attic_1000/index.html"
        actual = self.title_filter.search_book_by_exact_title(vh.expected_dict_of_titles)
        self.assertEqual(expected, actual)
