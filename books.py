import utility
import sorts
#Import the other two files
bookshelf = utility.load_books(#Insert file path of csv here.)
for book in bookshelf:
  print(book['title'])
 
def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']
  sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
  for book in sort_1:
    print(book['title'])
def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']
  bookshelf_v1 = bookshelf
  sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
bookshelf_v2 = bookshelf.copy()
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
def by_total_length(book_a, book_b):
  return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])
long_bookshelf = utility.load_books('books_large.csv')
sort3 = sorts.bubble_sort(long_bookshelf, by_total_length)
sort4 = sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)
