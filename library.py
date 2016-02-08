'''
Created on Jan 23, 2016
An exercise for CodeFellows
@author: awinner
'''
import sys

class Library(object):
    '''
    All interactions with the library system should use methods of the Library
    object. On initialization, the Library establishes a fixed number of shelves
    corresponding to dewey decimal categories.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        # create initial shelves
        shelf_data = [(0,'General works, Computer Science and Information'),
                      (100,'Philosophy and Psychology'),
                      (200,'Religion'),
                      (300,'Social Sciences'),
                      (400,'Language'),
                      (500,'Pure Science'),
                      (600,'Technology'),
                      (700,'Arts & Recreation'),
                      (800,'Literature'),
                      (900,'History & Geography')
                      ]
                      
        self.shelves = []
        for shelf in shelf_data:
            self.shelves.append(Shelf(shelf[0],shelf[1]))
        
    def find_shelf(self, dewey):
        for shelf in self.shelves:
            if dewey >= shelf.dewey_start and dewey < shelf.dewey_start + 100:
                return shelf
            
    def add_book(self, dewey, title):
        correct_shelf = self.find_shelf(dewey)
        correct_shelf.add_book(dewey, title)
                
    def remove_book(self, dewey):
        correct_shelf = self.find_shelf(dewey)
        correct_shelf.remove_book(dewey)
        
    def report_inventory(self, out=sys.stdout):
        out.write("The books in this library are:\n")
        for shelf in self.shelves:
            for book in shelf.books:
                out.write(str(book)+'\n')
        
class Shelf(object):
    '''
    Each shelf holds books within a range of 100 dewey decimal numbers.
    Books on the shelf are sorted by dewey number.
    Shelves are named according to the dewey decimal category.
    '''
    
    def __init__(self, dewey_start, name):
        self.dewey_start = dewey_start
        self.name = name
        self.books = []
        
    def add_book(self, dewey, title):
        self.books.append(Book(dewey, title))
        self.books.sort()
        
    def remove_book(self, dewey):
        # this dummy book works because two books with the same dewey number
        # evaluate as equal
        to_remove = Book(dewey, 'title')
        try:
            self.books.remove(to_remove)
        except ValueError:
            pass #do nothing if book not on shelf
            
    
class Book(object):
    '''
    Books have two attributes, title and dewey decimal number
    Books compared to other books are ordered by their dewey number
    '''
    
    def __init__(self, dewey, title):
        self.dewey = dewey
        self.title = title
    
    def __repr__(self):
        return str(self.dewey) + " - " + self.title
    
    def __cmp__(self, other):
        if isinstance(other, Book):
            if self.dewey < other.dewey:
                return -1
            if self.dewey > other.dewey:
                return 1
            if self.dewey == other.dewey:
                return 0
            
        