import json

class Data:

    def __init__(self):

        try:
            self.courses = None
            with open('bookmarks.json', encoding='utf-8') as myfile:
                self.bookmarks = json.load(myfile)

        except FileNotFoundError:
            self.bookmarks = []

        except ValueError:
            self.bookmarks = []
            
    def set_courses(self, courses):
        self.courses = courses

    # Adding a bookmark to the file, bookmarks based on course code and normalizes the course code
    def add_bookmark(self, itemIndex):
        if itemIndex not in self.bookmarks:
            self.bookmarks.append(itemIndex.upper())
        with open('bookmarks.json', 'w', encoding='utf-8') as myfile:
            json.dump(self.bookmarks, myfile)

    # Removes a bookmarked normalized course code
    def remove_bookmark(self, itemIndex):
        self.bookmarks.remove(itemIndex.upper())
        with open('bookmarks.json', 'w',  encoding='utf-8') as myfile:
            json.dump(self.bookmarks, myfile)
