import sys
import os
import gui.button
from argument_parser import ArgumentParser
from data_extraction.collect_data import CollectData
from data_extraction.request_handler import RequestHandler
from data_extraction.url_collector import UrlCollector
from data_storage.data_holder import DataHolder

if os.getcwd() not in sys.path:
    sys.path.insert(0, os.getcwd())


BASE_URL = "https://books.toscrape.com/"


def init_request_handler():
    try:
        page_handler = RequestHandler.create_request_handler(BASE_URL)
    except ValueError as ve:
        print(ve)
        return None
    else:
        return page_handler


def main(args):
    request_handler = init_request_handler()
    if not request_handler:
        exit(1)
    url_collector = UrlCollector(request_handler)
    data_holder = DataHolder()

    if args.gui:
        gui.button.Button(request_handler, url_collector, data_holder)
    else:
        collector = CollectData(args.books, args.genres, args.filters, args.keywords, args.title,
                                args.titles_json, request_handler, url_collector, data_holder)
        collector.collect_books_data()
        collector.collection.sort_collection(args.sorting)
        collector.collection.export_data_to_file()


if __name__ == "__main__":
    parser = ArgumentParser()
    main(parser.parse_arguments())
