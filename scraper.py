import os.path

import requests
import validators
from bs4 import BeautifulSoup


class Scraper:
    # Soup contains the content of Beautifulsoup
    soup = None
    # Response of the GET-request
    response = None
    # Dictionary to save the files to
    dir_path = ""

    # Class constructor requires the URL to the website and an existing directory
    def __init__(self, url, dirp):
        # check status code for response received
        # success code - 200
        if self.make_request(url) and self.check_dir(dirp):
            # Parsing the HTML
            self.soup = BeautifulSoup(self.response.content, 'html.parser')
            print("Scraper initialized - Soup created")
        else:
            print("Scraper initialization failed")
            raise Exception("Invalid URL or Path")

    def make_request(self, link):
        # False means the request was not a link
        ret = False
        if validators.url(link):
            # If the String is a link, it makes the GET-request
            self.response = requests.get(link)
            print("Response code: " + str(self.response))
            ret = True
        else:
            print("Invalid URL")
        return ret

    # Check if the given path is a valid directory
    def check_dir(self, path):
        ret = False
        # Checks if the dir exists and is valid or if it is empty
        if not path:
            self.dir_path = os.getcwd() + "\\"
            print("No path selected, using current dir:\n"
                  + self.dir_path)
            ret = True
        elif os.path.isdir(path):
            self.dir_path = path
            print("Path specified: " + self.dir_path)
            ret = True
        else:
            print("Unclear path error, path might be invalid or not exist")
        return ret

    # Returns the whole website with HTML tags
    def get_html(self):
        html_file_path = self.dir_path + "website.html"
        # Write the retrieved contents to a newly created file
        f = open(html_file_path, "w", encoding="utf-8")
        f.write(self.soup.prettify())
        f.close()
        print("Wrote HTML contents to: " + html_file_path)

    # Returns only the text inside the <p> tag
    def get_text(self):
        ret = ""
        text_file_path = self.dir_path + "texts.txt"
        lines = self.soup.find_all('p')

        for line in lines:
            ret += str(line.text) + "\n"

        # Write string to file
        f = open(text_file_path, "w", encoding="utf-8")
        f.write(ret)
        f.close()
        print("Wrote TXT contents to: " + text_file_path)

    # Returns all the links inside an <a> tag
    def get_links(self):
        ret = ""
        links_file_path = self.dir_path + "links.txt"

        # find all the anchor tags with "href"
        for link in self.soup.find_all('a'):
            ret += str(link.get('href')) + "\n"

        f = open(links_file_path, "w", encoding="utf-8")
        f.write(ret)
        f.close()
        print("Wrote LINKS contents to: " + links_file_path)

    # Returns all the images inside an <img> tag
    def get_images(self):
        ret = ""
        images_file_path = self.dir_path + "images.txt"
        images_list = []

        images = self.soup.select('img')
        for image in images:
            # Creates a dictionary with the src and alt of an image
            src = image.get('src')
            alt = image.get('alt')
            images_list.append({"src": src, "alt": alt})

        for image in images_list:
            ret += str(image) + "\n"

        f = open(images_file_path, "w", encoding="utf-8")
        f.write(ret)
        f.close()
        print("Wrote IMAGE contents to: " + images_file_path)
