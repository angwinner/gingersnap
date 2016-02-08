'''
Created on Jan 23, 2016

@author: awinner
'''
import unittest
from library import Library
from StringIO import StringIO

class Test(unittest.TestCase):

    def test_create_library(self):
        testlib = Library()
        assert len(testlib.shelves) == 10
        assert testlib.shelves[0].dewey_start == 0
        assert testlib.shelves[0].name == 'General works, Computer Science and Information'
        assert testlib.shelves[1].dewey_start == 100
        assert testlib.shelves[1].name == 'Philosophy and Psychology'
        assert testlib.shelves[2].dewey_start == 200
        assert testlib.shelves[2].name == 'Religion'
        assert testlib.shelves[3].dewey_start == 300
        assert testlib.shelves[3].name == 'Social Sciences'
        assert testlib.shelves[4].dewey_start == 400
        assert testlib.shelves[4].name == 'Language'
        assert testlib.shelves[5].dewey_start == 500
        assert testlib.shelves[5].name == 'Pure Science'
        assert testlib.shelves[6].dewey_start == 600
        assert testlib.shelves[6].name == 'Technology'
        assert testlib.shelves[7].dewey_start == 700
        assert testlib.shelves[7].name == 'Arts & Recreation'
        assert testlib.shelves[8].dewey_start == 800
        assert testlib.shelves[8].name == 'Literature'
        assert testlib.shelves[9].dewey_start == 900
        assert testlib.shelves[9].name == 'History & Geography'
    
    def test_add_book(self):
        testlib = Library()
        testlib.add_book(006.74, 'Teach Yourself HTML and CSS')
        testlib.add_book(576.82, 'A New History of Life')
        testlib.add_book(741.5942, 'The Thrilling Adventures of Lovelace and Babbage')
        assert testlib.shelves[0].books[0].dewey == 006.74
        assert testlib.shelves[0].books[0].title == 'Teach Yourself HTML and CSS'
        assert testlib.shelves[5].books[0].dewey == 576.82
        assert testlib.shelves[5].books[0].title == 'A New History of Life'
        assert testlib.shelves[7].books[0].title == 'The Thrilling Adventures of Lovelace and Babbage'
        
    def test_sorting(self):
        testlib = Library()
        testlib.add_book(100.32, 'First Book')
        testlib.add_book(199.3, 'Last Book')
        testlib.add_book(150, 'Middle Book')
        assert testlib.shelves[1].books[0].title == 'First Book'
        assert testlib.shelves[1].books[1].title == 'Middle Book'
        assert testlib.shelves[1].books[2].title == 'Last Book'
        
    def test_remove_book(self):
        testlib = Library()
        testlib.add_book(576.82, 'A New History of Life')
        testlib.add_book(575.01, 'An Old History of Life')
        assert len(testlib.shelves[5].books) == 2
        testlib.remove_book(576.82)
        assert len(testlib.shelves[5].books) == 1
        # remove nonexistent book
        testlib.remove_book(501.2)
        assert len(testlib.shelves[5].books) == 1
        
    def test_duplicate_books(self):
        testlib = Library()
        testlib.add_book(576.82, 'A New History of Life')
        testlib.add_book(576.82, 'A New History of Life')
        assert len(testlib.shelves[5].books) == 2
        testlib.remove_book(576.82)
        assert len(testlib.shelves[5].books) == 1
        
    def test_report_inventory(self):
        testlib = Library()
        testlib.add_book(006.74, 'Teach Yourself HTML and CSS')
        testlib.add_book(576.82, 'A New History of Life')
        testlib.add_book(741.5942, 'The Thrilling Adventures of Lovelace and Babbage')
        testlib.add_book(741.5942, 'The Thrilling Adventures of Lovelace and Babbage')
        out = StringIO()
        report = "The books in this library are:\n"
        report += "6.74 - Teach Yourself HTML and CSS\n"
        report += "576.82 - A New History of Life\n"
        report += "741.5942 - The Thrilling Adventures of Lovelace and Babbage\n"
        report += "741.5942 - The Thrilling Adventures of Lovelace and Babbage\n"
        testlib.report_inventory(out)
        assert out.getvalue() == report

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_create_library']
    unittest.main()