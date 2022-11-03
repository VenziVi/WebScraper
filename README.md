# Python Bookscraper Project - Team 2

* ## Project Summary
The purpose of this project is to scrape https://books.toscrape.com and collect its data, based on users' preferences. The collection can store all books on the website or a number of books based on the input filters. After the data has been collected, the complete JSON can be sorted if required.


* ## Requirements

This script uses [virtualenv with python 2.7](https://docs.python.org/2.7/)...   
To run the script successfully you must have first installed the following libraries: 
- BeautifulSoup 4
- requests
- grequests
- lxml parser

To run the GUI you must have the following libraries:
- Pillow
- pygame
- Tkinter
Full list of requirements can be found in "requirements.txt"

* ## Usage

The script is used to gather data from https://books.toscrape.com/
You can write the following command in your terminal:
  ```
  python main.py [-b <number of books>]
                 [-g <genre to search for>]           - list of genres to search through
                 [-s <sorting type> <sort direction>] - list of sorting (for the output, ascending or descending)
                 [-f <filter by><sign><number>]       - list of priority filters for which books to exclude from the scrape e.g. 'price>20' or 'rating<3'
                 [-d <keywords>]                      - list of keywords to be searched from the description
                 [-t <title>]                         - title of a book to search for 
                 [-F <path to json>]                  - list of book titles to search for (from given json)
                 [-X]                                 - GUI
                 
  ```
  
The same options can be viewed on the GUI.
  
* ## Technical Details

To get data from https://books.toscrape.com/, the script uses the requests, grequests and BeautifulSoup 4 libraries.
Using the requests library, we receive the response as html text. This text is then passed to BeautifulSoup 4 and it
converts it to xml. The built-in methods of BeautifulSoup give us the ability to search for html tags which are
used to scrape the desired data from the website. The filters only scrape that data which matches the criteria and then is added to the collection of books. The sort is applied just before the collection is saved as a JSON file.

  
### Workflow:

The expected workflow is:

1. The user entered arguments are parsed to the main function
2. Depending on the arguments, the GUI is started or the program is executed in the console.
3. The targeted website is sent to requests or grequests library to receive a response.
4. The response is then converted to html data via the ".content" method.
5. The html data is sent to BeautifulSoup 4, which converts it to xml via the lxml tree builder.
6. Using the methods "find" and "find_all", we are searching for specific tags and descriptions or css classes. If filters are applied, the only content that is scraped is the one that is matching the filter criteria. When a match is found, we obtain the content between the angle brackets ("< >") with the method ".text"
5. For every book, a class instance of type Book is created. The instance stores all of the information for the given book in a dictionary.
6. The instances are stored in a list, which is then sorted if such argument is given in the CLI or GUI.
7. The sorted list of book instances is the stored in a JSON.
