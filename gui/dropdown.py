import ttk
from main import init_request_handler
from data_extraction.url_collector import UrlCollector
from entry import Entry


class DropdownMenu(Entry):
    def __init__(self):
        Entry.__init__(self)
        self.category_list = self.get_category_list()
        self.categoriesMenu = ttk.Combobox(self.root, state='readonly', values=self.category_list)
        self.categoriesMenu.set(self.category_list[0])
        self.categoriesMenu.bind("<<ComboboxSelected>>", self.highlight_category_clear)
        self.categoriesMenuWindow = self.canvas1.create_window(105, 125, window=self.categoriesMenu, width=135)
        self.ratingList = ["All ratings", "1", "2", "3", "4", "5"]
        self.ratingMenu = ttk.Combobox(self.root, state='readonly', values=self.ratingList)
        self.ratingMenu.set(self.ratingList[0])
        self.ratingMenu.bind("<<ComboboxSelected>>", self.highlight_rating_clear)
        self.ratingMenuWindow = self.canvas1.create_window(200, 200, window=self.ratingMenu, width=85)

    def get_category_list(self):
        request_handler = init_request_handler()
        collector = UrlCollector(request_handler)
        category_list = collector.get_all_genres()
        category_list.sort()
        category_list = [each_string.capitalize() for each_string in category_list]
        category_list.insert(0, "All categories")
        return category_list

    def highlight_category_clear(self, event):
        current = self.categoriesMenu.get()
        self.categoriesMenu.set("")
        self.categoriesMenu.set(current)

    def highlight_rating_clear(self, event):
        current = self.ratingMenu.get()
        self.ratingMenu.set("")
        self.ratingMenu.set(current)

    def get_category(self):
        category = self.categoriesMenu.get()
        if category == "All categories":
            return None
        return category

    def get_rating(self):
        rating = self.ratingMenu.get()
        if rating == "All ratings":
            return None
        return rating
