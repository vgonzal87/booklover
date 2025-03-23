import unittest
from booklover import BookLover
#import pandas as pd

class BookLoverTestSuite(unittest.TestCase):
    
	def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
		my_books = BookLover("Victoria", "email.com", "fantasy")
		my_books.add_book("ACOTAR", 5)
		self.assertIn("ACOTAR", my_books.book_list["book_name"].values)
		
	def test_2_add_book(self):
		# add the same book twice. Test if it's in `book_list` only once.
		my_books = BookLover("Victoria", "email.com", "fantasy")
		my_books.add_book("ACOTAR", 5)
		my_books.add_book("ACOTAR", 5)
		self.assertTrue(sum(my_books.book_list.book_name == "ACOTAR") == 1)
		
	def test_3_has_read(self): 
		# pass a book in the list and test if the answer is `True`.
		my_books = BookLover("Victoria", "email.com", "fantasy")
		my_books.add_book("ACOTAR", 5)
		self.assertTrue(my_books.has_read("ACOTAR"))
		
	def test_4_has_read(self): 
		# pass a book NOT in the list and use `assert False` to test the answer is `True`
		my_books = BookLover("Victoria", "email.com", "fantasy")
		my_books.add_book("ACOTAR", 5)
		self.assertFalse(my_books.has_read("ACOMAF"))
		
	def test_5_num_books_read(self): 
		# add some books to the list, and test num_books matches expected.
		my_books = BookLover("Victoria", "email.com", "fantasy")
		my_books.add_book("ACOTAR", 5)
		my_books.add_book("ACOMAF", 5)
		my_books.add_book("ACOWAR", 5)
		my_books.add_book("ACOFAS", 5)
		my_books.add_book("ACOSF", 5)
		self.assertEqual(my_books.num_books_read(), 5)
		
	def test_6_fav_books(self):
		# add some books with ratings to the list, making sure some of them have rating > 3. 
		# Your test should check that the returned books have rating  > 3
		my_books = BookLover("Victoria", "email.com", "fantasy")
		my_books.add_book("ACOTAR", 5)
		my_books.add_book("ACOMAF", 5)
		my_books.add_book("It Ends W Us", 2)
		my_fav_books = my_books.fav_books()
		self.assertTrue(sum(my_fav_books.book_rating > 3) == 2)
                
if __name__ == '__main__':
	unittest.main(verbosity=3)