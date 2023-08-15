import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
for book in bookshelf:
  print(book['title'])
print(ord("a"))
print(ord(" "))
print(ord("A"))
 
def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']
  sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
  for book in sort_1:
    print(book['title'])
def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']
  bookshelf_v1 = bookshelf
  sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)